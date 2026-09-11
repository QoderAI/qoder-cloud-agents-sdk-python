# Qoder Cloud Agents Python SDK

Python 3.10+，同步与原生异步客户端，支持类型化响应、自动分页、SSE 和文件传输。

完整 API 参考：[Forward API](docs/forward-api.md) · [Managed API](docs/managed-api.md)，包含初始化、同步/异步调用、分页、SSE、文件传输，以及全部资源方法的参数、返回类型与 HTTP 路由。

## 安装与配置

```bash
# 在本仓库中安装
python -m pip install .
# 开发环境
python -m pip install -e '.[dev]'
```

```python
from qca import Forward, Managed

with Forward() as client:
    for model in client.models.list().data:
        if model.is_enabled:
            print(model.id)

with Managed() as client:
    for agent in client.agents.list(limit=20):
        print(agent.id, agent.name)
```

也可使用 `from qca.forward import Client` 或 `from qca.managed import Client`。两种模式独立实例化，使用各自的资源与类型。

| 配置 | Forward | Managed |
|---|---|---|
| 令牌 | `QODER_ACCESS_TOKEN` | `QODER_ACCESS_TOKEN` |
| API 根地址 | `QODER_FORWARD_BASE_URL` | `QODER_BASE_URL` |
| 默认地址 | `https://api.qoder.com/api/v1/forward/` | `https://api.qoder.com/api/v1/cloud/` |

显式参数优先于环境变量。客户端不读取 `.env`；只有 examples 读取 `.env.live`。CN 环境需要显式配置对应根地址：

```python
client = Forward(
    access_token="your-access-token",
    base_url="https://api.qoder.com.cn/api/v1/forward",
    timeout=30.0,
    max_retries=2,
)
```

## 会话

Forward 通过 Identity 和 Template 创建 Session，Managed 通过 Agent 和 Environment 创建 Session：

```python
from qca import Forward

with Forward() as client:
    environment = client.environments.create(name="demo", config={"type": "cloud"})
    identity = client.identities.create(external_id="example-user", name="示例用户")
    template = client.templates.create(
        name="assistant", environment_id=environment.id,
        model="ultimate",  # 使用当前账号已启用的模型
        system="根据可读取的资料回答问题。",
        tools=[{"type": "agent_toolset_20260401"}],
    )
    session = client.sessions.create(identity_id=identity.id, template_id=template.id)
    print(session.id)
```

```python
from qca import Managed

with Managed() as client:
    environment = client.environments.create(name="demo", config={"type": "cloud"})
    agent = client.agents.create(
        name="assistant", model={"id": "ultimate"},
        system="根据可读取的资料回答问题。",
        tools=[{"type": "agent_toolset_20260401"}],
    )
    session = client.sessions.create(environment_id=environment.id, agent=agent.id)
    print(session.id)
```

片段会创建资源。包含执行断言和清理的完整用例见 [examples](examples/README.md)。Forward 还提供 Schedule、Batch、Channel；Managed 提供 Deployment、Dream、自托管环境 Work API。

## 消息与 SSE

下列代码适用于两种客户端。在同一段对话中复用 `session_id`，同一条逻辑消息的 HTTP 重试复用幂等键。

```python
from uuid import uuid4

sent = client.sessions.events.send(
    session_id,
    events=[{"type": "user.message", "content": [{"type": "text", "text": "你好"}]}],
    extra_headers={"Idempotency-Key": uuid4().hex},
)

with client.sessions.events.stream(
    session_id,
    extra_headers={"Last-Event-ID": sent.data[0].id},
    event_deltas=["agent.message"],
) as stream:
    for event in stream:
        if event.type == "agent.message":
            print(event.to_json())
        elif event.type == "session.status_idle":
            print(event.stop_reason)
            break
        elif event.type in ("session.error", "session.status_terminated"):
            raise RuntimeError(f"Session stopped: {event.type}")
```

SDK 不自动重连 SSE。保存 `stream.last_event_id`，重连时通过 `Last-Event-ID` 恢复，不要重发已被接收的消息。`event_start`、`event_delta` 是预览，最终事件会再次包含完整内容；同一个 ID 的增量事件不会被去重。idle 可能表示等待确认或达到预算，业务成功还需检查 `stop_reason` 和最终回复。

## 异步

异步客户端使用 `httpx.AsyncClient`，请求、重试等待、SSE 读取均为原生异步 I/O。

```python
import asyncio
from qca import AsyncManaged

async def main():
    async with AsyncManaged() as client:
        async for agent in client.agents.list(limit=20):
            print(agent.id)
        first_page = await client.sessions.list(limit=10)
        print(first_page.data)

asyncio.run(main())
```

异步流使用 `async with await client.sessions.events.stream(...)`。完整片段见 [Forward 异步示例](examples/forward/async_session.py)和 [Managed 异步示例](examples/managed/async_session.py)。本地文件读取通过线程执行，网络请求直接使用异步 HTTP 客户端。

## 参数与响应

方法使用 snake_case、关键字参数和类型注解。嵌套资源的目标 ID 可以作为位置参数，祖先 ID 必须具名：

```python
credential = client.vaults.credentials.retrieve("credential-id", vault_id="vault-id")
memory = client.memory_stores.memories.retrieve("memory-id", memory_store_id="store-id")
```

各 mode 的 `types/*_params.py` 使用 `TypedDict` 定义请求。嵌套参数直接传普通字典；联合类型直接传对应的字符串、字典或列表。响应是 Pydantic 模型，可以直接访问字段，未知字段也会保留。

```python
from qca import NOT_GIVEN

client.identities.update("identity-id", name=NOT_GIVEN)  # 不发送 name
client.identities.update("identity-id", name=None)       # 发送 null
client.identities.update("identity-id", enabled=False)   # 保留 false

identity = client.identities.retrieve("identity-id")
print(identity.to_dict())
print(identity.to_json())
print(identity._request_id)
print("name" in identity.model_fields_set)  # 区分缺失与 null
```

能否清空字段由服务端决定。方法均支持 `extra_headers`、`extra_query`、`extra_body`、`timeout`；extra 值优先于方法参数。空数组、空对象、0、false 均保留。

## 分页

```python
page = client.sessions.list(limit=20)
print(page.data)                  # 当前页
for session in page:              # 自动获取后续页
    print(session.id)
for page in client.sessions.list().iter_pages():
    print(len(page.data))
```

SDK 按 Go API 区分 `after_id` / `before_id` 与 `next_page` 分页，后续请求保留过滤条件。游标不前进或循环时抛出异常。非分页列表响应（例如 Models）通过 `.data` 访问。

## 错误、超时与重试

```python
from qca import APIConnectionError, APIStatusError, APITimeoutError

try:
    session = client.sessions.retrieve("sess-id", timeout=10)
except APITimeoutError:
    print("请求超时")
except APIConnectionError:
    print("网络连接失败")
except APIStatusError as exc:
    print(exc.status_code, exc.code, exc.type, exc.request_id)
```

HTTP 状态分别对应 `BadRequestError`、`AuthenticationError`、`PermissionDeniedError`、`NotFoundError`、`ConflictError`、`UnprocessableEntityError`、`RateLimitError`、`InternalServerError`。非 JSON 错误正文保留在 `.body`。响应无法解码为声明类型时抛出 `APIResponseValidationError`。

默认连接超时 10 秒，其余 HTTP 阶段 60 秒。可传浮点秒数、`httpx.Timeout`、`None`；超时按 HTTP 阶段和单次尝试计算。端到端任务期限由调用方管理，异步代码可用 `asyncio.wait_for`。

默认最多重试 2 次：GET/HEAD 或携带 `Idempotency-Key` 的请求可对连接错误、408、429、5xx 重试；无幂等键的其他请求仅对 429 重试；409 不自动重试。在上述约束内遵循 `x-should-retry` 和有效的 `Retry-After-Ms` / `Retry-After`，否则指数退避。已建立的 SSE 不重试。

`client.with_options(max_retries=0, timeout=20)` 返回独立配置的客户端，复用同一个 HTTP 连接池；关闭任一客户端会关闭这个池。

## 文件和自定义 HTTP

```python
from pathlib import Path

file = client.files.upload(file=Path("report.txt"))
skill = client.skills.create(files=[("example/SKILL.md", b"---\nname: example\n---\nExample skill")])
with client.files.download(file.id) as content:
    content.write_to_file("downloaded.txt")
```

上传支持 bytes、二进制文件对象、Path、`(文件名, 内容[, MIME 类型])`。调用方传入的文件对象由调用方关闭；上传内容会缓存以便重试。metadata 使用 JSON 编码，Skill 相对路径保留在 multipart 文件名中。

Files 下载先获取临时链接，再流式读取存储地址；API 认证、默认请求头、Cookie 不会发送到存储主机。Skill Version 下载直接返回 API 的二进制响应。异步下载使用 `await client.files.download(...)`、`await response.write_to_file(...)`。

```python
import httpx
from qca import Forward

with Forward(http_client=httpx.Client(proxy="http://localhost:8080")) as client:
    raw = client.models.with_raw_response.list()
    print(raw.status_code, raw.headers)
    models = raw.parse()
```

异步客户端可传 `httpx.AsyncClient`，异步 raw response 使用 `await raw.parse()`。动态令牌提供者传到 `credential=`，每次 HTTP 尝试调用 `get_token()`；异步客户端也接受异步 `get_token()`。静态 access_token 优先于提供者，显式 Authorization 请求头优先于两者。

需要先查看响应头再读取正文时使用 `with_streaming_response`。退出上下文时关闭连接：

```python
with client.models.with_streaming_response.list() as response:
    print(response.headers)
    models = response.parse()
```

异步版本使用 `async with client.models.with_streaming_response.list()`，通过 `await response.parse()` 解析正文；也可以按块迭代 `iter_bytes()` / `iter_lines()`。

## 目录

```text
src/qca/
  __init__.py
  common/                 # HTTP、鉴权、错误、分页、上传/下载、SSE
  forward/
    _client.py
    resources/            # identities/configs、sessions/events 等
    types/                # 请求 TypedDict、响应模型
  managed/
    _client.py
    resources/            # agents、deployments、environments/work 等
    types/
tests/                    # 资源面、文档契约、公共层与模拟执行场景
examples/                 # 每个场景一个文件；各 mode 含 6 个同步场景、异步片段及 live 测试
docs/                     # Forward / Managed 完整 API 参考
```

## 许可证

本项目基于 [MIT License](LICENSE) 开源。
