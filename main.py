"""MinerU PDF 解析工具 — 在线 API 封装

通过 MinerU 精准解析 API 对 PDF 等文件进行解析。

用法:
    python main.py single <file_url> [参数...]
    python main.py batch <file_path1> [file_path2 ...] [参数...]
    python main.py parse <file_path> [参数...]

配置:
    config.json 或 .env 中配置 Token (https://mineru.net/apiManage)
"""

import argparse
import json
import logging
import sys

from modules.config import Config
from modules.single_parser import SingleParser
from modules.batch_parser import BatchParser
from modules.local_parser import LocalParser

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("main")


def build_shared_args(parser: argparse.ArgumentParser):
    parser.add_argument(
        "--model-version",
        default="vlm",
        choices=["pipeline", "vlm", "MinerU-HTML"],
        help="MinerU 模型版本（默认 vlm）",
    )
    parser.add_argument("--enable-formula", action="store_true", default=None)
    parser.add_argument("--no-formula", dest="enable_formula", action="store_false")
    parser.add_argument("--enable-table", action="store_true", default=None)
    parser.add_argument("--no-table", dest="enable_table", action="store_false")
    parser.add_argument(
        "--language", default=None, choices=["ch", "en", "auto"],
        help="文档语言（默认 ch）"
    )
    parser.add_argument(
        "--output-dir",
        default=None,
        help="结果保存目录（默认 ./data/文件名）",
    )
    parser.add_argument(
        "--no-extract",
        action="store_true",
        help="不自动解压结果 ZIP",
    )
    parser.add_argument(
        "--poll-interval",
        type=int,
        default=None,
        help="轮询间隔秒数（默认 5）",
    )
    parser.add_argument(
        "--poll-timeout",
        type=int,
        default=None,
        help="轮询超时秒数（默认 1800）",
    )
    parser.add_argument(
        "--auto-split",
        action="store_true",
        default=False,
        help="自动分片：页数 > 200 时以 200 页为一片自动拆分（重叠 1 页衔接）",
    )
    parser.add_argument(
        "--total-pages",
        type=int,
        default=None,
        help="文档总页数（配合 --auto-split 使用，省略时自动探测）",
    )


def _build_parse_kwargs(args) -> dict:
    kwargs = {
        "model_version": args.model_version,
        "output_dir": args.output_dir,
        "auto_extract": not args.no_extract,
        "auto_split": args.auto_split,
        "total_pages": args.total_pages,
        "poll_interval": args.poll_interval,
        "poll_timeout": args.poll_timeout,
    }
    for key in ("enable_formula", "enable_table", "language"):
        val = getattr(args, key, None)
        if val is not None:
            kwargs[key] = val
    return kwargs


def cmd_single(args: argparse.Namespace):
    parser = SingleParser()
    kwargs = _build_parse_kwargs(args)
    result = parser.parse_url(args.file_url, **kwargs)
    print("\n✅ 解析完成！")
    print(json.dumps(result, ensure_ascii=False, indent=2))


def cmd_batch(args: argparse.Namespace):
    parser = BatchParser()
    file_paths = args.file_paths
    kwargs = {"model_version": args.model_version}
    for key in ("enable_formula", "enable_table", "language"):
        val = getattr(args, key, None)
        if val is not None:
            kwargs[key] = val

    batch_id = parser.parse_local_files(file_paths, **kwargs)
    print(f"\n✅ 批量上传完成！batch_id: {batch_id}")
    print("系统将自动提交解析任务，请到 MinerU 控制台查看进度。")


def cmd_parse(args: argparse.Namespace):
    parser = LocalParser()
    kwargs = _build_parse_kwargs(args)

    result = parser.parse_file(args.file_path, **kwargs)

    if "chunks" in result:
        print(f"\n✅ 解析完成！文档共 {result['total_pages']} 页，分为 {len(result['chunks'])} 片：")
        for c in result["chunks"]:
            ed = c.get("extract_dir", c.get("zip_path", ""))
            print(f"  第 {c['chunk_index']+1} 片 ({c['page_range']}): {ed}")
    else:
        ed = result.get("extract_dir", result.get("zip_path", ""))
        print(f"\n✅ 解析完成！结果: {ed}")
        files = result.get("files", {})
        if files:
            for name, path in files.items():
                print(f"  {name}")

    print(json.dumps(result, ensure_ascii=False, indent=2))


def main():
    Config.validate()

    root_parser = argparse.ArgumentParser(
        description="MinerU PDF 解析工具 — 在线 API 封装",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "示例:\n"
            "  # 通过 URL 解析单个文件\n"
            "  python main.py single https://example.com/doc.pdf\n\n"
            "  # 解析本地文件（上传→轮询→下载）\n"
            "  python main.py parse report.pdf\n\n"
            "  # 解析大文档（自动分片）\n"
            "  python main.py parse large.pdf --auto-split\n\n"
            "  # 批量上传本地文件解析\n"
            "  python main.py batch report1.pdf report2.pdf\n"
        ),
    )
    subparsers = root_parser.add_subparsers(dest="command", required=True)

    # ---- single ----
    single_parser = subparsers.add_parser(
        "single", help="解析单个文件（通过 URL）"
    )
    single_parser.add_argument("file_url", help="文件下载链接")
    build_shared_args(single_parser)
    single_parser.set_defaults(func=cmd_single)

    # ---- batch ----
    batch_parser = subparsers.add_parser(
        "batch", help="批量上传本地文件解析（仅上传，不会自动下载结果）"
    )
    batch_parser.add_argument(
        "file_paths", nargs="+", help="本地文件路径（支持多个）"
    )
    build_shared_args(batch_parser)
    batch_parser.set_defaults(func=cmd_batch)

    # ---- parse ----
    parse_parser = subparsers.add_parser(
        "parse", help="解析本地文件（上传→轮询→下载结果到本地）"
    )
    parse_parser.add_argument("file_path", help="本地文件路径")
    build_shared_args(parse_parser)
    parse_parser.set_defaults(func=cmd_parse)

    args = root_parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error("程序运行失败: %s", e)
        sys.exit(1)
