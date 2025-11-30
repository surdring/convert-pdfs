from __future__ import annotations

DEFAULT_PROMPT = (
    "你是一个高质量的 OCR + Markdown 排版助手。"
    "请识别图片中的中文和英文文本，保持原有的标题层级、列表、段落结构，"
    "尽量用 Markdown 语法（# 标题、- 列表、``` 代码块、| 表格 等）表达。"
)


PROMPTS = {
    "default": DEFAULT_PROMPT,
}


def get_prompt(preset: str = "default") -> str:
    """根据预设名称返回对应的 OCR prompt。"""
    return PROMPTS.get(preset, DEFAULT_PROMPT)
