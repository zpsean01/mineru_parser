import time
import logging
from pathlib import Path
from typing import Optional

from modules.config import Config
from modules.api_client import MineruClient
from modules import utils

logger = logging.getLogger(__name__)


class SingleParser:
    def __init__(self, client: Optional[MineruClient] = None):
        self.client = client or MineruClient()

    def submit_task(
        self,
        file_url: str,
        model_version: str = "vlm",
        is_ocr: Optional[bool] = None,
        enable_formula: Optional[bool] = None,
        enable_table: Optional[bool] = None,
        language: Optional[str] = None,
        data_id: Optional[str] = None,
        page_ranges: Optional[str] = None,
        extra_formats: Optional[list[str]] = None,
        no_cache: Optional[bool] = None,
        cache_tolerance: Optional[int] = None,
    ) -> str:
        data = {"url": file_url, "model_version": model_version}

        if is_ocr is not None:
            data["is_ocr"] = is_ocr
        if enable_formula is not None:
            data["enable_formula"] = enable_formula
        if enable_table is not None:
            data["enable_table"] = enable_table
        if language is not None:
            data["language"] = language
        if data_id is not None:
            data["data_id"] = data_id
        if page_ranges is not None:
            data["page_ranges"] = page_ranges
        if extra_formats is not None:
            data["extra_formats"] = extra_formats
        if no_cache is not None:
            data["no_cache"] = no_cache
        if cache_tolerance is not None:
            data["cache_tolerance"] = cache_tolerance

        result = self.client._request("POST", "/api/v4/extract/task", json=data)
        task_id = result["task_id"]
        logger.info("解析任务已提交，task_id: %s", task_id)
        return task_id

    def query_task(self, task_id: str) -> dict:
        return self.client._request("GET", f"/api/v4/extract/task/{task_id}")

    def wait_for_result(
        self,
        task_id: str,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
    ) -> dict:
        poll_interval = poll_interval or Config.POLL_INTERVAL
        poll_timeout = poll_timeout or Config.POLL_TIMEOUT
        deadline = time.time() + poll_timeout

        while True:
            if time.time() > deadline:
                raise TimeoutError(
                    f"轮询超时（{poll_timeout}s），task_id: {task_id}"
                )

            data = self.query_task(task_id)
            state = data.get("state")
            extract_progress = data.get("extract_progress", {})

            if state == "running":
                ep = extract_progress.get("extracted_pages", 0)
                tp = extract_progress.get("total_pages", 0)
                logger.info("解析中… %s/%s 页", ep, tp)
            elif state == "pending":
                logger.info("排队中…")
            elif state == "converting":
                logger.info("格式转换中…")
            elif state == "done":
                logger.info("解析完成！task_id: %s", task_id)
                return data
            elif state == "failed":
                err = data.get("err_msg", "未知错误")
                raise RuntimeError(f"解析失败: {err}")
            else:
                logger.info("当前状态: %s", state)

            time.sleep(poll_interval)

    def _discover_total_pages(
        self,
        task_id: str,
        poll_interval: int = 2,
        timeout: int = 120,
    ) -> int:
        deadline = time.time() + timeout
        while time.time() < deadline:
            data = self.query_task(task_id)
            state = data.get("state")
            extract_progress = data.get("extract_progress", {})

            if state == "running" and extract_progress.get("total_pages"):
                return extract_progress["total_pages"]
            if state == "done":
                tp = extract_progress.get("total_pages", 0)
                if tp:
                    return tp
                return 0
            if state == "failed":
                raise RuntimeError(
                    f"无法获取文档页数: {data.get('err_msg', '未知错误')}"
                )
            time.sleep(poll_interval)
        raise TimeoutError("获取文档总页数超时")

    def _download_result(
        self,
        task_id: str,
        result_data: dict,
        output_path: Path,
        auto_extract: bool,
    ) -> dict:
        zip_url = result_data.get("full_zip_url")
        if not zip_url:
            raise RuntimeError("解析完成但未获取到下载链接")

        zip_name = f"{task_id}.zip"
        zip_path = utils.download_file(zip_url, output_path / zip_name)

        result = {"task_id": task_id, "zip_path": str(zip_path)}

        if auto_extract:
            extract_dir = utils.extract_zip(zip_path, output_path / task_id)
            files = utils.list_result_files(extract_dir)
            result["extract_dir"] = str(extract_dir)
            result["files"] = files

        return result

    def parse_url(
        self,
        file_url: str,
        output_dir: Optional[str] = None,
        auto_extract: bool = True,
        auto_split: bool = False,
        total_pages: Optional[int] = None,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs,
    ) -> dict:
        poll_interval = poll_interval or Config.POLL_INTERVAL
        poll_timeout = poll_timeout or Config.POLL_TIMEOUT

        if not auto_split:
            return self._parse_single(file_url, output_dir, auto_extract,
                                      poll_interval, poll_timeout, **kwargs)

        return self._parse_with_splitting(file_url, total_pages, output_dir,
                                          auto_extract, poll_interval,
                                          poll_timeout, **kwargs)

    def _parse_single(
        self,
        file_url: str,
        output_dir: Optional[str],
        auto_extract: bool,
        poll_interval: int,
        poll_timeout: int,
        **kwargs,
    ) -> dict:
        task_id = self.submit_task(file_url, **kwargs)
        result_data = self.wait_for_result(task_id, poll_interval, poll_timeout)
        output_path = Config.DATA_DIR if output_dir is None else Path(output_dir)
        return self._download_result(task_id, result_data, output_path, auto_extract)

    def _parse_with_splitting(
        self,
        file_url: str,
        total_pages: Optional[int],
        output_dir: Optional[str],
        auto_extract: bool,
        poll_interval: int,
        poll_timeout: int,
        **kwargs,
    ) -> dict:
        output_path = Config.DATA_DIR if output_dir is None else Path(output_dir)

        first_task_id = self.submit_task(file_url, page_ranges="1-200", **kwargs)

        if total_pages is None:
            logger.info("正在探测文档总页数…")
            total_pages = self._discover_total_pages(first_task_id)

        if total_pages <= 200:
            logger.info("文档共 %s 页，无需分片", total_pages)
            result_data = self.wait_for_result(
                first_task_id, poll_interval, poll_timeout
            )
            return self._download_result(first_task_id, result_data, output_path, auto_extract)

        logger.info("文档共 %s 页（超过 200 页），自动分片解析", total_pages)
        ranges = utils.build_page_ranges(total_pages)

        remaining_tasks = []
        for pr in ranges[1:]:
            task_id = self.submit_task(file_url, page_ranges=pr, **kwargs)
            remaining_tasks.append(task_id)

        chunks = []
        logger.info("等待分片任务完成（共 %d 片）…", len(ranges))
        all_task_ids = [first_task_id] + remaining_tasks

        for i, task_id in enumerate(all_task_ids):
            result_data = self.wait_for_result(task_id, poll_interval, poll_timeout)
            chunk_result = self._download_result(
                task_id, result_data, output_path, auto_extract
            )
            chunk_result["chunk_index"] = i
            chunk_result["page_range"] = ranges[i]
            chunks.append(chunk_result)

        return {
            "total_pages": total_pages,
            "chunks": chunks,
        }
