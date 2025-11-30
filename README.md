# 目录批量 PDF → Markdown 转换工具

> 基于自建 Llama.cpp OCR 模型的异步 Python 脚本

本项目提供一个命令行工具，用于对指定目录（含子目录）下的所有 PDF 文件进行批量处理：

- 将 PDF 按页渲染为图片；
- 通过自建 `llama-server` 暴露的 `chandra-ocr` 模型进行 OCR；
- 按页组织为结构化的 Markdown 文档；
- 保持输入/输出目录结构镜像。

核心特点：

- **异步并发**：基于 `asyncio` + `httpx`，支持配置最大并发数，充分利用 OCR 服务能力；
- **分页处理**：以“文件 → 页”为基本任务单元，便于控制上下文长度、失败重试；
- **结构化 Markdown**：以 Markdown 形式保留标题、页分隔与失败页占位信息；
- **可扩展设计**：PDF 处理、OCR 调用、Markdown 生成均按模块拆分，方便后续扩展。

---

## 1. 项目结构

实际代码实现与设计文档中给出的结构基本一致：

```text
project_root/
  convert_pdfs_to_md.py        # CLI 入口（命令行工具）

  pdf_ocr_md/                  # 主包
    __init__.py

    config.py                  # AppConfig 配置模型与构建函数
    logging_utils.py           # 日志初始化
    types_.py                  # 核心数据结构（PdfTask、PageOcrResult 等）

    pdf/
      __init__.py
      scanner.py               # 目录递归扫描、PDF 任务发现
      loader.py                # 获取 PDF 页数
      renderer.py              # 使用 PyMuPDF 将单页渲染为 PNG bytes

    ocr/
      __init__.py
      client.py                # 基于 httpx 的异步 OCR 客户端（/v1/chat/completions）
      prompts.py               # OCR 提示词模板（可扩展不同场景）

    markdown/
      __init__.py
      writer.py                # 将页级 OCR 结果组装为 Markdown 文本
      postprocess.py           # Markdown 文本清洗与简单格式优化

    orchestrator.py            # 异步任务编排：并发控制、调用各子模块

  requirements.txt             # 运行依赖
  README.md                    # 使用说明（当前文件）

  目录批量 PDF → Markdown 转换工具.md                # 需求文档
  目录批量 PDF → Markdown 转换工具-项目结构与模块设计.md  # 设计文档
```

---

## 2. 工作流程概览

1. 从命令行读取配置（输入目录、输出目录、并发数、OCR 服务地址等）；
2. 递归扫描输入根目录，收集所有 `.pdf` 文件，构造 `PdfTask` 列表；
3. 异步并发处理多个 PDF：
   - 读取 PDF 页数；
   - 对每一页：
     - 使用 PyMuPDF 将该页渲染为 PNG 图片；
     - 构造带图片的 Chat Completion 请求，调用 `chandra-ocr`；
     - 收集 OCR 文本或错误信息；
   - 调用 Markdown 模块生成最终 `.md` 文件；
4. 在输出根目录下，以镜像结构写出 Markdown 文件；
5. 全程记录日志，并在结束时输出总体统计（成功/失败文件数、总耗时、平均耗时）。

当前实现中：

- 每个 PDF 在单个信号量保护下处理（**文件级并发**，文件内页是串行 OCR）；
- 所有 PDF 的处理由 `asyncio` 并发调度，最大并发数由 `--max-concurrency` 控制。

---

## 3. 环境准备

### 3.1 Python 环境

- 已安装 Python 3 环境（建议使用虚拟环境，如 `venv` / `conda`）。

#### 3.1.1 在本项目目录中创建虚拟环境（推荐）

```bash
cd /path/to/convert-pdfs  # 进入本项目根目录
python -m venv .venv      # 创建名为 .venv 的虚拟环境
source .venv/bin/activate # 激活虚拟环境（Linux/macOS）
```

如果你使用的是 Windows PowerShell，可以改为：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3.2 安装依赖

在已经激活的虚拟环境中，在项目根目录执行：

```bash
pip install -r requirements.txt
```

`requirements.txt` 中核心依赖：

- `pypdf`：读取 PDF 页数等基础信息；
- `PyMuPDF`（包名 `PyMuPDF`，导入名 `fitz`）：将 PDF 页面渲染为图片；
- `httpx`：异步 HTTP 客户端，请求 `llama-server` 的 `/v1/chat/completions` 接口。

### 3.3 Llama.cpp OCR 服务

你需要先在目标机器上启动 `llama-server`，并暴露 OpenAI Chat 兼容接口。

例如（仅示例，需根据你的实际部署路径和硬件配置调整）：

```bash
HIP_VISIBLE_DEVICES=0 \
./build-hip/bin/llama-server \
  --model /mnt/ssd/models/chandra-ocr/chandra-Q4_K_M.gguf \
  --mmproj /mnt/ssd/models/chandra-ocr/chandra-mmproj-f16.gguf \
  --ctx-size 8192 \
  --n-gpu-layers -1 \
  --threads 16 \
  --batch-size 512 \
  --ubatch-size 128 \
  --parallel 4 \
  --jinja \
  --flash-attn on \
  --host 0.0.0.0 \
  --port 8082 \
  --alias chandra-ocr
```

脚本默认假设：

- 服务地址：`http://0.0.0.0:8082`（可通过 `--server-url` 覆盖）；
- 模型别名：`chandra-ocr`（可通过 `--model` 覆盖）；
- 接口：`POST /v1/chat/completions`，OpenAI Chat 兼容。

---

## 4. 使用方法

### 4.1 配置文件（推荐）

项目使用 `config.toml` 作为默认配置文件，包含所有参数。首次使用前请编辑 `config.toml`：

```toml
[input]
dir = "/path/to/input_pdfs"

[output]
dir = "/path/to/output_mds"

[ocr]
server_url = "http://0.0.0.0:8082"
model = "chandra-ocr"
prompt_preset = "default"

[concurrency]
max_concurrency = 4

[retry]
max_retries = 3
request_timeout = 60.0

[logging]
level = "INFO"
```

### 4.2 运行命令

配置完成后，在项目根目录直接执行：

```bash
python convert_pdfs_to_md.py
```

脚本会自动读取 `config.toml`，无需手动传递参数。

### 4.3 命令行参数覆盖（可选）

如需临时覆盖配置文件中的参数，可在命令行指定：

```bash
python convert_pdfs_to_md.py --max-concurrency 8 --log-level DEBUG
```

#### 4.3.1 断点续传

- **自动断点续传**：脚本会在输出目录为每个 PDF 创建 `.convert_state.json` 状态文件，记录已完成和失败的页号。中断后重新运行会自动跳过已完成的页面。
- **强制重新开始**：如需从头开始，可使用 `--force-restart` 删除所有状态文件：

```bash
python convert_pdfs_to_md.py --force-restart
```

### 4.4 参数说明

| 配置项 | TOML 路径 | 默认值 | 说明 |
| ---- | ---- | ------ | ---- |
| 输入目录 | `input.dir` | 无 | 输入 PDF 根目录，递归扫描 `.pdf` |
| 输出目录 | `output.dir` | 无 | 输出 Markdown 根目录，镜像结构 |
| OCR 服务地址 | `ocr.server_url` | `http://0.0.0.0:8082` | llama-server 地址 |
| 模型别名 | `ocr.model` | `chandra-ocr` | llama-server --alias |
| 最大并发数 | `concurrency.max_concurrency` | `4` | 全局最大并发 OCR 请求数（页级全并发） |
| 最大重试次数 | `retry.max_retries` | `3` | 网络/5xx 错误重试次数 |
| 请求超时 | `retry.request_timeout` | `60.0` | 单次 OCR 请求超时（秒） |
| 日志级别 | `logging.level` | `INFO` | DEBUG/INFO/WARNING/ERROR |
| OCR 提示词 | `ocr.prompt_preset` | `default` | OCR 提示词模板名称 |

### 4.5 输出结构与命名规则

- 输出根目录：由 `output.dir` 指定；
- 子目录结构：每个 PDF 在输出目录下生成一个同名目录；
- Markdown 文件：固定名为 `file.md`，存放在该目录内；
- 状态文件：断点续传状态文件为 `.convert_state.json`，与 `file.md` 同目录。

示例：

```text
test/
├── a.pdf
└── sub/
    └── b.pdf

test_output/
├── a/
│   ├── file.md
│   └── .convert_state.json
└── sub/
    └── b/
        ├── file.md
        └── .convert_state.json
```

### 4.6 日志与统计

- 日志初始化在 `logging_utils.setup_logging` 中完成，输出到标准输出；
- 会记录：
  - 当前处理的 PDF 路径与页数；
  - 每页 OCR 请求的开始与完成；
  - 请求错误（HTTP 状态码、超时、上下文超限等）；
- 脚本结束时，会打印总体统计：
  - 成功转换 PDF 数；
  - 失败 PDF 数及错误信息；
  - 总用时与平均每文件用时。

---

## 5. 内部模块说明（简要）

### 5.1 配置与类型（`config.py` / `types_.py`）

- `AppConfig`：整体配置数据类，包含输入输出目录、并发数、重试次数、OCR 服务地址、模型名、超时时间、prompt preset 等；
- `PdfTask`：单个 PDF 转换任务描述（源路径、目标输出路径、页数）；
- `PageTask`：单页任务描述（目前主要在内部流转）；
- `PageOcrResult`：单页 OCR 结果（页号、文本、成功/失败、错误信息、原始响应）；
- `FileConvertResult`：单个 PDF 转换总体结果（页级结果列表、成功标记、错误信息、耗时）。

### 5.2 PDF 处理（`pdf/scanner.py` / `pdf/loader.py` / `pdf/renderer.py`）

- `scan_pdfs(input_dir, output_dir)`：
  - 使用 `Path.rglob("*.pdf")` 递归扫描；
  - 跳过隐藏路径（以 `.` 开头的目录/文件）；
  - 为每个 PDF 构造对应的输出 `.md` 路径与 `PdfTask`；
- `get_pdf_page_count(pdf_path)`：使用 `pypdf.PdfReader` 获取页数；
- `render_page_to_png_bytes(pdf_path, page_number)`：
  - 使用 PyMuPDF（`fitz`）打开 PDF；
  - 渲染指定页为 PNG 二进制数据，用于后续 base64 编码传给 OCR 模型。

> 当前版本统一走图片 OCR，尚未实现“检测文本层并直接提取”的逻辑，可在后续扩展。

### 5.3 OCR 客户端（`ocr/client.py` / `ocr/prompts.py`）

- `OcrClient`：基于 `httpx.AsyncClient` 的上下文管理器，负责与 `llama-server` 交互；
- `ocr_page(image_bytes, page_number, prompt)`：
  - 将 PNG bytes 做 base64 编码，构造 `image_url: data:image/png;base64,...`；
  - 按 OpenAI Chat 格式构造 `messages`：`[{role: "user", content: [text, image_url]}]`；
  - 调用 `/v1/chat/completions`，解析返回的 `choices[0].message.content` 作为 OCR 结果；
  - 针对：
    - 400 且包含 `context` / `exceeds` 文本：视为上下文超限，标记该页失败；
    - 5xx / 网络错误 / 超时：按照 `max_retries` 做重试，指数退避；
- `prompts.py`：
  - 定义 `PROMPTS = {"default": ...}`；
  - `get_prompt(preset)` 根据名称返回对应 prompt，可在此扩展不同场景模板。

### 5.4 Markdown 生成（`markdown/writer.py` / `markdown/postprocess.py`）

- `build_markdown(pdf_task, page_results)`：
  - 顶部插入 `# <原 PDF 文件名>`；
  - 每一页插入：
    - `## Page N` 作为标题；
    - 页文本（若 OCR 成功），或
    - `> [OCR FAILED] Page N` + 错误信息占位；
  - 文末追加 `## OCR 失败页列表` 汇总所有失败页面；
- `postprocess_markdown(md)`：
  - 合并多余空行；
  - 去除首尾空白，并确保末尾有换行。

### 5.5 异步编排（`orchestrator.py`）

- `run(config)`：
  - 使用 `scan_pdfs` 获取 `PdfTask` 列表；
  - 创建 `asyncio.Semaphore(max_concurrency)` 控制并发；
  - 在 `async with OcrClient(config)` 中，为每个 PDF 创建异步任务：
    - 获取页数；
    - 逐页渲染 + OCR；
    - 收集 `PageOcrResult`；
    - 生成 Markdown 并写入磁盘；
  - 汇总所有 `FileConvertResult`，计算并返回整体统计信息。

CLI 入口脚本 `convert_pdfs_to_md.py` 中：

- 使用 `argparse` 解析命令行参数，
- 调用 `build_config_from_args` 构建 `AppConfig`，
- 初始化日志，
- 使用 `asyncio.run()` 调用 `orchestrator.run` 执行完整流程。

---

## 6. 常见问题（FAQ）

### Q1. 运行时提示找不到依赖 / `ImportError`

请确认已在当前 Python 环境中执行：

```bash
pip install -r requirements.txt
```

以及当前执行脚本的目录为项目根目录（包含 `convert_pdfs_to_md.py`）。

### Q2. OCR 调用失败，日志中出现 5xx 或网络超时

- 检查 `llama-server` 是否已经正常启动；
- 确认 `--server-url` 地址与端口正确无误；
- 可适当调小 `--max-concurrency` 避免压垮服务；
- 可调大 `--request-timeout` 以容纳慢请求。

### Q3. 日志里显示 `the request exceeds the available context size`

说明单次请求已超出模型上下文长度限制：

- 当前实现中单次只处理一个页面，理论上较难触发；
- 若仍然触发，多半是某页内容异常复杂，可以先忽略该页结果（脚本会标记为失败页）。

### Q4. 如何只测试少量 PDF？

- 建议在一个小目录下放少量 PDF（包含 1~2 页的小文件），
- 使用该目录作为 `--input-dir`，先验证流程与输出格式，再批量处理大目录。

---

## 7. 开发与扩展建议

如果你计划进一步扩展本项目，可以考虑以下方向：

- **文本层检测与直抽**：
  - 在 `pdf/renderer.py` 或 `loader.py` 中加入对 PDF 文本层的检测，
  - 对纯文本 PDF 直接抽取文本而不是渲染为图片后 OCR，提高性能与精度。

- **页级并发**：
  - 目前同一 PDF 内部按页串行处理，
  - 可以在单个 PDF 内部再引入小范围并发（注意与全局信号量配合，避免过载）。

- **多种 prompt 模板**：
  - 在 `ocr/prompts.py` 中扩展不同场景（表格、代码、试卷等）的模板，
  - 新增命令行参数或根据文件路径/名称自动选择模板。

- **测试用例**：
  - 为 `scanner`、`renderer`、`ocr.client`、`markdown.writer` 等模块添加单元测试，
  - 使用本地小样本 PDF 做集成测试，确保调整后仍能稳定运行。

---

## 8. 设计文档

本仓库中还包含两份用于约束与说明实现的文档：

- `目录批量 PDF → Markdown 转换工具.md`：需求文档；
- `目录批量 PDF → Markdown 转换工具-项目结构与模块设计.md`：项目结构与模块设计说明。

如果你需要了解更详细的需求背景、边界与扩展规划，可以直接阅读上述文档，再结合当前 `README` 与源码理解整体实现。
