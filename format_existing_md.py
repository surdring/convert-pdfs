from __future__ import annotations

import argparse
from pathlib import Path

from pdf_ocr_md.markdown.postprocess import postprocess_markdown


def format_md_file(path: Path) -> bool:
    """对单个 Markdown 文件执行二次格式化。

    返回是否发生了内容变更。
    """

    original = path.read_text(encoding="utf-8")
    formatted = postprocess_markdown(original)

    if formatted == original or formatted.strip() == original.strip():
        return False

    path.write_text(formatted, encoding="utf-8")
    return True


def iter_md_files(target: Path):
    """遍历目标路径下的所有 .md 文件。

    - 如果 target 是文件且后缀为 .md，则只处理该文件；
    - 如果是目录，则递归查找其中的 .md 文件。
    """

    if target.is_file():
        if target.suffix.lower() == ".md":
            yield target
        return

    for p in target.rglob("*.md"):
        if p.is_file():
            yield p


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "对已有的 Markdown 文件执行 HTML→Markdown 二次格式化，"
            "使用项目内的 postprocess_markdown 逻辑。"
        )
    )
    parser.add_argument(
        "path",
        type=str,
        help="要处理的路径，可以是单个 .md 文件或包含 .md 的目录",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="只显示将要处理的文件，不实际写回",
    )

    args = parser.parse_args()
    target = Path(args.path).expanduser().resolve()

    if not target.exists():
        raise SystemExit(f"路径不存在: {target}")

    changed_count = 0
    total_count = 0

    for md_file in iter_md_files(target):
        total_count += 1
        if args.dry_run:
            print(f"[DRY-RUN] 将处理: {md_file}")
            continue

        changed = format_md_file(md_file)
        status = "修改" if changed else "未变化"
        print(f"[{status}] {md_file}")
        if changed:
            changed_count += 1

    if args.dry_run:
        print(f"共发现 {total_count} 个 Markdown 文件（预览模式，不做修改）")
    else:
        print(f"共处理 {total_count} 个 Markdown 文件，其中 {changed_count} 个发生变更")


if __name__ == "__main__":  # pragma: no cover
    main()
