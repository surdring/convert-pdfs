from __future__ import annotations

import re

from markdownify import markdownify as html2markdown


def _is_noise_line(line: str) -> bool:
    s = line.strip()
    if not s:
        return False

    if all(ch in ".-_=·*" for ch in s) and len(s) >= 6:
        return True

    if s.isdigit():
        return True
    if (s.startswith("(") and s.endswith(")")) or (s.startswith("（") and s.endswith("）")):
        inner = s[1:-1].strip()
        if inner.isdigit():
            return True

    has_alpha = any(ch.isalpha() for ch in s)
    has_cjk = any("\u4e00" <= ch <= "\u9fff" for ch in s)
    if not (has_alpha or has_cjk) and any(ch.isdigit() for ch in s):
        return True

    return False


def _clean_lines(md: str) -> str:
    lines = []
    for raw_line in md.splitlines():
        line = raw_line.rstrip()
        if _is_noise_line(line):
            continue
        lines.append(line)

    cleaned_lines = []
    empty_count = 0
    for line in lines:
        if line.strip():
            empty_count = 0
            cleaned_lines.append(line)
        else:
            empty_count += 1
            if empty_count <= 2:
                cleaned_lines.append("")

    return "\n".join(cleaned_lines).strip() + "\n"


def postprocess_markdown(md: str) -> str:
    """对 Markdown 文本做简单清洗与格式优化。"""

    # 先将内联 HTML（div/p/h1/table 等）转换为 Markdown
    md = html2markdown(md, heading_style="ATX")

    # 合并多余的空行
    md = re.sub(r"\n{3,}", "\n\n", md)

    # 进一步按行清洗噪音并压缩空行
    return _clean_lines(md)
