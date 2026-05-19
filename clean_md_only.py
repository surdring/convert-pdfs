#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable, List

from pdf_ocr_md.markdown.postprocess import postprocess_markdown


def iter_md_files(target: Path) -> Iterable[Path]:
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


def _is_noise_line(line: str) -> bool:
    """判断一行是否为明显噪音行（如纯点线、分隔线、单独页码等）。"""
    s = line.strip()
    if not s:
        return False

    # 只包含重复的符号：点、横线、下划线等
    if all(ch in ".-_=·*" for ch in s) and len(s) >= 6:
        return True

    # 常见页码独占一行的情况："109"、"(109)"、"（109）"
    if s.isdigit():
        return True
    if (s.startswith("(") and s.endswith(")")) or (s.startswith("（") and s.endswith("）")):
        inner = s[1:-1].strip()
        if inner.isdigit():
            return True

    # 只包含数字和常见标点（不含任何字母或汉字）的行，也视为噪音
    # 例如："...... 109"、"--- (45) ---"，但会保留含有中文或字母的目录/标题行
    has_alpha = any(ch.isalpha() for ch in s)
    has_cjk = any("\u4e00" <= ch <= "\u9fff" for ch in s)
    if not (has_alpha or has_cjk) and any(ch.isdigit() for ch in s):
        return True

    return False


def clean_markdown_text(text: str) -> str:
    """对 Markdown 文本做轻量清洗：

    - 使用项目内的 postprocess_markdown 做基础格式化；
    - 删除噪音行（分隔线、纯页码行等）；
    - 合理压缩空行（最多允许连续 2 行空行）。
    """
    return postprocess_markdown(text)


def format_md_file(path: Path, encoding: str = "utf-8") -> bool:
    """对单个 Markdown 文件执行清洗，返回是否发生内容变更。"""
    original = path.read_text(encoding=encoding)
    cleaned = clean_markdown_text(original)

    if cleaned == original:
        return False

    path.write_text(cleaned, encoding=encoding)
    return True


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "对已有的 Markdown 文件执行二次清洗：使用 postprocess_markdown 并去除分隔线/页码等噪音，"
            "不做切分，只在原文件上就地覆盖。"
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
    parser.add_argument(
        "--encoding",
        type=str,
        default="utf-8",
        help="读取/写入文件使用的编码，默认 utf-8",
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
            print(f"[DRY-RUN] 将清洗: {md_file}")
            continue

        changed = format_md_file(md_file, encoding=args.encoding)
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
