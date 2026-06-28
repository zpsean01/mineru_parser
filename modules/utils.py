import zipfile
from pathlib import Path
from typing import Optional
import requests


def download_file(url: str, save_path: Path, timeout: int = 300) -> Path:
    save_path = Path(save_path)
    save_path.parent.mkdir(parents=True, exist_ok=True)

    with requests.get(url, stream=True, timeout=timeout) as r:
        r.raise_for_status()
        with open(save_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    return save_path


def extract_zip(zip_path: Path, extract_dir: Optional[Path] = None) -> Path:
    zip_path = Path(zip_path)
    if extract_dir is None:
        extract_dir = zip_path.parent / zip_path.stem
    extract_dir = Path(extract_dir)
    extract_dir.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(zip_path, "r") as zf:
        zf.extractall(extract_dir)
    return extract_dir


def list_result_files(extract_dir: Path) -> dict:
    extract_dir = Path(extract_dir)
    result = {}
    for f in extract_dir.iterdir():
        if f.is_file():
            result[f.name] = str(f)
    return result


def build_page_ranges(total_pages: int, chunk_size: int = 200) -> list[str]:
    ranges = []
    start = 1
    while start <= total_pages:
        end = min(start + chunk_size - 1, total_pages)
        ranges.append(f"{start}-{end}")
        if end == total_pages:
            break
        start = end
    return ranges
