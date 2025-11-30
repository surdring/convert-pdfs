# 目录批量 PDF → Markdown 转换工具

## 项目结构与关键模块设计

> 基于自建 Llama.cpp OCR 模型的异步 Python 脚本

---

## 1. 目标回顾

- **批量范围**：对指定根目录下（含子目录）的所有 PDF 文件进行批量处理。
- **处理方式**：
  - 按 PDF **分页**，将每页渲染为图片或读取文本；
  - 调用自建 `chandra-ocr` 模型完成 OCR 与结构化提取；
  - 生成语义清晰、结构友好的 Markdown 文档。
- **并发要求**：整体流程基于 `asyncio` 异步实现，合理控制并发度，避免压垮 OCR 服务。

---

## 2. 整体架构概览

逻辑分层建议：

- **CLI 层**：命令行入口，解析参数，启动异步任务。
- **应用编排层 (orchestrator)**：
  - 负责目录扫描、任务切分（按文件 / 按页）；
  - 调度 PDF 解析、OCR 请求、Markdown 生成三类能力；
  - 控制并发、重试与错误聚合。
- **领域能力层**：
  - **PDF 处理子模块**：扫描、分页、渲染为图片、提取文本层；
  - **OCR 客户端子模块**：与 Llama.cpp `llama-server` 交互；
  - **Markdown 生成子模块**：把 OCR 结果组织为结构化 Markdown。
- **基础设施层**：配置、日志、通用工具、类型定义等。

---

## 3. 推荐项目目录结构

以单一包 + 独立 CLI 脚本方式组织：

```text
project_root/
  convert_pdfs_to_md.py        # CLI 入口（支持命令行参数）
  pdf_ocr_md/                  # 主包
    __init__.py

    config.py                  # 配置加载与数据模型
    logging_utils.py           # 日志初始化与统一封装
    types_.py                  # 常用类型与数据结构（Task、PageResult 等）

    pdf/
      __init__.py
      scanner.py               # 目录递归扫描、PDF 文件发现
      loader.py                # 打开 PDF、获取页数、基础元数据
      renderer.py              # 将页面渲染为图片，或提取文本层

    ocr/
      __init__.py
      client.py                # 与 llama-server 的 HTTP 交互（async）
      prompts.py               # OCR 提示词模版（试卷/书籍/报告等可扩展）

    markdown/
      __init__.py
      writer.py                # 将页级 OCR 结果组装成 Markdown 文本
      postprocess.py           # 文本清洗、合并段落、简单排版优化

    orchestrator.py            # 异步任务编排：并发控制、重试、错误处理

  tests/
    test_scanner.py
    test_renderer.py
    test_ocr_client.py
    test_markdown_writer.py

  requirements.txt             # 运行依赖（PyPDF2 / pdf2image / httpx[aio] 等）
  README.md                    # 使用说明（可引用需求 & 设计文档）
```

> 上述只是逻辑结构，实际放置路径可以按你现有仓库布局微调，比如放在 `scripts/` 或单独仓库中。

---

## 4. 关键模块设计

### 4.1 命令行入口：`convert_pdfs_to_md.py`

**职责**：

- 解析命令行参数：
  - `--input-dir` 输入根目录；
  - `--output-dir` 输出根目录；
  - `--server-url` OCR 服务地址；
  - `--model` 模型别名（默认 `chandra-ocr`）；
  - `--max-concurrency` 最大并发数；
  - `--max-retries` 最大重试次数；
  - 请求超时、单次处理页数等可选参数。
- 调用 `pdf_ocr_md.config` 构建配置对象。
- 初始化日志（调用 `logging_utils`）。
- 调用 `asyncio.run(main(config))` 进入编排层。

### 4.2 配置与类型模块：`config.py` / `types_.py`

**`config.py` 建议内容**：

- `AppConfig`：整体配置数据类，包括：
  - 输入输出目录、并发数、重试次数；
  - OCR 服务 URL、模型名、超时时间；
  - 每次请求最大页数/最大 token 估算参数。
- 从命令行参数或环境变量加载配置的辅助函数。

**`types_.py` 建议内容**：

- `PdfTask`：单个 PDF 转换任务描述（路径、目标输出路径、页数等）。
- `PageTask`：单页或多页 OCR 子任务描述。
- `PageOcrResult`：单页 OCR 结果（页号、纯文本、原始模型响应等）。
- `FileConvertResult`：单个 PDF 转换的聚合结果（成功/失败、失败页列表等）。

### 4.3 目录扫描与 PDF 处理：`pdf/scanner.py`、`pdf/loader.py`、`pdf/renderer.py`

**`scanner.py`**：

- 递归遍历 `input_dir`，过滤出 `.pdf` 文件。
- 生成 `PdfTask` 列表，并负责映射到输出路径（镜像目录结构）。

**`loader.py`**：

- 使用 PDF 库（如 `PyPDF2` / `pypdf`）打开 PDF：
  - 获取总页数；
  - 读取基础信息（标题、作者等，可选）。

**`renderer.py`**：

- 将指定页渲染成图片：
  - 可使用 `pdf2image`、`fitz(PyMuPDF)` 等库；
  - 输出为内存中的图像对象或临时文件路径。
- 可选：尝试从 PDF 文本层直接提取文字，作为 OCR 的补充或替代。

### 4.4 OCR 客户端：`ocr/client.py`、`ocr/prompts.py`

**`client.py`**：

- 基于 `httpx`（异步）封装：
  - `async def ocr_page(image, config, prompt_template) -> PageOcrResult`；
  - 构造 `/v1/chat/completions` 请求体：
    - `model: chandra-ocr`；
    - `messages`: 带有系统/用户指令与图像。
- 支持：
  - 超时控制；
  - 重试机制（网络错误/5xx）；
  - 对 400 错误中特别是 `context size` 超限做特殊处理（可返回特定错误码）。

**`prompts.py`**：

- 定义不同场景下的 OCR 指令模版，例如：
  - 通用文本页（试卷、书籍）；
  - 表格/代码页（提示输出 Markdown 表格或代码块）。
- 对外暴露按“文档类型”或“页类型”选择模版的函数。

### 4.5 Markdown 生成：`markdown/writer.py`、`markdown/postprocess.py`

**`writer.py`**：

- 输入：`PdfTask`、`[PageOcrResult]`。
- 输出：完整 Markdown 字符串：
  - 顶部：`# <原 PDF 文件名>`；
  - 逐页追加：
    - `## Page N` 或 `---` 作为分隔；
    - 插入对应页的 OCR 文本。
- 对于失败页：
  - 插入 `> [OCR FAILED] Page N` 等占位符；
  - 记录至文末“失败页列表”。

**`postprocess.py`**：

- 可选文本清洗与格式优化，例如：
  - 去除重复换行；
  - 合并被错误切分的段落；
  - 简单修正项目符号/编号格式。

### 4.6 编排模块：`orchestrator.py`

**核心职责**：

- 根据 `AppConfig` 和 `PdfTask` 列表：
  - 控制 **文件级并发**（例如多个 PDF 并行）；
  - 对单个 PDF 内部按页串行或小并发执行 OCR（避免超载）。
- 使用 `asyncio.Semaphore` 限制整体并发数。
- 为每个 PDF：
  - 调用 PDF 解析/渲染得到页任务列表；
  - 逐页调度 `ocr.client`；
  - 收集结果并调用 `markdown.writer` 生成 `.md`；
  - 写入目标路径。
- 负责聚合日志与最终统计信息。

---

## 5. 错误处理与重试策略

- **网络与服务错误**：
  - 对连接错误、5xx 响应进行有限次重试（配置 `max_retries` + 间隔策略）。
- **上下文超限**：
  - 若服务返回 `the request exceeds the available context size`：
    - 当前设计中单次仅处理 1 页，理论上不应触发；
    - 如触发，可记录为该页失败并继续处理其余页面。
- **文件级失败**：
  - 若某 PDF 所有页都失败，则将该文件标记为失败任务；
  - 不影响其他文件的处理。

---

## 6. 测试与验证

- **单元测试**：
  - 对 `scanner`、`renderer` 使用本地小 PDF 样例测试页数与渲染正确性；
  - 对 `ocr.client` 进行 HTTP 调用 mock 测试，请求体结构与错误分支；
  - 对 `markdown.writer` 验证分页标题、失败页占位符等是否符合预期。
- **集成测试（小规模）**：
  - 选取少量多页 PDF，验证从目录到 Markdown 的完整流程；
  - 观察并发下对 llama-server 的压力与响应时间。

---

## 7. 后续可扩展点

- 支持：
  - 文档类型自动识别 → 自动选择不同 OCR prompt；
  - 将结果直接写入知识库或搜索索引，而不仅是 `.md` 文件；
  - 通过 REST API 或任务队列包装成服务，供其他系统调度。

以上结构可以作为接下来编写异步 Python 实现时的蓝本。
