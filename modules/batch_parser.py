import logging
import time
from pathlib import Path
from typing import Optional

import requests

from modules.api_client import MineruClient
from modules.config import Config

logger = logging.getLogger(__name__)


class BatchParser:
    def __init__(self, client: Optional[MineruClient] = None):
        self.client = client or MineruClient()

    def parse_local_files(
        self,
        file_paths: list[str | Path],
        model_version: str = "vlm",
        enable_formula: Optional[bool] = None,
        enable_table: Optional[bool] = None,
        language: Optional[str] = None,
        data_ids: Optional[list[str]] = None,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        auto_download: bool = False,
    ) -> dict:
        file_paths = [Path(p) for p in file_paths]
        files_payload = []
        for i, fp in enumerate(file_paths):
            entry = {"name": fp.name}
            if enable_formula is not None:
                entry["enable_formula"] = enable_formula
            if enable_table is not None:
                entry["enable_table"] = enable_table
            if language is not None:
                entry["language"] = language
            if data_ids and i < len(data_ids):
                entry["data_id"] = data_ids[i]
            files_payload.append(entry)

        result = self.client._request(
            "POST", "/api/v4/file-urls/batch",
            json={"files": files_payload, "model_version": model_version},
        )
        batch_id = result["batch_id"]
        upload_urls = result["file_urls"]
        logger.info("batch_id: %s，文件数: %d", batch_id, len(upload_urls))

        for url, fp in zip(upload_urls, file_paths):
            if not fp.exists():
                raise FileNotFoundError(f"文件不存在: {fp}")
            logger.info("上传 %s …", fp.name)
            with open(fp, "rb") as f:
                resp = requests.put(url, data=f, timeout=600)
            if resp.status_code != 200:
                raise RuntimeError(f"上传失败 [{resp.status_code}]: {fp.name}")
            logger.info("上传成功: %s", fp.name)

        logger.info("所有文件上传完成")

        if auto_download:
            from modules import utils
            output_path = Config.DATA_DIR
            extract_results = self._poll_batch(batch_id, poll_interval, poll_timeout)
            results = []
            for entry in extract_results:
                file_name = entry.get("file_name", "?")
                item = {"file_name": file_name, "state": "done"}
                zip_url = entry.get("full_zip_url")
                if zip_url:
                    file_output = output_path / f"{file_name}-{batch_id}"
                    file_output.mkdir(parents=True, exist_ok=True)
                    zip_name = f"{file_name}-{batch_id}.zip"
                    zip_path = file_output / zip_name
                    utils.download_file(zip_url, zip_path)
                    item["zip_path"] = str(zip_path)
                    extract_dir = utils.extract_zip(zip_path, file_output)
                    item["extract_dir"] = str(extract_dir)
                    item["files"] = utils.list_result_files(extract_dir)
                results.append(item)
            return {"batch_id": batch_id, "results": results}

        return {"batch_id": batch_id}

    def _poll_batch(
        self,
        batch_id: str,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
    ) -> list[dict]:
        poll_interval = poll_interval or Config.POLL_INTERVAL
        poll_timeout = poll_timeout or Config.POLL_TIMEOUT
        deadline = time.time() + poll_timeout

        while True:
            if time.time() > deadline:
                raise TimeoutError(f"轮询超时（{poll_timeout}s），batch_id: {batch_id}")

            result = self.client._request(
                "GET", f"/api/v4/extract-results/batch/{batch_id}"
            )
            extract_results = result.get("extract_result", [])

            if not extract_results:
                logger.info("等待系统提交解析任务…")
                time.sleep(poll_interval)
                continue

            all_done = True
            for entry in extract_results:
                state = entry.get("state")
                fn = entry.get("file_name", "?")
                if state == "done":
                    logger.info("%s: 完成", fn)
                elif state == "failed":
                    raise RuntimeError(f"{fn} 解析失败: {entry.get('err_msg', '未知错误')}")
                elif state == "running":
                    ep = entry.get("extract_progress", {}).get("extracted_pages", 0)
                    tp = entry.get("extract_progress", {}).get("total_pages", 0)
                    logger.info("%s: 解析中 (%s/%s)", fn, ep, tp)
                    all_done = False
                else:
                    logger.info("%s: 状态: %s", fn, state)
                    all_done = False

            if all_done:
                return extract_results

            time.sleep(poll_interval)
