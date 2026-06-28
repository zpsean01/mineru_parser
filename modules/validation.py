import json
import logging
import re
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)


def parse_page_range(page_ranges: str) -> list[tuple[int, int]]:
    """解析 page_ranges 字符串（如 "1-200" 或 "2,4-6"），返回 (start, end) 列表（1-based）"""
    segments = []
    for part in page_ranges.split(","):
        part = part.strip()
        m = re.match(r"^(\d+)-(\d+)$", part)
        if m:
            start, end = int(m.group(1)), int(m.group(2))
        elif re.match(r"^\d+$", part):
            start = end = int(part)
        else:
            continue
        segments.append((start, end))
    return segments


def _find_content_file(extract_dir: Path) -> Optional[Path]:
    for f in extract_dir.iterdir():
        if f.is_file() and f.name.endswith("_content_list.json") and "_v2" not in f.name:
            return f
    return None


def _find_content_v2_file(extract_dir: Path) -> Optional[Path]:
    for f in extract_dir.iterdir():
        if f.is_file() and f.name.endswith("_content_list_v2.json"):
            return f
    return None


def _find_layout_file(extract_dir: Path) -> Optional[Path]:
    fp = extract_dir / "layout.json"
    return fp if fp.exists() else None


def validate_page_range(
    extract_dir: str | Path,
    expected_range: str,
    strict: bool = False,
) -> dict:
    """验证提取结果是否在期望的 page_range 内。

    Args:
        extract_dir: 解压后的结果目录
        expected_range: 期望的页码范围，如 "1-200"
        strict: 严格模式 — 超出范围视为失败

    Returns:
        {"valid": bool, "actual_pages": int, "page_idx_range": (min, max),
         "expected_pages": int, "details": str}
    """
    extract_dir = Path(extract_dir)
    if not extract_dir.exists():
        return {"valid": False, "error": "目录不存在: %s" % extract_dir}

    segments = parse_page_range(expected_range)
    if not segments:
        return {"valid": True, "info": "page_range 格式无法解析"}

    expected_start = segments[0][0]  # 1-based
    expected_end = segments[-1][1]    # 1-based
    expected_count = expected_end - expected_start + 1
    expected_idxs = set(range(expected_start - 1, expected_end))  # 转为 0-based

    # 方法1：通过 content_list_v2 长度获取页数
    v2_file = _find_content_v2_file(extract_dir)
    if v2_file:
        try:
            v2_data = json.loads(v2_file.read_text(encoding="utf-8"))
            actual_count = len(v2_data) if isinstance(v2_data, list) else 0
            if actual_count != expected_count:
                logger.warning("页数不匹配: 期望 %d (range=%s), 实际 %d", expected_count, expected_range, actual_count)
                return {"valid": False, "actual_pages": actual_count, "page_idx_range": None,
                        "expected_pages": expected_count,
                        "error": "页数不匹配: 期望 %d, 实际 %d" % (expected_count, actual_count)}
            return {"valid": True, "actual_pages": actual_count, "page_idx_range": (expected_start - 1, expected_end - 1),
                    "expected_pages": expected_count, "details": "content_list_v2 页数匹配"}
        except Exception as e:
            logger.warning("读取 content_list_v2 失败: %s", e)

    # 方法2：通过 content_list.json 中的 page_idx 获取
    c1_file = _find_content_file(extract_dir)
    if c1_file:
        try:
            c1_data = json.loads(c1_file.read_text(encoding="utf-8"))
            page_idxes = set()
            for item in c1_data if isinstance(c1_data, list) else []:
                pi = item.get("page_idx")
                if pi is not None:
                    page_idxes.add(pi)
            if page_idxes:
                actual_min, actual_max = min(page_idxes), max(page_idxes)
                actual_set = page_idxes
                if actual_set == expected_idxs:
                    return {"valid": True, "actual_pages": len(actual_set),
                            "page_idx_range": (actual_min, actual_max),
                            "expected_pages": expected_count,
                            "details": "content_list page_idx 完全匹配"}

                missing = expected_idxs - actual_set
                extra = actual_set - expected_idxs
                if strict and (missing or extra):
                    return {"valid": False, "actual_pages": len(actual_set),
                            "page_idx_range": (actual_min, actual_max),
                            "expected_pages": expected_count,
                            "error": "page_idx 不匹配: 缺失 %s, 多余 %s" % (sorted(missing)[:5], sorted(extra)[:5])}
                if extra:
                    logger.warning("page_range=%s 实际 page_idx 超出范围: %s", expected_range, sorted(extra))
                    return {"valid": False, "actual_pages": len(actual_set),
                            "page_idx_range": (actual_min, actual_max),
                            "expected_pages": expected_count,
                            "error": "page_idx 超出预期范围: %s" % sorted(extra)[:5]}
                return {"valid": True, "actual_pages": len(actual_set),
                        "page_idx_range": (actual_min, actual_max),
                        "expected_pages": expected_count,
                        "details": "content_list page_idx 在范围内"}
        except Exception as e:
            logger.warning("读取 content_list 失败: %s", e)

    # 方法3：通过 layout.json pdf_info 长度
    layout_file = _find_layout_file(extract_dir)
    if layout_file:
        try:
            layout_data = json.loads(layout_file.read_text(encoding="utf-8"))
            pdf_info = layout_data.get("pdf_info", []) if isinstance(layout_data, dict) else []
            actual_count = len(pdf_info) if isinstance(pdf_info, list) else 0
            if actual_count != expected_count:
                return {"valid": False, "actual_pages": actual_count, "page_idx_range": None,
                        "expected_pages": expected_count,
                        "error": "layout 页数不匹配: 期望 %d, 实际 %d" % (expected_count, actual_count)}
            return {"valid": True, "actual_pages": actual_count, "page_idx_range": None,
                    "expected_pages": expected_count, "details": "layout.json pdf_info 页数匹配"}
        except Exception as e:
            logger.warning("读取 layout.json 失败: %s", e)

    return {"valid": None, "error": "未找到可验证的内容文件 (content_list.json / layout.json)"}
