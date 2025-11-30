from __future__ import annotations

import re

from markdownify import markdownify as html2markdown


def postprocess_markdown(md: str) -> str:
    """对 Markdown 文本做简单清洗与格式优化。"""

    # 先将内联 HTML（div/p/h1/table 等）转换为 Markdown
    md = html2markdown(md, heading_style="ATX")

    # 合并多余的空行
    md = re.sub(r"\n{3,}", "\n\n", md)
    # 去掉首尾多余空白，并保证文件末尾有换行
    return md.strip() + "\n"
