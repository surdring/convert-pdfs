# vllm-gfx906 在 AMD gfx906(ROCm) 上部署 PaddleOCR-VL-1.5（整理版）

本文整理了在 AMD ROCm（gfx906）环境下，使用 `nalanzeyu/vllm-gfx906` 容器部署 `PaddleOCR-VL-1.5` 的常用命令、关键参数与排障要点。

## 1. 目标与基本结论

- **目标**：在 AMD GPU（gfx906）上用 vLLM 启动 PaddleOCR-VL-1.5 的 OpenAI 兼容服务（`/v1/chat/completions`）。
- **结论**：
  - `nlzy/vllm-gfx906`/`nalanzeyu/vllm-gfx906` 是面向 gfx906 的定制版 vLLM 环境，能够在该类显卡上尝试部署。
  - 真实落地的主要难点通常不是模型格式，而是 **ROCm 多卡/显存与端口/网络配置**。

## 2. 容器启动（Docker run）

### 2.1 推荐：host 网络模式

使用 `--network=host` 的好处：
- 容器内服务端口直接暴露到宿主机同端口，便于本机调用。

注意：
- **host 网络模式下 `-p 8011:8011` 之类端口映射会被忽略**（Docker 会提示 *Published ports are discarded when using host network mode*），这是正常的。

### 2.2 单卡容器（示例）

```bash
sudo docker run -itd \
  --name vllm-gfx906 \
  --restart=unless-stopped \
  --network=host \
  --ipc=host \
  --shm-size=32g \
  --device=/dev/kfd \
  --device=/dev/dri \
  --group-add video \
  -e HIP_VISIBLE_DEVICES=0 \
  -e ROCR_VISIBLE_DEVICES=0 \
  -e HSA_OVERRIDE_GFX_VERSION=9.0.6 \
  -e HCC_AMDGPU_TARGET=gfx906 \
  -v /home/zhengxueen/model:/model \
  -v /home/zhengxueen/workspace/localworkspace:/workspace \
  -v /home/zhengxueen/vllm-root:/root \
  nalanzeyu/vllm-gfx906
```

### 2.3 双卡可见（注意：不等于 vLLM 自动双卡并行）

```bash
sudo docker run -itd \
  --name vllm-gfx906 \
  --restart=unless-stopped \
  --network=host \
  --ipc=host \
  --shm-size=32g \
  --device=/dev/kfd \
  --device=/dev/dri \
  --group-add video \
  -e HIP_VISIBLE_DEVICES=0,1 \
  -e ROCR_VISIBLE_DEVICES=0,1 \
  -e HSA_OVERRIDE_GFX_VERSION=9.0.6 \
  -e HCC_AMDGPU_TARGET=gfx906 \
  -v /home/zhengxueen/model:/model \
  -v /home/zhengxueen/workspace/localworkspace:/workspace \
  -v /home/zhengxueen/vllm-root:/root \
  nalanzeyu/vllm-gfx906
```

#### 常见报错：`--group-add render` 失败

如果你加了 `--group-add render` 并报错：

> Unable to find group render: no matching entries in group file

原因：宿主机不存在 `render` 用户组。

解决：
- **推荐**：直接删掉 `--group-add render`（通常 `video` 就够用）。
- 或者：在宿主机创建该组（需要 root 权限），再重新运行。

## 3. `--shm-size=32g` 是否需要？

- `--shm-size` 是容器 **共享内存**（/dev/shm）大小，主要影响 CPU 侧的进程间共享内存与部分数据管线，不等同于 GPU 显存。
- 在多进程/大批量推理、图像处理等场景中，增大 `shm-size` 通常更稳。
- **与“显存 16GB/32GB”没有直接对应关系**；`--shm-size=32g` 一般可用。

## 4. 容器内启动 vLLM 服务

进入容器：

```bash
sudo docker exec -it vllm-gfx906 bash
```

### 4.1 只用 GPU1（例如 GPU1 有 32GB 时推荐）

```bash
export HIP_VISIBLE_DEVICES=1
export ROCR_VISIBLE_DEVICES=1

MODEL_DIR="/model/PaddleOCR-VL-1.5"

vllm serve "$MODEL_DIR" \
  --served-model-name "PaddleOCR-VL-1.5" \
  --host 0.0.0.0 \
  --port 8011 \
  --trust-remote-code \
  --dtype float16 \
  --max-num-batched-tokens 8192 \
  --no-enable-prefix-caching \
  --mm-processor-cache-gb 0
```

### 4.2 显存不足时的关键参数：`--gpu-memory-utilization`

如果启动时报错类似：

> ValueError: Free memory on device (3.27/15.98 GiB) on startup is less than desired GPU memory utilization (0.9, 14.39 GiB)

含义：
- vLLM 会按 `gpu_memory_utilization`（默认 0.9）预留显存。
- 如果显卡已被其它进程占用，导致“启动时可用显存”不足，就会直接失败。

解决方式：
- **释放显存**（停掉其它占用 GPU 的进程/服务）。
- 或者降低 vLLM 的显存预留比例，例如：

```bash
vllm serve "$MODEL_DIR" \
  --served-model-name "PaddleOCR-VL-1.5" \
  --host 0.0.0.0 \
  --port 8011 \
  --trust-remote-code \
  --dtype float16 \
  --gpu-memory-utilization 0.75 \
  --max-num-batched-tokens 8192 \
  --no-enable-prefix-caching \
  --mm-processor-cache-gb 0
```

如果仍不足，可继续下调：`0.6` / `0.5`。

### 4.3 端口占用：`Address already in use`

- 说明宿主机（host 网络）上该端口已被占用。
- 解决：换端口，例如 `--port 8012`，或停掉占用端口的服务。

## 5. 是否能“同时用两张卡并行”？

需要区分两件事：

### 5.1 让容器“看到两张卡”

这只是：

```bash
export HIP_VISIBLE_DEVICES=0,1
export ROCR_VISIBLE_DEVICES=0,1
```

但这 **不等于 vLLM 自动双卡并行**。

### 5.2 让 vLLM 真正多卡并行（Tensor Parallel）

通常需要开启张量并行：

```bash
export HIP_VISIBLE_DEVICES=0,1
export ROCR_VISIBLE_DEVICES=0,1

MODEL_DIR="/model/PaddleOCR-VL-1.5"

vllm serve "$MODEL_DIR" \
  --served-model-name "PaddleOCR-VL-1.5" \
  --host 0.0.0.0 \
  --port 8011 \
  --trust-remote-code \
  --dtype float16 \
  --tensor-parallel-size 2 \
  --max-num-batched-tokens 8192 \
  --no-enable-prefix-caching \
  --mm-processor-cache-gb 0
```

注意事项：
- 多卡会引入通信开销（ROCm/RCCL）。在低并发/小 batch 场景下，吞吐未必更高。
- 如果两张卡显存差异很大（例如 16GB + 32GB），张量并行通常会被较小显存的那张卡限制。
- 若启动时报通信/多进程错误，建议先回退到“单卡（32GB 的那张）”跑通再说。

## 6. 服务可用性验证

因为用了 `--network=host`，所以在宿主机上可以直接访问容器服务：

### 6.1 检查模型列表

```bash
curl http://127.0.0.1:8011/v1/models
```

### 6.2 发起一个最小 chat 请求（纯文本，先确认服务正常）

```bash
curl http://127.0.0.1:8011/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "PaddleOCR-VL-1.5",
    "messages": [
      {"role": "user", "content": [{"type": "text", "text": "Hello"}]}
    ],
    "stream": false
  }'
```

如果需要多模态（图像 + 文本），请求体需要包含 `image_url`（可以是 data URL 的 base64）。

## 7. 与本项目（convert-pdfs）对接提示

- 本项目 OCR 客户端请求的是 OpenAI 兼容接口：`POST /v1/chat/completions`。
- `config.toml` 里通常需要配置：
  - `server_url = "http://<宿主机IP>:8011"`（host 网络时也可以 `http://127.0.0.1:8011`，视调用端位置而定）
  - `model = "PaddleOCR-VL-1.5"`
- 若出现超时，优先调大客户端 `request_timeout`（以及 connect/read/write/pool），并确保客户端不走代理（例如 httpx 设置 `trust_env=False`）。

## 8. 常用排障清单

- **端口**：host 网络下确保端口未被占用（`Address already in use` 直接换端口最快）。
- **显存**：遇到 `Free memory on device ... less than desired`：
  - 释放占用显存的进程
  - 或降低 `--gpu-memory-utilization`
  - 必要时先用显存更大的 GPU 单卡跑通
- **容器权限**：`/dev/kfd`、`/dev/dri` 映射正常；一般 `--group-add video` 足够。
- **多卡并行**：需要 `--tensor-parallel-size 2`；仅设置 `HIP_VISIBLE_DEVICES=0,1` 不会自动并行。
