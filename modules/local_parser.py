import logging
import time
from pathlib import Path
from typing import Optional

import requests
from PyPDF2 import PdfReader

from modules.api_client import MineruClient
from modules.config import Config
from modules import utils
from modules.validation import validate_page_range

logger = logging.getLogger(__name__)


class LocalParser:
    def __init__(self, client: Optional[MineruClient] = None):
        self.client = client or MineruClient()

    def _batch_label(self, file_path: Path, page_ranges: Optional[str] = None) -> str:
        label = file_path.name
        if page_ranges:
            label = f"{file_path.stem}_{page_ranges}{file_path.suffix}"
        return label

    def _upload_and_get_batch_id(self, file_path: Path, page_ranges: Optional[str] = None, **kwargs) -> str:
        model = kwargs.get("model_version", "vlm")
        entry = {"name": file_path.name}
        if page_ranges is not None:
            entry["page_ranges"] = page_ranges
        for key in ("enable_formula", "enable_table", "language"):
            val = kwargs.get(key)
            if val is not None:
                entry[key] = val

        result = self.client._request(
            "POST", "/api/v4/file-urls/batch",
            json={"files": [entry], "model_version": model},
        )
        batch_id = result["batch_id"]
        upload_url = result["file_urls"][0]

        logger.info("上传 %s …", file_path.name)
        with open(file_path, "rb") as f:
            resp = requests.put(upload_url, data=f, timeout=600)
        if resp.status_code != 200:
            raise RuntimeError(f"上传失败 [{resp.status_code}]: {file_path.name}")
        logger.info("上传成功，batch_id: %s", batch_id)
        return batch_id

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
                elif state in ("running", "converting"):
                    ep = entry.get("extract_progress", {}).get("extracted_pages", 0)
                    tp = entry.get("extract_progress", {}).get("total_pages", 0)
                    logger.info("%s: %s (%s/%s)", fn, state, ep, tp)
                    all_done = False
                else:
                    logger.info("%s: %s", fn, state)
                    all_done = False

            if all_done:
                return extract_results

            time.sleep(poll_interval)

    def _save_result(self, extract_results: list[dict], label: str, batch_id: str, auto_extract: bool,
                     page_range: Optional[str] = None) -> dict:
        results = []
        for entry in extract_results:
            file_name = entry.get("file_name", "?")
            item = {"file_name": file_name, "state": "done", "batch_id": batch_id}

            zip_url = entry.get("full_zip_url")
            if zip_url:
                zip_name = f"{label}-{batch_id}.zip"
                zip_path = Config.DATA_DIR / zip_name
                utils.download_file(zip_url, zip_path)
                item["zip_path"] = str(zip_path)

                if auto_extract:
                    extract_dir = Config.DATA_DIR / f"{label}-{batch_id}"
                    utils.extract_zip(zip_path, extract_dir)
                    files = utils.list_result_files(extract_dir)
                    item["extract_dir"] = str(extract_dir)
                    item["files"] = files

                    if page_range:
                        v = validate_page_range(extract_dir, page_range)
                        item["validation"] = v
                        if not v.get("valid"):
                            logger.error("分片 %s page_range 验证失败: %s", page_range, v.get("error"))

            results.append(item)

        result = {"results": results}
        if len(results) == 1:
            result.update(results[0])
        return result

    def _detect_total_pages(self, file_path: Path) -> int:
        try:
            reader = PdfReader(str(file_path))
            return len(reader.pages)
        except Exception:
            return 0

    def parse_file(
        self,
        file_path: str | Path,
        output_dir: Optional[str] = None,
        auto_extract: bool = True,
        auto_split: bool = False,
        total_pages: Optional[int] = None,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs,
    ) -> dict:
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"文件不存在: {file_path}")

        if total_pages is None:
            total_pages = self._detect_total_pages(file_path)
            if total_pages:
                logger.info("本地检测页数: %s", total_pages)

        if total_pages and total_pages > 200:
            logger.info("共 %s 页，超过 200 页限制，自动分片解析", total_pages)
            ranges = utils.build_page_ranges(total_pages)

            batch_ids = []
            for pr in ranges:
                logger.info("提交分片 %s …", pr)
                bid = self._upload_and_get_batch_id(file_path, page_ranges=pr, **kwargs)
                batch_ids.append(bid)

            chunks = []
            for i, (bid, pr) in enumerate(zip(batch_ids, ranges)):
                logger.info("等待分片 %d/%d (batch: %s)…", i + 1, len(ranges), bid)
                extract_results = self._poll_batch(bid, poll_interval, poll_timeout)
                label = f"{file_path.stem}_{pr}"
                chunk_result = self._save_result(extract_results, label, bid, auto_extract, page_range=pr)
                chunk_result["chunk_index"] = i
                chunk_result["page_range"] = pr
                chunks.append(chunk_result)

            return {"total_pages": total_pages, "chunks": chunks}

        batch_id = self._upload_and_get_batch_id(file_path, page_ranges=None, **kwargs)
        extract_results = self._poll_batch(batch_id, poll_interval, poll_timeout)
        return self._save_result(extract_results, file_path.stem, batch_id, auto_extract)
