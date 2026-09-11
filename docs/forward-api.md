# Forward API 参考

本文覆盖当前 Python SDK 的 **110 个 Forward HTTP 操作**，同步与异步客户端均支持相同资源树。方法与路由依据当前 [资源源码](../src/qca/forward/resources/) 核对。另一种模式见 [Managed API](managed-api.md)。

## 安装、初始化与鉴权

在仓库根目录执行 `python -m pip install .`，要求 Python 3.10+。将账号令牌放入 `QODER_ACCESS_TOKEN`；SDK 不读取 `.env` 文件。

```python
from qca import Forward, AsyncForward

with Forward() as client:
    for model in client.models.list().data:
        if model.is_enabled:
            print(model.id)
```

也可从 `qca.forward` 导入 `Client` / `AsyncClient`。同步客户端使用 `with` 或 `close()`；异步客户端使用 `async with` 或 `await close()`。构造参数由 [公共客户端](../src/qca/common/_base_client.py) 实现，默认地址由 [Forward 客户端](../src/qca/forward/_client.py) 定义。

| 参数 | 类型和默认行为 |
|---|---|
| `access_token` | `str \| None`；显式值优先，否则读取 `QODER_ACCESS_TOKEN`，作为 Bearer 令牌发送。 |
| `base_url` | `str \| httpx.URL \| None`；显式值优先，否则读取 `QODER_FORWARD_BASE_URL`，默认 `https://api.qoder.com/api/v1/forward/`。中国站可设为 `https://api.qoder.com.cn/api/v1/forward/`。 |
| `timeout` | `float \| httpx.Timeout \| None`；单位秒，默认连接阶段 10 秒、其他 HTTP 阶段 60 秒。`None` 关闭 HTTP 超时。 |
| `max_retries` | 非负整数，默认 `2`。 |
| `default_headers` / `default_query` | 分别为 `Mapping[str, str]` / `Mapping[str, Any]`，设定默认请求头和查询参数。 |
| `http_client` | 同步传 `httpx.Client`，异步传 `httpx.AsyncClient`，可配置代理或测试用 transport。 |
| `credential` | [Credential / AsyncCredential](../src/qca/common/credentials.py)；每次 HTTP 尝试调用 `get_token()`。静态令牌优先，显式 `Authorization` 请求头优先级最高。 |

`client.with_options(timeout=20, max_retries=0)` 返回配置独立的客户端，但共享 HTTP 连接池；关闭其中任意客户端会关闭该池。

## 创建会话并读取 SSE

下面片段从当前账号选择已启用模型，再创建会话并发送一条消息。片段会创建资源；包含断言、失败处理与清理的完整实现见 [Forward 场景示例](../examples/forward/)。生产代码应复用同一会话 ID，并在不再需要时清理本次创建的资源。

```python
from uuid import uuid4
from qca import Forward

with Forward() as client:
    model_id = next(model.id for model in client.models.list().data if model.is_enabled)
    environment = client.environments.create(name="docs-example", config={"type": "cloud"})
    identity = client.identities.create(external_id=f"docs-example-{uuid4().hex}", name="文档示例")
    template = client.templates.create(
        name="docs-assistant", environment_id=environment.id, model=model_id,
        system="根据可读取的资料回答问题。",
        tools=[{"type": "agent_toolset_20260401"}],
    )
    session = client.sessions.create(identity_id=identity.id, template_id=template.id)
    sent = client.sessions.events.send(
        session.id,
        events=[{"type": "user.message", "content": [{"type": "text", "text": "你好"}]}],
        extra_headers={"Idempotency-Key": uuid4().hex},
    )
    with client.sessions.events.stream(
        session.id,
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
                raise RuntimeError(event.type)
```

[Stream / AsyncStream](../src/qca/common/_streaming.py) 按 SSE 事件解码，维护 `last_event_id`。SDK 不自动重连；重连时传 `extra_headers={"Last-Event-ID": saved_id}`，不要重发已接收的消息。`event_start` / `event_delta` 是增量预览，最终事件可能再次包含完整内容；相同 ID 的增量事件不会去重。`session.status_idle` 也可能表示等待确认或达到预算，业务成功应结合 `stop_reason` 和最终回复判断。Session Thread 的流采用相同处理方式。

## 异步与分页

异步普通方法加 `await`，参数与同步方法一致。分页方法返回 [AsyncPaginator](../src/qca/common/pagination.py)，可以直接 `async for`，或者 `await` 得到第一页 `AsyncPage`。`models.list()` 是普通列表响应，通过 `.data` 访问。

```python
import asyncio
from qca import AsyncForward

async def main():
    async with AsyncForward() as client:
        async for session in client.sessions.list(limit=20):
            print(session.id)
        page = await client.sessions.list(limit=10)
        print(page.data)

asyncio.run(main())
```

异步 SSE 使用 `async with await client.sessions.events.stream(session_id) as stream:`，内部用 `async for event in stream:`。异步二进制下载使用 `async with await client.files.download(file_id) as response:`，通过 `await response.write_to_file(path)` 保存。

同步分页返回 [SyncPage](../src/qca/common/pagination.py)：

```python
with Forward() as client:
    page = client.sessions.list(limit=20)
    print(page.data)                          # 当前页
    for session in page:                     # 自动获取全部后续页
        print(session.id)
    for page in client.sessions.list().iter_pages():
        print(page.has_more, len(page.data))
```

分页会保留过滤条件，按接口使用 `after_id` / `before_id`、`page` 或 `page_token`；不要将这些游标混用。页对象提供 `has_next_page()`、`get_next_page()`，异步 `get_next_page()` 需要 `await`。游标不前进或循环时抛出 `RuntimeError`，防止无限请求。

## 请求参数与响应

下文签名列出所有业务参数及其真实类型，省略各方法共有的四个关键字参数。签名中的 `*` 表示后续参数必须具名；多层资源的目标 ID 可作位置参数，祖先 ID 必须具名，例如 `client.vaults.credentials.retrieve("credential-id", vault_id="vault-id")`。

| 公共请求参数 | 类型 / 默认值 | 行为 |
|---|---|---|
| `extra_headers` | `Dict[str, str] \| None = None` | 追加或覆盖请求头，适合幂等键、SSE 恢复游标。 |
| `extra_query` | `Dict[str, Any] \| None = None` | 追加或覆盖查询字段。 |
| `extra_body` | `Dict[str, Any] \| None = None` | 追加或覆盖请求正文字段。 |
| `timeout` | `float \| httpx.Timeout \| None \| NotGiven = NOT_GIVEN` | 覆盖单次请求超时；省略时继承客户端配置。 |

`NOT_GIVEN` 从 `qca` 导入，表示不发送该字段；`None` 会发送显式 null。`False`、`0`、空字符串/数组/对象均保留。接口是否允许 null 由服务端决定。时间参数接受 `datetime`。请求嵌套对象使用普通字典，完整字段定义见每个操作下方的 `TypedDict` 与嵌套类型链接；不需要实例化请求类。

响应模型由 [BaseModel](../src/qca/common/_models.py) 实现，支持字段属性、`to_dict()`、`to_json()`、`_request_id`，未知字段会保留。使用 `model_fields_set` 区分缺失字段与 null。返回类型中的 `SyncPage[T]` 表示分页，`Stream[T]` 表示 SSE；返回 `None` 表示没有声明的响应实体。

每个资源均提供 `with_raw_response` 和 `with_streaming_response`，方法和参数与普通资源相同：

```python
with Forward() as client:
    raw = client.models.with_raw_response.list()
    print(raw.status_code, raw.headers)
    models = raw.parse()
    with client.models.with_streaming_response.list() as response:
        print(response.headers)
        models = response.parse()
```

[APIResponse](../src/qca/common/_response.py) 的异步版本通过 `await raw.parse()` 解析，流式包装使用 `async with client.models.with_streaming_response.list()`。二进制响应提供 `read()`、`iter_bytes()`、`write_to_file()` 和 `close()`；异步版本使用对应的 await/async for。

## 文件与 Skill

[FileTypes](../src/qca/common/_types.py) 支持 `bytes`、二进制文件对象、`Path` 以及 `(文件名, 内容[, MIME 类型[, 文件头]])`。SDK 缓存上传内容用于重试，调用方传入的文件对象由调用方关闭。Skill 文件相对路径保留在 multipart 文件名中。

```python
from pathlib import Path
from qca import Forward

with Forward() as client:
    uploaded = client.files.upload(file=Path("report.txt"), purpose="session_resource")
    with client.files.download(uploaded.id) as response:
        response.write_to_file("downloaded-report.txt")
    skill = client.skills.create(files=[
        ("example/SKILL.md", b"---\nname: example\ndescription: Example documentation skill\n---\nExample skill")
    ])
```

Files 下载先获取临时地址再读取内容，API 的认证、默认请求头和 Cookie 不会转发给存储主机。Skill Version 下载直接读取 API 二进制响应。具体请求字段以以下方法签名为准。

## 错误、重试与超时

```python
from qca import APIConnectionError, APIStatusError, APITimeoutError

try:
    with Forward() as client:
        client.sessions.retrieve("session-id", timeout=10)
except APITimeoutError:
    print("请求超时")
except APIConnectionError:
    print("连接失败")
except APIStatusError as exc:
    print(exc.status_code, exc.code, exc.type, exc.request_id)
```

[异常类型](../src/qca/common/_exceptions.py) 包括 `BadRequestError`（400）、`AuthenticationError`（401）、`PermissionDeniedError`（403）、`NotFoundError`（404）、`ConflictError`（409）、`UnprocessableEntityError`（422）、`RateLimitError`（429）、`InternalServerError`（5xx）。`APIStatusError.body` 保留服务端错误正文，返回实体无法解析时抛出 `APIResponseValidationError`。

默认最多重试两次：GET/HEAD 或携带 `Idempotency-Key` 的请求可对连接错误、408、429、5xx 重试；其他请求仅对 429 重试，409 不自动重试。在上述幂等性限制内遵循 `x-should-retry` 和有效 `Retry-After-Ms` / `Retry-After`，否则指数退避。已建立的 SSE 不重试。同一逻辑写入的 HTTP 重试必须复用同一个幂等键。

HTTP 超时按阶段、按尝试计算，不是整个 Agent 任务期限；轮询或流式业务应由调用方控制总期限，异步可使用 `asyncio.wait_for`。真实场景运行方法见 [examples](../examples/README.md)。

## 资源与操作索引

| 资源 | 操作数 | 用途 |
|---|---:|---|
| [batches](#batches) | 7 | 提交 JSONL 批处理输入，查询任务状态、逐项结果及输出/错误文件的临时链接。取消请求后仍需查询最终状态。 |
| [channels](#channels) | 7 | 配置通信渠道、绑定与状态；渠道消息涉及实际外部渠道，应由应用按业务授权发送。 |
| [channel_pairings](#channel_pairings) | 2 | 创建和查询渠道配对，完成配对后可用于渠道身份绑定。 |
| [environments](#environments) | 6 | 管理运行环境。Managed 的 work 子资源还用于自托管执行器轮询任务、确认、心跳和上报结果。 |
| [files](#files) | 5 | 上传和管理文件元数据，按 ID 下载内容。upload 使用 multipart，download 返回需关闭的二进制响应。 |
| [identities](#identities) | 18 | 按外部用户标识管理身份、启用状态和关联记忆；身份配置可以覆盖指定 Template 的设置。 |
| [memory_stores](#memory_stores) | 14 | 管理记忆存储、记忆正文与历史版本；Memory Store 通过会话资源挂载后可供助手访问。 |
| [models](#models) | 1 | 获取当前账号的模型列表与启用状态，创建 Agent 或 Template 前可从中选择可用模型。 |
| [schedules](#schedules) | 9 | 创建并管理定时任务，支持暂停、恢复和手动触发。执行记录位于 schedule_runs。 |
| [schedule_runs](#schedule_runs) | 2 | 读取定时任务的执行记录及关联会话，检查执行状态与最终结果。 |
| [sessions](#sessions) | 15 | 创建、查询和管理会话。events 发送输入并读取历史或 SSE；threads 访问子线程，resources 管理挂载资源。 |
| [skills](#skills) | 10 | 上传 Skill 文件并管理版本；版本下载返回二进制响应。Skill 路径会保留在 multipart 文件名中。 |
| [templates](#templates) | 6 | 管理可复用的模型、工具与环境配置；Identity 使用 Template 创建会话，可克隆或归档模板。 |
| [vaults](#vaults) | 8 | 管理凭据仓库及仓库中的凭据。参数中可能包含令牌或密钥，业务日志应避免打印请求正文。 |

## batches

提交 JSONL 批处理输入，查询任务状态、逐项结果及输出/错误文件的临时链接。取消请求后仍需查询最终状态。

### `batches.list`

`GET /batches`

```python
def list(
    *,
    status: Union[str, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
) -> SyncPage[Batch]: ...
```

调用：`client.batches.list(...)`。实现：[同步](../src/qca/forward/resources/batches/batches.py#L24) / [异步](../src/qca/forward/resources/batches/batches.py#L169)。异步返回 `AsyncPaginator[Batch]`。

查询：`status`、`limit`、`after_id`、`before_id`。

请求字段：[TypedDict](../src/qca/forward/types/batch_list_params.py)。类型定义：[Batch](../src/qca/forward/types/batch.py)、[NotGiven](../src/qca/common/_types.py)、[SyncPage](../src/qca/common/pagination.py)。

分页协议：`Page`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

### `batches.create`

`POST /batches`

```python
def create(
    *,
    input_file_id: str,
    completion_window: str,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
) -> Batch: ...
```

调用：`client.batches.create(...)`。实现：[同步](../src/qca/forward/resources/batches/batches.py#L49) / [异步](../src/qca/forward/resources/batches/batches.py#L196)。

正文：`input_file_id`、`completion_window`、`metadata`。

请求头：`idempotency_key` → `Idempotency-Key`。

请求字段：[TypedDict](../src/qca/forward/types/batch_create_params.py)。类型定义：[Batch](../src/qca/forward/types/batch.py)、[NotGiven](../src/qca/common/_types.py)。

### `batches.retrieve`

`GET /batches/{batch_id}`

```python
def retrieve(
    batch_id: str,
) -> Batch: ...
```

调用：`client.batches.retrieve(...)`。实现：[同步](../src/qca/forward/resources/batches/batches.py#L74) / [异步](../src/qca/forward/resources/batches/batches.py#L221)。

路径：`batch_id`。

类型定义：[Batch](../src/qca/forward/types/batch.py)。

### `batches.cancel`

`POST /batches/{batch_id}/cancel`

```python
def cancel(
    batch_id: str,
    *,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
) -> Batch: ...
```

调用：`client.batches.cancel(...)`。实现：[同步](../src/qca/forward/resources/batches/batches.py#L96) / [异步](../src/qca/forward/resources/batches/batches.py#L243)。

路径：`batch_id`。

请求头：`idempotency_key` → `Idempotency-Key`。

请求字段：[TypedDict](../src/qca/forward/types/batch_cancel_params.py)。类型定义：[Batch](../src/qca/forward/types/batch.py)、[NotGiven](../src/qca/common/_types.py)。

### `batches.retrieve_error`

`GET /batches/{batch_id}/error`

```python
def retrieve_error(
    batch_id: str,
) -> BatchFile: ...
```

调用：`client.batches.retrieve_error(...)`。实现：[同步](../src/qca/forward/resources/batches/batches.py#L119) / [异步](../src/qca/forward/resources/batches/batches.py#L266)。

路径：`batch_id`。

类型定义：[BatchFile](../src/qca/forward/types/batch_file.py)。

此方法返回临时下载地址及过期时间；它不会读取 JSONL 内容。

### `batches.retrieve_output`

`GET /batches/{batch_id}/output`

```python
def retrieve_output(
    batch_id: str,
) -> BatchFile: ...
```

调用：`client.batches.retrieve_output(...)`。实现：[同步](../src/qca/forward/resources/batches/batches.py#L141) / [异步](../src/qca/forward/resources/batches/batches.py#L288)。

路径：`batch_id`。

类型定义：[BatchFile](../src/qca/forward/types/batch_file.py)。

此方法返回临时下载地址及过期时间；它不会读取 JSONL 内容。

### `batches.tasks.list`

`GET /batches/{batch_id}/tasks`

```python
def list(
    batch_id: str,
    *,
    status: Union[str, None, NotGiven] = NOT_GIVEN,
    custom_id: Union[str, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
) -> SyncPage[BatchTask]: ...
```

调用：`client.batches.tasks.list(...)`。实现：[同步](../src/qca/forward/resources/batches/tasks.py#L17) / [异步](../src/qca/forward/resources/batches/tasks.py#L45)。异步返回 `AsyncPaginator[BatchTask]`。

路径：`batch_id`。

查询：`status`、`custom_id`、`limit`、`after_id`。

请求字段：[TypedDict](../src/qca/forward/types/batch_task_list_params.py)。类型定义：[BatchTask](../src/qca/forward/types/batch_task.py)、[NotGiven](../src/qca/common/_types.py)、[SyncPage](../src/qca/common/pagination.py)。

分页协议：`Page`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

## channels

配置通信渠道、绑定与状态；渠道消息涉及实际外部渠道，应由应用按业务授权发送。

### `channels.list`

`GET /channels`

```python
def list(
    *,
    channel_type: Union[str, None, NotGiven] = NOT_GIVEN,
    enabled: Union[bool, None, NotGiven] = NOT_GIVEN,
    binding_status: Union[str, None, NotGiven] = NOT_GIVEN,
    identity_id: Union[str, None, NotGiven] = NOT_GIVEN,
    template_id: Union[str, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
) -> SyncPage[Channel]: ...
```

调用：`client.channels.list(...)`。实现：[同步](../src/qca/forward/resources/channels/channels.py#L24) / [异步](../src/qca/forward/resources/channels/channels.py#L183)。异步返回 `AsyncPaginator[Channel]`。

查询：`channel_type`、`enabled`、`binding_status`、`identity_id`、`template_id`、`limit`、`after_id`、`before_id`。

请求字段：[TypedDict](../src/qca/forward/types/channel_list_params.py)。类型定义：[Channel](../src/qca/forward/types/channel.py)、[NotGiven](../src/qca/common/_types.py)、[SyncPage](../src/qca/common/pagination.py)。

分页协议：`Page`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

### `channels.create`

`POST /channels`

```python
def create(
    *,
    channel_type: str,
    identity_id: Union[str, None, NotGiven] = NOT_GIVEN,
    identity_resolution: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    template_id: Union[str, None, NotGiven] = NOT_GIVEN,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    enabled: Union[bool, None, NotGiven] = NOT_GIVEN,
    channel_config: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
) -> Channel: ...
```

调用：`client.channels.create(...)`。实现：[同步](../src/qca/forward/resources/channels/channels.py#L62) / [异步](../src/qca/forward/resources/channels/channels.py#L223)。

正文：`identity_id`、`identity_resolution`、`template_id`、`channel_type`、`name`、`enabled`、`channel_config`。

请求头：`idempotency_key` → `Idempotency-Key`。

请求字段：[TypedDict](../src/qca/forward/types/channel_create_params.py)。类型定义：[Channel](../src/qca/forward/types/channel.py)、[NotGiven](../src/qca/common/_types.py)。

### `channels.retrieve`

`GET /channels/{channel_id}`

```python
def retrieve(
    channel_id: str,
) -> Channel: ...
```

调用：`client.channels.retrieve(...)`。实现：[同步](../src/qca/forward/resources/channels/channels.py#L99) / [异步](../src/qca/forward/resources/channels/channels.py#L260)。

路径：`channel_id`。

类型定义：[Channel](../src/qca/forward/types/channel.py)。

### `channels.update`

`POST /channels/{channel_id}`

```python
def update(
    channel_id: str,
    *,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    identity_id: Union[str, None, NotGiven] = NOT_GIVEN,
    template_id: Union[str, None, NotGiven] = NOT_GIVEN,
    enabled: Union[bool, None, NotGiven] = NOT_GIVEN,
    channel_config: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
) -> Channel: ...
```

调用：`client.channels.update(...)`。实现：[同步](../src/qca/forward/resources/channels/channels.py#L121) / [异步](../src/qca/forward/resources/channels/channels.py#L282)。

路径：`channel_id`。

正文：`name`、`identity_id`、`template_id`、`enabled`、`channel_config`。

请求头：`idempotency_key` → `Idempotency-Key`。

请求字段：[TypedDict](../src/qca/forward/types/channel_update_params.py)。类型定义：[Channel](../src/qca/forward/types/channel.py)、[NotGiven](../src/qca/common/_types.py)。

### `channels.delete`

`DELETE /channels/{channel_id}`

```python
def delete(
    channel_id: str,
) -> DeletedChannel: ...
```

调用：`client.channels.delete(...)`。实现：[同步](../src/qca/forward/resources/channels/channels.py#L155) / [异步](../src/qca/forward/resources/channels/channels.py#L316)。

路径：`channel_id`。

类型定义：[DeletedChannel](../src/qca/forward/types/deleted_channel.py)。

### `channels.qr_sessions.create`

`POST /channels/{channel_id}/qr_sessions`

```python
def create(
    channel_id: str,
    *,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
) -> ChannelQRSession: ...
```

调用：`client.channels.qr_sessions.create(...)`。实现：[同步](../src/qca/forward/resources/channels/qr_sessions.py#L16) / [异步](../src/qca/forward/resources/channels/qr_sessions.py#L63)。

路径：`channel_id`。

请求头：`idempotency_key` → `Idempotency-Key`。

请求字段：[TypedDict](../src/qca/forward/types/channel_qr_session_create_params.py)。类型定义：[ChannelQRSession](../src/qca/forward/types/channel_qr_session.py)、[NotGiven](../src/qca/common/_types.py)。

### `channels.qr_sessions.retrieve`

`GET /qr_sessions/{session_key}`

```python
def retrieve(
    session_key: str,
) -> ChannelQRSession: ...
```

调用：`client.channels.qr_sessions.retrieve(...)`。实现：[同步](../src/qca/forward/resources/channels/qr_sessions.py#L39) / [异步](../src/qca/forward/resources/channels/qr_sessions.py#L86)。

路径：`session_key`。

类型定义：[ChannelQRSession](../src/qca/forward/types/channel_qr_session.py)。

## channel_pairings

创建和查询渠道配对，完成配对后可用于渠道身份绑定。

### `channel_pairings.create`

`POST /channel_pairings`

```python
def create(
    *,
    code: str,
    identity_id: str,
    template_id: str,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
) -> ChannelPairing: ...
```

调用：`client.channel_pairings.create(...)`。实现：[同步](../src/qca/forward/resources/channel_pairings.py#L17) / [异步](../src/qca/forward/resources/channel_pairings.py#L66)。

正文：`code`、`identity_id`、`template_id`。

请求头：`idempotency_key` → `Idempotency-Key`。

请求字段：[TypedDict](../src/qca/forward/types/channel_pairing_create_params.py)。类型定义：[ChannelPairing](../src/qca/forward/types/channel_pairing.py)、[NotGiven](../src/qca/common/_types.py)。

### `channel_pairings.delete`

`DELETE /channel_pairings/{pairing_id}`

```python
def delete(
    pairing_id: str,
) -> DeletedChannelPairing: ...
```

调用：`client.channel_pairings.delete(...)`。实现：[同步](../src/qca/forward/resources/channel_pairings.py#L42) / [异步](../src/qca/forward/resources/channel_pairings.py#L91)。

路径：`pairing_id`。

类型定义：[DeletedChannelPairing](../src/qca/forward/types/deleted_channel_pairing.py)。

## environments

管理运行环境。Managed 的 work 子资源还用于自托管执行器轮询任务、确认、心跳和上报结果。

### `environments.list`

`GET /environments`

```python
def list(
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
) -> SyncPage[Environment]: ...
```

调用：`client.environments.list(...)`。实现：[同步](../src/qca/forward/resources/environments.py#L17) / [异步](../src/qca/forward/resources/environments.py#L162)。异步返回 `AsyncPaginator[Environment]`。

查询：`limit`、`page`、`after_id`、`before_id`。

请求字段：[TypedDict](../src/qca/forward/types/environment_list_params.py)。类型定义：[Environment](../src/qca/forward/types/environment.py)、[NotGiven](../src/qca/common/_types.py)、[SyncPage](../src/qca/common/pagination.py)。

分页协议：`PageCursor`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

### `environments.create`

`POST /environments`

```python
def create(
    *,
    name: str,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    config: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
) -> Environment: ...
```

调用：`client.environments.create(...)`。实现：[同步](../src/qca/forward/resources/environments.py#L42) / [异步](../src/qca/forward/resources/environments.py#L189)。

正文：`name`、`description`、`config`、`metadata`。

请求头：`idempotency_key` → `Idempotency-Key`。

请求字段：[TypedDict](../src/qca/forward/types/environment_create_params.py)。类型定义：[Environment](../src/qca/forward/types/environment.py)、[NotGiven](../src/qca/common/_types.py)。

### `environments.retrieve`

`GET /environments/{environment_id}`

```python
def retrieve(
    environment_id: str,
) -> Environment: ...
```

调用：`client.environments.retrieve(...)`。实现：[同步](../src/qca/forward/resources/environments.py#L68) / [异步](../src/qca/forward/resources/environments.py#L215)。

路径：`environment_id`。

类型定义：[Environment](../src/qca/forward/types/environment.py)。

### `environments.update`

`POST /environments/{environment_id}`

```python
def update(
    environment_id: str,
    *,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    config: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
) -> Environment: ...
```

调用：`client.environments.update(...)`。实现：[同步](../src/qca/forward/resources/environments.py#L90) / [异步](../src/qca/forward/resources/environments.py#L237)。

路径：`environment_id`。

正文：`name`、`description`、`config`、`metadata`。

请求字段：[TypedDict](../src/qca/forward/types/environment_update_params.py)。类型定义：[Environment](../src/qca/forward/types/environment.py)、[NotGiven](../src/qca/common/_types.py)。

### `environments.archive`

`POST /environments/{environment_id}/archive`

```python
def archive(
    environment_id: str,
) -> Environment: ...
```

调用：`client.environments.archive(...)`。实现：[同步](../src/qca/forward/resources/environments.py#L116) / [异步](../src/qca/forward/resources/environments.py#L263)。

路径：`environment_id`。

类型定义：[Environment](../src/qca/forward/types/environment.py)。

### `environments.delete`

`DELETE /environments/{environment_id}`

```python
def delete(
    environment_id: str,
) -> None: ...
```

调用：`client.environments.delete(...)`。实现：[同步](../src/qca/forward/resources/environments.py#L138) / [异步](../src/qca/forward/resources/environments.py#L285)。

路径：`environment_id`。


## files

上传和管理文件元数据，按 ID 下载内容。upload 使用 multipart，download 返回需关闭的二进制响应。

### `files.list`

`GET /files`

```python
def list(
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    scope_id: Union[str, None, NotGiven] = NOT_GIVEN,
) -> SyncPage[FileMetadata]: ...
```

调用：`client.files.list(...)`。实现：[同步](../src/qca/forward/resources/files.py#L18) / [异步](../src/qca/forward/resources/files.py#L146)。异步返回 `AsyncPaginator[FileMetadata]`。

查询：`limit`、`page`、`after_id`、`before_id`、`name`、`scope_id`。

请求字段：[TypedDict](../src/qca/forward/types/file_list_params.py)。类型定义：[FileMetadata](../src/qca/forward/types/file_metadata.py)、[NotGiven](../src/qca/common/_types.py)、[SyncPage](../src/qca/common/pagination.py)。

分页协议：`PageCursor`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

### `files.upload`

`POST /files`

```python
def upload(
    *,
    file: FileTypes,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    purpose: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
) -> FileMetadata: ...
```

调用：`client.files.upload(...)`。实现：[同步](../src/qca/forward/resources/files.py#L52) / [异步](../src/qca/forward/resources/files.py#L182)。

正文：`file`、`name`、`purpose`、`metadata`。

请求头：`idempotency_key` → `Idempotency-Key`。

请求字段：[TypedDict](../src/qca/forward/types/file_upload_params.py)。类型定义：[FileMetadata](../src/qca/forward/types/file_metadata.py)、[FileTypes](../src/qca/common/_types.py)、[NotGiven](../src/qca/common/_types.py)。

### `files.retrieve_metadata`

`GET /files/{file_id}`

```python
def retrieve_metadata(
    file_id: str,
) -> FileMetadata: ...
```

调用：`client.files.retrieve_metadata(...)`。实现：[同步](../src/qca/forward/resources/files.py#L78) / [异步](../src/qca/forward/resources/files.py#L208)。

路径：`file_id`。

类型定义：[FileMetadata](../src/qca/forward/types/file_metadata.py)。

### `files.delete`

`DELETE /files/{file_id}`

```python
def delete(
    file_id: str,
) -> None: ...
```

调用：`client.files.delete(...)`。实现：[同步](../src/qca/forward/resources/files.py#L100) / [异步](../src/qca/forward/resources/files.py#L230)。

路径：`file_id`。


### `files.download`

`GET /files/{file_id}/content`

```python
def download(
    file_id: str,
) -> BinaryAPIResponse: ...
```

调用：`client.files.download(...)`。实现：[同步](../src/qca/forward/resources/files.py#L122) / [异步](../src/qca/forward/resources/files.py#L252)。异步返回 `AsyncBinaryAPIResponse`。

路径：`file_id`。

类型定义：[BinaryAPIResponse](../src/qca/common/_response.py)。

下载返回二进制响应，使用上下文管理器关闭；通过 `write_to_file()` 写入文件。

## identities

按外部用户标识管理身份、启用状态和关联记忆；身份配置可以覆盖指定 Template 的设置。

### `identities.list`

`GET /identities`

```python
def list(
    *,
    external_id: Union[str, None, NotGiven] = NOT_GIVEN,
    identity_i_ds: Union[List[str], None, NotGiven] = NOT_GIVEN,
    search: Union[str, None, NotGiven] = NOT_GIVEN,
    enabled: Union[bool, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
) -> SyncPage[Identity]: ...
```

调用：`client.identities.list(...)`。实现：[同步](../src/qca/forward/resources/identities/identities.py#L32) / [异步](../src/qca/forward/resources/identities/identities.py#L306)。异步返回 `AsyncPaginator[Identity]`。

查询：`external_id`、`identity_i_ds` → `identity_ids`、`search`、`enabled`、`limit`、`after_id`、`before_id`。

请求字段：[TypedDict](../src/qca/forward/types/identity_list_params.py)。类型定义：[Identity](../src/qca/forward/types/identity.py)、[NotGiven](../src/qca/common/_types.py)、[SyncPage](../src/qca/common/pagination.py)。

分页协议：`Page`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

### `identities.create`

`POST /identities`

```python
def create(
    *,
    external_id: str,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    enabled: Union[bool, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
) -> Identity: ...
```

调用：`client.identities.create(...)`。实现：[同步](../src/qca/forward/resources/identities/identities.py#L68) / [异步](../src/qca/forward/resources/identities/identities.py#L344)。

正文：`external_id`、`name`、`enabled`、`metadata`。

请求头：`idempotency_key` → `Idempotency-Key`。

请求字段：[TypedDict](../src/qca/forward/types/identity_create_params.py)。类型定义：[Identity](../src/qca/forward/types/identity.py)、[NotGiven](../src/qca/common/_types.py)。

### `identities.ensure_admin`

`POST /identities/admin/ensure`

```python
def ensure_admin() -> Identity: ...
```

调用：`client.identities.ensure_admin(...)`。实现：[同步](../src/qca/forward/resources/identities/identities.py#L94) / [异步](../src/qca/forward/resources/identities/identities.py#L370)。

类型定义：[Identity](../src/qca/forward/types/identity.py)。

### `identities.stats`

`GET /identities/stats`

```python
def stats() -> IdentityStats: ...
```

调用：`client.identities.stats(...)`。实现：[同步](../src/qca/forward/resources/identities/identities.py#L115) / [异步](../src/qca/forward/resources/identities/identities.py#L391)。

类型定义：[IdentityStats](../src/qca/forward/types/identity_stats.py)。

### `identities.retrieve`

`GET /identities/{identity_id}`

```python
def retrieve(
    identity_id: str,
) -> Identity: ...
```

调用：`client.identities.retrieve(...)`。实现：[同步](../src/qca/forward/resources/identities/identities.py#L136) / [异步](../src/qca/forward/resources/identities/identities.py#L412)。

路径：`identity_id`。

类型定义：[Identity](../src/qca/forward/types/identity.py)。

### `identities.update`

`POST /identities/{identity_id}`

```python
def update(
    identity_id: str,
    *,
    external_id: Union[str, None, NotGiven] = NOT_GIVEN,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    enabled: Union[bool, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
) -> Identity: ...
```

调用：`client.identities.update(...)`。实现：[同步](../src/qca/forward/resources/identities/identities.py#L158) / [异步](../src/qca/forward/resources/identities/identities.py#L434)。

路径：`identity_id`。

正文：`external_id`、`name`、`enabled`、`metadata`。

请求头：`idempotency_key` → `Idempotency-Key`。

请求字段：[TypedDict](../src/qca/forward/types/identity_update_params.py)。类型定义：[Identity](../src/qca/forward/types/identity.py)、[NotGiven](../src/qca/common/_types.py)。

### `identities.delete`

`DELETE /identities/{identity_id}`

```python
def delete(
    identity_id: str,
) -> DeletedIdentity: ...
```

调用：`client.identities.delete(...)`。实现：[同步](../src/qca/forward/resources/identities/identities.py#L185) / [异步](../src/qca/forward/resources/identities/identities.py#L461)。

路径：`identity_id`。

类型定义：[DeletedIdentity](../src/qca/forward/types/deleted_identity.py)。

### `identities.list_templates`

`GET /identities/{identity_id}/agents`

```python
def list_templates(
    identity_id: str,
) -> IdentityListTemplatesResponse: ...
```

调用：`client.identities.list_templates(...)`。实现：[同步](../src/qca/forward/resources/identities/identities.py#L207) / [异步](../src/qca/forward/resources/identities/identities.py#L483)。

路径：`identity_id`。

类型定义：[IdentityListTemplatesResponse](../src/qca/forward/types/identity_list_templates_response.py)。

### `identities.clear`

`POST /identities/{identity_id}/clear`

```python
def clear(
    identity_id: str,
    *,
    reason: Union[str, None, NotGiven] = NOT_GIVEN,
) -> IdentityClearResponse: ...
```

调用：`client.identities.clear(...)`。实现：[同步](../src/qca/forward/resources/identities/identities.py#L229) / [异步](../src/qca/forward/resources/identities/identities.py#L505)。

路径：`identity_id`。

正文：`reason`。

请求字段：[TypedDict](../src/qca/forward/types/identity_clear_params.py)。类型定义：[IdentityClearResponse](../src/qca/forward/types/identity_clear_response.py)、[NotGiven](../src/qca/common/_types.py)。

### `identities.disable`

`POST /identities/{identity_id}/disable`

```python
def disable(
    identity_id: str,
) -> Identity: ...
```

调用：`client.identities.disable(...)`。实现：[同步](../src/qca/forward/resources/identities/identities.py#L252) / [异步](../src/qca/forward/resources/identities/identities.py#L528)。

路径：`identity_id`。

类型定义：[Identity](../src/qca/forward/types/identity.py)。

### `identities.enable`

`POST /identities/{identity_id}/enable`

```python
def enable(
    identity_id: str,
) -> Identity: ...
```

调用：`client.identities.enable(...)`。实现：[同步](../src/qca/forward/resources/identities/identities.py#L274) / [异步](../src/qca/forward/resources/identities/identities.py#L550)。

路径：`identity_id`。

类型定义：[Identity](../src/qca/forward/types/identity.py)。

### `identities.configs.list`

`GET /identities/{identity_id}/templates`

```python
def list(
    identity_id: str,
    *,
    template_id: Union[str, None, NotGiven] = NOT_GIVEN,
    status: Union[str, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
) -> SyncPage[IdentityConfig]: ...
```

调用：`client.identities.configs.list(...)`。实现：[同步](../src/qca/forward/resources/identities/configs.py#L19) / [异步](../src/qca/forward/resources/identities/configs.py#L135)。异步返回 `AsyncPaginator[IdentityConfig]`。

路径：`identity_id`。

查询：`template_id`、`status`、`limit`、`after_id`、`before_id`。

请求字段：[TypedDict](../src/qca/forward/types/identity_config_list_params.py)。类型定义：[IdentityConfig](../src/qca/forward/types/identity_config.py)、[NotGiven](../src/qca/common/_types.py)、[SyncPage](../src/qca/common/pagination.py)。

分页协议：`Page`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

### `identities.configs.retrieve`

`GET /identities/{identity_id}/templates/{template_id}/config`

```python
def retrieve(
    template_id: str,
    *,
    identity_id: str,
) -> IdentityConfig: ...
```

调用：`client.identities.configs.retrieve(...)`。实现：[同步](../src/qca/forward/resources/identities/configs.py#L52) / [异步](../src/qca/forward/resources/identities/configs.py#L170)。

路径：`template_id`、`identity_id`。

类型定义：[IdentityConfig](../src/qca/forward/types/identity_config.py)。

### `identities.configs.upsert`

`POST /identities/{identity_id}/templates/{template_id}/config`

```python
def upsert(
    template_id: str,
    *,
    identity_id: str,
    identity_config: IdentityConfigSpecParam,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
) -> IdentityConfig: ...
```

调用：`client.identities.configs.upsert(...)`。实现：[同步](../src/qca/forward/resources/identities/configs.py#L77) / [异步](../src/qca/forward/resources/identities/configs.py#L195)。

路径：`template_id`、`identity_id`。

正文：`name`、`identity_config`、`metadata`。

请求头：`idempotency_key` → `Idempotency-Key`。

请求字段：[TypedDict](../src/qca/forward/types/identity_config_upsert_params.py)。类型定义：[IdentityConfig](../src/qca/forward/types/identity_config.py)、[IdentityConfigSpecParam](../src/qca/forward/types/identity_config_spec_param.py)、[NotGiven](../src/qca/common/_types.py)。

### `identities.configs.retrieve_effective`

`GET /identities/{identity_id}/templates/{template_id}/effective`

```python
def retrieve_effective(
    template_id: str,
    *,
    identity_id: str,
) -> EffectiveConfig: ...
```

调用：`client.identities.configs.retrieve_effective(...)`。实现：[同步](../src/qca/forward/resources/identities/configs.py#L106) / [异步](../src/qca/forward/resources/identities/configs.py#L224)。

路径：`template_id`、`identity_id`。

类型定义：[EffectiveConfig](../src/qca/forward/types/effective_config.py)。

### `identities.memory_stores.list`

`GET /identities/{identity_id}/templates/{template_id}/memory_stores`

```python
def list(
    template_id: str,
    *,
    identity_id: str,
) -> IdentityMemoryStoreListResponse: ...
```

调用：`client.identities.memory_stores.list(...)`。实现：[同步](../src/qca/forward/resources/identities/memory_stores.py#L18) / [异步](../src/qca/forward/resources/identities/memory_stores.py#L104)。

路径：`template_id`、`identity_id`。

类型定义：[IdentityMemoryStoreListResponse](../src/qca/forward/types/identity_memory_store_list_response.py)。

### `identities.memory_stores.mount`

`POST /identities/{identity_id}/templates/{template_id}/memory_stores`

```python
def mount(
    template_id: str,
    *,
    identity_id: str,
    memory_store_id: str,
) -> MemoryStoreMount: ...
```

调用：`client.identities.memory_stores.mount(...)`。实现：[同步](../src/qca/forward/resources/identities/memory_stores.py#L45) / [异步](../src/qca/forward/resources/identities/memory_stores.py#L131)。

路径：`template_id`、`identity_id`。

正文：`memory_store_id`。

请求字段：[TypedDict](../src/qca/forward/types/identity_memory_store_mount_params.py)。类型定义：[MemoryStoreMount](../src/qca/forward/types/memory_store_mount.py)。

### `identities.memory_stores.detach`

`DELETE /identities/{identity_id}/templates/{template_id}/memory_stores/{memory_store_id}`

```python
def detach(
    memory_store_id: str,
    *,
    template_id: str,
    identity_id: str,
) -> DeletedMemoryStoreMount: ...
```

调用：`client.identities.memory_stores.detach(...)`。实现：[同步](../src/qca/forward/resources/identities/memory_stores.py#L73) / [异步](../src/qca/forward/resources/identities/memory_stores.py#L159)。

路径：`memory_store_id`、`template_id`、`identity_id`。

类型定义：[DeletedMemoryStoreMount](../src/qca/forward/types/deleted_memory_store_mount.py)。

## memory_stores

管理记忆存储、记忆正文与历史版本；Memory Store 通过会话资源挂载后可供助手访问。

### `memory_stores.list`

`GET /memory_stores`

```python
def list(
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    system_managed: Union[bool, None, NotGiven] = NOT_GIVEN,
) -> SyncPage[MemoryStore]: ...
```

调用：`client.memory_stores.list(...)`。实现：[同步](../src/qca/forward/resources/memory_stores/memory_stores.py#L29) / [异步](../src/qca/forward/resources/memory_stores/memory_stores.py#L180)。异步返回 `AsyncPaginator[MemoryStore]`。

查询：`limit`、`before_id`、`after_id`、`system_managed`。

请求字段：[TypedDict](../src/qca/forward/types/memory_store_list_params.py)。类型定义：[MemoryStore](../src/qca/forward/types/memory_store.py)、[NotGiven](../src/qca/common/_types.py)、[SyncPage](../src/qca/common/pagination.py)。

分页协议：`Page`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

### `memory_stores.create`

`POST /memory_stores`

```python
def create(
    *,
    name: str,
    idempotency_key: str,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
) -> MemoryStore: ...
```

调用：`client.memory_stores.create(...)`。实现：[同步](../src/qca/forward/resources/memory_stores/memory_stores.py#L54) / [异步](../src/qca/forward/resources/memory_stores/memory_stores.py#L207)。

正文：`name`、`description`、`metadata`。

请求头：`idempotency_key` → `Idempotency-Key`。

请求字段：[TypedDict](../src/qca/forward/types/memory_store_create_params.py)。类型定义：[MemoryStore](../src/qca/forward/types/memory_store.py)、[NotGiven](../src/qca/common/_types.py)。

### `memory_stores.retrieve`

`GET /memory_stores/{memory_store_id}`

```python
def retrieve(
    memory_store_id: str,
) -> MemoryStore: ...
```

调用：`client.memory_stores.retrieve(...)`。实现：[同步](../src/qca/forward/resources/memory_stores/memory_stores.py#L79) / [异步](../src/qca/forward/resources/memory_stores/memory_stores.py#L232)。

路径：`memory_store_id`。

类型定义：[MemoryStore](../src/qca/forward/types/memory_store.py)。

### `memory_stores.update`

`POST /memory_stores/{memory_store_id}`

```python
def update(
    memory_store_id: str,
    *,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
) -> MemoryStore: ...
```

调用：`client.memory_stores.update(...)`。实现：[同步](../src/qca/forward/resources/memory_stores/memory_stores.py#L101) / [异步](../src/qca/forward/resources/memory_stores/memory_stores.py#L254)。

路径：`memory_store_id`。

正文：`name`、`description`、`metadata`。

请求字段：[TypedDict](../src/qca/forward/types/memory_store_update_params.py)。类型定义：[MemoryStore](../src/qca/forward/types/memory_store.py)、[NotGiven](../src/qca/common/_types.py)。

### `memory_stores.delete`

`DELETE /memory_stores/{memory_store_id}`

```python
def delete(
    memory_store_id: str,
) -> DeletedMemoryStore: ...
```

调用：`client.memory_stores.delete(...)`。实现：[同步](../src/qca/forward/resources/memory_stores/memory_stores.py#L126) / [异步](../src/qca/forward/resources/memory_stores/memory_stores.py#L279)。

路径：`memory_store_id`。

类型定义：[DeletedMemoryStore](../src/qca/forward/types/deleted_memory_store.py)。

### `memory_stores.archive`

`POST /memory_stores/{memory_store_id}/archive`

```python
def archive(
    memory_store_id: str,
) -> MemoryStore: ...
```

调用：`client.memory_stores.archive(...)`。实现：[同步](../src/qca/forward/resources/memory_stores/memory_stores.py#L148) / [异步](../src/qca/forward/resources/memory_stores/memory_stores.py#L301)。

路径：`memory_store_id`。

类型定义：[MemoryStore](../src/qca/forward/types/memory_store.py)。

### `memory_stores.memories.list`

`GET /memory_stores/{memory_store_id}/memories`

```python
def list(
    memory_store_id: str,
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    path_prefix: Union[str, None, NotGiven] = NOT_GIVEN,
) -> SyncPage[Memory]: ...
```

调用：`client.memory_stores.memories.list(...)`。实现：[同步](../src/qca/forward/resources/memory_stores/memories.py#L18) / [异步](../src/qca/forward/resources/memory_stores/memories.py#L155)。异步返回 `AsyncPaginator[Memory]`。

路径：`memory_store_id`。

查询：`limit`、`before_id`、`after_id`、`path_prefix`。

请求字段：[TypedDict](../src/qca/forward/types/memory_store_memory_list_params.py)。类型定义：[Memory](../src/qca/forward/types/memory.py)、[NotGiven](../src/qca/common/_types.py)、[SyncPage](../src/qca/common/pagination.py)。

分页协议：`Page`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

### `memory_stores.memories.create`

`POST /memory_stores/{memory_store_id}/memories`

```python
def create(
    memory_store_id: str,
    *,
    path: str,
    content: str,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
) -> Memory: ...
```

调用：`client.memory_stores.memories.create(...)`。实现：[同步](../src/qca/forward/resources/memory_stores/memories.py#L44) / [异步](../src/qca/forward/resources/memory_stores/memories.py#L183)。

路径：`memory_store_id`。

正文：`path`、`content`、`metadata`。

请求字段：[TypedDict](../src/qca/forward/types/memory_store_memory_create_params.py)。类型定义：[Memory](../src/qca/forward/types/memory.py)、[NotGiven](../src/qca/common/_types.py)。

### `memory_stores.memories.retrieve`

`GET /memory_stores/{memory_store_id}/memories/{memory_id}`

```python
def retrieve(
    memory_id: str,
    *,
    memory_store_id: str,
) -> Memory: ...
```

调用：`client.memory_stores.memories.retrieve(...)`。实现：[同步](../src/qca/forward/resources/memory_stores/memories.py#L69) / [异步](../src/qca/forward/resources/memory_stores/memories.py#L208)。

路径：`memory_id`、`memory_store_id`。

类型定义：[Memory](../src/qca/forward/types/memory.py)。

### `memory_stores.memories.update`

`POST /memory_stores/{memory_store_id}/memories/{memory_id}`

```python
def update(
    memory_id: str,
    *,
    memory_store_id: str,
    content: str,
    content_sha256: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
) -> Memory: ...
```

调用：`client.memory_stores.memories.update(...)`。实现：[同步](../src/qca/forward/resources/memory_stores/memories.py#L96) / [异步](../src/qca/forward/resources/memory_stores/memories.py#L235)。

路径：`memory_id`、`memory_store_id`。

正文：`content`、`content_sha256`、`metadata`。

请求字段：[TypedDict](../src/qca/forward/types/memory_store_memory_update_params.py)。类型定义：[Memory](../src/qca/forward/types/memory.py)、[NotGiven](../src/qca/common/_types.py)。

### `memory_stores.memories.delete`

`DELETE /memory_stores/{memory_store_id}/memories/{memory_id}`

```python
def delete(
    memory_id: str,
    *,
    memory_store_id: str,
) -> DeletedMemory: ...
```

调用：`client.memory_stores.memories.delete(...)`。实现：[同步](../src/qca/forward/resources/memory_stores/memories.py#L126) / [异步](../src/qca/forward/resources/memory_stores/memories.py#L265)。

路径：`memory_id`、`memory_store_id`。

类型定义：[DeletedMemory](../src/qca/forward/types/deleted_memory.py)。

### `memory_stores.memory_versions.list`

`GET /memory_stores/{memory_store_id}/memory_versions`

```python
def list(
    memory_store_id: str,
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    memory_id: Union[str, None, NotGiven] = NOT_GIVEN,
) -> SyncPage[MemoryVersion]: ...
```

调用：`client.memory_stores.memory_versions.list(...)`。实现：[同步](../src/qca/forward/resources/memory_stores/memory_versions.py#L17) / [异步](../src/qca/forward/resources/memory_stores/memory_versions.py#L99)。异步返回 `AsyncPaginator[MemoryVersion]`。

路径：`memory_store_id`。

查询：`limit`、`before_id`、`after_id`、`memory_id`。

请求字段：[TypedDict](../src/qca/forward/types/memory_store_memory_version_list_params.py)。类型定义：[MemoryVersion](../src/qca/forward/types/memory_version.py)、[NotGiven](../src/qca/common/_types.py)、[SyncPage](../src/qca/common/pagination.py)。

分页协议：`Page`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

### `memory_stores.memory_versions.retrieve`

`GET /memory_stores/{memory_store_id}/memory_versions/{memory_version_id}`

```python
def retrieve(
    memory_version_id: str,
    *,
    memory_store_id: str,
) -> MemoryVersion: ...
```

调用：`client.memory_stores.memory_versions.retrieve(...)`。实现：[同步](../src/qca/forward/resources/memory_stores/memory_versions.py#L43) / [异步](../src/qca/forward/resources/memory_stores/memory_versions.py#L127)。

路径：`memory_version_id`、`memory_store_id`。

类型定义：[MemoryVersion](../src/qca/forward/types/memory_version.py)。

### `memory_stores.memory_versions.redact`

`POST /memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact`

```python
def redact(
    memory_version_id: str,
    *,
    memory_store_id: str,
) -> MemoryVersion: ...
```

调用：`client.memory_stores.memory_versions.redact(...)`。实现：[同步](../src/qca/forward/resources/memory_stores/memory_versions.py#L70) / [异步](../src/qca/forward/resources/memory_stores/memory_versions.py#L154)。

路径：`memory_version_id`、`memory_store_id`。

类型定义：[MemoryVersion](../src/qca/forward/types/memory_version.py)。

## models

获取当前账号的模型列表与启用状态，创建 Agent 或 Template 前可从中选择可用模型。

### `models.list`

`GET /models`

```python
def list() -> ModelListResponse: ...
```

调用：`client.models.list(...)`。实现：[同步](../src/qca/forward/resources/models.py#L16) / [异步](../src/qca/forward/resources/models.py#L39)。

类型定义：[ModelListResponse](../src/qca/forward/types/model_list_response.py)。

## schedules

创建并管理定时任务，支持暂停、恢复和手动触发。执行记录位于 schedule_runs。

### `schedules.list`

`GET /schedules`

```python
def list(
    *,
    identity_id: Union[str, None, NotGiven] = NOT_GIVEN,
    template_id: Union[str, None, NotGiven] = NOT_GIVEN,
    status: Union[str, None, NotGiven] = NOT_GIVEN,
    include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    sort_by: Union[str, None, NotGiven] = NOT_GIVEN,
    order: Union[str, None, NotGiven] = NOT_GIVEN,
) -> SyncPage[Schedule]: ...
```

调用：`client.schedules.list(...)`。实现：[同步](../src/qca/forward/resources/schedules.py#L19) / [异步](../src/qca/forward/resources/schedules.py#L283)。异步返回 `AsyncPaginator[Schedule]`。

查询：`identity_id`、`template_id`、`status`、`include_archived`、`limit`、`after_id`、`before_id`、`sort_by`、`order`。

请求字段：[TypedDict](../src/qca/forward/types/schedule_list_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[Schedule](../src/qca/forward/types/schedule.py)、[SyncPage](../src/qca/common/pagination.py)。

分页协议：`Page`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

### `schedules.create`

`POST /schedules`

```python
def create(
    *,
    identity_id: str,
    template_id: str,
    name: str,
    initial_events: List[Dict[str, Any]],
    environment_id: str,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    execution: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    trigger_policy: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    sinks: Union[List[Dict[str, Any]], None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
) -> Schedule: ...
```

调用：`client.schedules.create(...)`。实现：[同步](../src/qca/forward/resources/schedules.py#L59) / [异步](../src/qca/forward/resources/schedules.py#L325)。

正文：`identity_id`、`template_id`、`name`、`description`、`initial_events`、`execution`、`trigger_policy`、`environment_id`、`sinks`、`metadata`。

请求头：`idempotency_key` → `Idempotency-Key`。

请求字段：[TypedDict](../src/qca/forward/types/schedule_create_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[Schedule](../src/qca/forward/types/schedule.py)。

### `schedules.archive_many`

`POST /schedules/archive`

```python
def archive_many(
    *,
    schedule_ids: List[str],
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
) -> ScheduleArchiveManyResponse: ...
```

调用：`client.schedules.archive_many(...)`。实现：[同步](../src/qca/forward/resources/schedules.py#L102) / [异步](../src/qca/forward/resources/schedules.py#L368)。

正文：`schedule_ids`。

请求头：`idempotency_key` → `Idempotency-Key`。

请求字段：[TypedDict](../src/qca/forward/types/schedule_archive_many_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[ScheduleArchiveManyResponse](../src/qca/forward/types/schedule_archive_many_response.py)。

自动设置正文字段 `scope="by_schedule_ids"`，只归档 `schedule_ids` 指定的任务。

### `schedules.retrieve`

`GET /schedules/{schedule_id}`

```python
def retrieve(
    schedule_id: str,
) -> Schedule: ...
```

调用：`client.schedules.retrieve(...)`。实现：[同步](../src/qca/forward/resources/schedules.py#L125) / [异步](../src/qca/forward/resources/schedules.py#L391)。

路径：`schedule_id`。

类型定义：[Schedule](../src/qca/forward/types/schedule.py)。

### `schedules.update`

`POST /schedules/{schedule_id}`

```python
def update(
    schedule_id: str,
    *,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    template_id: Union[str, None, NotGiven] = NOT_GIVEN,
    initial_events: Union[List[Dict[str, Any]], None, NotGiven] = NOT_GIVEN,
    execution: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    trigger_policy: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    environment_id: Union[str, None, NotGiven] = NOT_GIVEN,
    sinks: Union[List[Dict[str, Any]], None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
) -> Schedule: ...
```

调用：`client.schedules.update(...)`。实现：[同步](../src/qca/forward/resources/schedules.py#L147) / [异步](../src/qca/forward/resources/schedules.py#L413)。

路径：`schedule_id`。

正文：`name`、`description`、`template_id`、`initial_events`、`execution`、`trigger_policy`、`environment_id`、`sinks`、`metadata`。

请求头：`idempotency_key` → `Idempotency-Key`。

请求字段：[TypedDict](../src/qca/forward/types/schedule_update_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[Schedule](../src/qca/forward/types/schedule.py)。

### `schedules.archive`

`POST /schedules/{schedule_id}/archive`

```python
def archive(
    schedule_id: str,
    *,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
) -> Schedule: ...
```

调用：`client.schedules.archive(...)`。实现：[同步](../src/qca/forward/resources/schedules.py#L189) / [异步](../src/qca/forward/resources/schedules.py#L455)。

路径：`schedule_id`。

请求头：`idempotency_key` → `Idempotency-Key`。

请求字段：[TypedDict](../src/qca/forward/types/schedule_archive_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[Schedule](../src/qca/forward/types/schedule.py)。

### `schedules.pause`

`POST /schedules/{schedule_id}/pause`

```python
def pause(
    schedule_id: str,
    *,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
) -> Schedule: ...
```

调用：`client.schedules.pause(...)`。实现：[同步](../src/qca/forward/resources/schedules.py#L212) / [异步](../src/qca/forward/resources/schedules.py#L478)。

路径：`schedule_id`。

请求头：`idempotency_key` → `Idempotency-Key`。

请求字段：[TypedDict](../src/qca/forward/types/schedule_pause_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[Schedule](../src/qca/forward/types/schedule.py)。

### `schedules.run`

`POST /schedules/{schedule_id}/run`

```python
def run(
    schedule_id: str,
    *,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
) -> ScheduleRun: ...
```

调用：`client.schedules.run(...)`。实现：[同步](../src/qca/forward/resources/schedules.py#L235) / [异步](../src/qca/forward/resources/schedules.py#L501)。

路径：`schedule_id`。

请求头：`idempotency_key` → `Idempotency-Key`。

请求字段：[TypedDict](../src/qca/forward/types/schedule_run_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[ScheduleRun](../src/qca/forward/types/schedule_run.py)。

### `schedules.unpause`

`POST /schedules/{schedule_id}/unpause`

```python
def unpause(
    schedule_id: str,
    *,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
) -> Schedule: ...
```

调用：`client.schedules.unpause(...)`。实现：[同步](../src/qca/forward/resources/schedules.py#L258) / [异步](../src/qca/forward/resources/schedules.py#L524)。

路径：`schedule_id`。

请求头：`idempotency_key` → `Idempotency-Key`。

请求字段：[TypedDict](../src/qca/forward/types/schedule_unpause_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[Schedule](../src/qca/forward/types/schedule.py)。

## schedule_runs

读取定时任务的执行记录及关联会话，检查执行状态与最终结果。

### `schedule_runs.list`

`GET /schedule_runs`

```python
def list(
    *,
    identity_id: Union[str, None, NotGiven] = NOT_GIVEN,
    schedule_id: Union[str, None, NotGiven] = NOT_GIVEN,
    status: Union[str, None, NotGiven] = NOT_GIVEN,
    trigger_type: Union[str, None, NotGiven] = NOT_GIVEN,
    has_error: Union[bool, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    sort_by: Union[str, None, NotGiven] = NOT_GIVEN,
    order: Union[str, None, NotGiven] = NOT_GIVEN,
) -> SyncPage[ScheduleRun]: ...
```

调用：`client.schedule_runs.list(...)`。实现：[同步](../src/qca/forward/resources/schedule_runs.py#L17) / [异步](../src/qca/forward/resources/schedule_runs.py#L84)。异步返回 `AsyncPaginator[ScheduleRun]`。

查询：`identity_id`、`schedule_id`、`status`、`trigger_type`、`has_error`、`limit`、`after_id`、`before_id`、`sort_by`、`order`。

请求字段：[TypedDict](../src/qca/forward/types/schedule_run_list_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[ScheduleRun](../src/qca/forward/types/schedule_run.py)、[SyncPage](../src/qca/common/pagination.py)。

分页协议：`Page`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

### `schedule_runs.retrieve`

`GET /schedule_runs/{run_id}`

```python
def retrieve(
    run_id: str,
    *,
    identity_id: Union[str, None, NotGiven] = NOT_GIVEN,
) -> ScheduleRun: ...
```

调用：`client.schedule_runs.retrieve(...)`。实现：[同步](../src/qca/forward/resources/schedule_runs.py#L59) / [异步](../src/qca/forward/resources/schedule_runs.py#L128)。

路径：`run_id`。

查询：`identity_id`。

请求字段：[TypedDict](../src/qca/forward/types/schedule_run_retrieve_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[ScheduleRun](../src/qca/forward/types/schedule_run.py)。

## sessions

创建、查询和管理会话。events 发送输入并读取历史或 SSE；threads 访问子线程，resources 管理挂载资源。

### `sessions.list`

`GET /sessions`

```python
def list(
    *,
    identity_i_ds: Union[List[str], None, NotGiven] = NOT_GIVEN,
    template_id: Union[str, None, NotGiven] = NOT_GIVEN,
    source_type: Union[str, None, NotGiven] = NOT_GIVEN,
    created_at_gt: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lt: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    updated_at_gt: Union[datetime, None, NotGiven] = NOT_GIVEN,
    updated_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    updated_at_lt: Union[datetime, None, NotGiven] = NOT_GIVEN,
    updated_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    order: Union[str, None, NotGiven] = NOT_GIVEN,
    include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
) -> SyncPage[Session]: ...
```

调用：`client.sessions.list(...)`。实现：[同步](../src/qca/forward/resources/sessions/sessions.py#L37) / [异步](../src/qca/forward/resources/sessions/sessions.py#L234)。异步返回 `AsyncPaginator[Session]`。

查询：`identity_i_ds` → `identity_ids`、`template_id`、`source_type`、`created_at_gt` → `created_at[gt]`、`created_at_gte` → `created_at[gte]`、`created_at_lt` → `created_at[lt]`、`created_at_lte` → `created_at[lte]`、`updated_at_gt` → `updated_at[gt]`、`updated_at_gte` → `updated_at[gte]`、`updated_at_lt` → `updated_at[lt]`、`updated_at_lte` → `updated_at[lte]`、`limit`、`after_id`、`before_id`、`order`、`include_archived`。

请求字段：[TypedDict](../src/qca/forward/types/session_list_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[Session](../src/qca/forward/types/session.py)、[SyncPage](../src/qca/common/pagination.py)。

分页协议：`Page`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

### `sessions.create`

`POST /sessions`

```python
def create(
    *,
    identity_id: str,
    template_id: str,
    title: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    config: Union[SessionCreateParamsConfigParam, None, NotGiven] = NOT_GIVEN,
    resources: Union[List[SessionResourceSpecParam], None, NotGiven] = NOT_GIVEN,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
) -> Session: ...
```

调用：`client.sessions.create(...)`。实现：[同步](../src/qca/forward/resources/sessions/sessions.py#L91) / [异步](../src/qca/forward/resources/sessions/sessions.py#L290)。

正文：`identity_id`、`template_id`、`title`、`metadata`、`config`、`resources`。

请求头：`idempotency_key` → `Idempotency-Key`。

请求字段：[TypedDict](../src/qca/forward/types/session_create_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[Session](../src/qca/forward/types/session.py)、[SessionCreateParamsConfigParam](../src/qca/forward/types/session_create_params_config_param.py)、[SessionResourceSpecParam](../src/qca/forward/types/session_resource_spec_param.py)。

### `sessions.retrieve`

`GET /sessions/{session_id}`

```python
def retrieve(
    session_id: str,
) -> Session: ...
```

调用：`client.sessions.retrieve(...)`。实现：[同步](../src/qca/forward/resources/sessions/sessions.py#L126) / [异步](../src/qca/forward/resources/sessions/sessions.py#L325)。

路径：`session_id`。

类型定义：[Session](../src/qca/forward/types/session.py)。

### `sessions.update`

`POST /sessions/{session_id}`

```python
def update(
    session_id: str,
    *,
    title: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    config: Union[SessionUpdateParamsConfigParam, None, NotGiven] = NOT_GIVEN,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
) -> Session: ...
```

调用：`client.sessions.update(...)`。实现：[同步](../src/qca/forward/resources/sessions/sessions.py#L148) / [异步](../src/qca/forward/resources/sessions/sessions.py#L347)。

路径：`session_id`。

正文：`title`、`metadata`、`config`。

请求头：`idempotency_key` → `Idempotency-Key`。

请求字段：[TypedDict](../src/qca/forward/types/session_update_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[Session](../src/qca/forward/types/session.py)、[SessionUpdateParamsConfigParam](../src/qca/forward/types/session_update_params_config_param.py)。

### `sessions.archive`

`POST /sessions/{session_id}/archive`

```python
def archive(
    session_id: str,
    *,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
) -> Session: ...
```

调用：`client.sessions.archive(...)`。实现：[同步](../src/qca/forward/resources/sessions/sessions.py#L174) / [异步](../src/qca/forward/resources/sessions/sessions.py#L373)。

路径：`session_id`。

请求头：`idempotency_key` → `Idempotency-Key`。

请求字段：[TypedDict](../src/qca/forward/types/session_archive_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[Session](../src/qca/forward/types/session.py)。

### `sessions.cancel`

`POST /sessions/{session_id}/cancel`

```python
def cancel(
    session_id: str,
    *,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
) -> Session: ...
```

调用：`client.sessions.cancel(...)`。实现：[同步](../src/qca/forward/resources/sessions/sessions.py#L197) / [异步](../src/qca/forward/resources/sessions/sessions.py#L396)。

路径：`session_id`。

请求头：`idempotency_key` → `Idempotency-Key`。

请求字段：[TypedDict](../src/qca/forward/types/session_cancel_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[Session](../src/qca/forward/types/session.py)。

### `sessions.events.list`

`GET /sessions/{session_id}/events`

```python
def list(
    session_id: str,
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    order: Union[str, None, NotGiven] = NOT_GIVEN,
    type: Union[str, None, NotGiven] = NOT_GIVEN,
    types: Union[List[str], None, NotGiven] = NOT_GIVEN,
    include_tool_calls: Union[bool, None, NotGiven] = NOT_GIVEN,
    include_thinking: Union[bool, None, NotGiven] = NOT_GIVEN,
) -> SyncPage[SessionEvent]: ...
```

调用：`client.sessions.events.list(...)`。实现：[同步](../src/qca/forward/resources/sessions/events.py#L20) / [异步](../src/qca/forward/resources/sessions/events.py#L115)。异步返回 `AsyncPaginator[SessionEvent]`。

路径：`session_id`。

查询：`limit`、`after_id`、`before_id`、`order`、`type`、`types` → `types[]`、`include_tool_calls`、`include_thinking`。

请求字段：[TypedDict](../src/qca/forward/types/session_event_list_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[SessionEvent](../src/qca/forward/types/session_event.py)、[SyncPage](../src/qca/common/pagination.py)。

分页协议：`Page`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

### `sessions.events.send`

`POST /sessions/{session_id}/events`

```python
def send(
    session_id: str,
    *,
    events: List[SessionEventParam],
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
) -> SessionEventSendResponse: ...
```

调用：`client.sessions.events.send(...)`。实现：[同步](../src/qca/forward/resources/sessions/events.py#L59) / [异步](../src/qca/forward/resources/sessions/events.py#L156)。

路径：`session_id`。

正文：`events`。

请求头：`idempotency_key` → `Idempotency-Key`。

请求字段：[TypedDict](../src/qca/forward/types/session_event_send_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[SessionEventParam](../src/qca/forward/types/session_event_param.py)、[SessionEventSendResponse](../src/qca/forward/types/session_event_send_response.py)。

### `sessions.events.stream`

`GET /sessions/{session_id}/events/stream`

```python
def stream(
    session_id: str,
    *,
    event_deltas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    include_tool_calls: Union[bool, None, NotGiven] = NOT_GIVEN,
    include_thinking: Union[bool, None, NotGiven] = NOT_GIVEN,
    last_event_id: Union[str, None, NotGiven] = NOT_GIVEN,
) -> Stream[SessionEvent]: ...
```

调用：`client.sessions.events.stream(...)`。实现：[同步](../src/qca/forward/resources/sessions/events.py#L83) / [异步](../src/qca/forward/resources/sessions/events.py#L180)。异步返回 `AsyncStream[SessionEvent]`。

路径：`session_id`。

查询：`event_deltas` → `event_deltas[]`、`include_tool_calls`、`include_thinking`。

请求头：`last_event_id` → `Last-Event-ID`。

请求字段：[TypedDict](../src/qca/forward/types/session_event_stream_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[SessionEvent](../src/qca/forward/types/session_event.py)、[Stream](../src/qca/common/_streaming.py)。

SSE：读取事件直到业务终止条件，退出上下文关闭连接；保存 `last_event_id` 用于断点恢复。

### `sessions.resources.add`

`POST /sessions/{session_id}/resources`

```python
def add(
    session_id: str,
    *,
    type: str,
    file_id: str,
    mount_path: Union[str, None, NotGiven] = NOT_GIVEN,
) -> SessionResource: ...
```

调用：`client.sessions.resources.add(...)`。实现：[同步](../src/qca/forward/resources/sessions/resources.py#L16) / [异步](../src/qca/forward/resources/sessions/resources.py#L43)。

路径：`session_id`。

正文：`type`、`file_id`、`mount_path`。

请求字段：[TypedDict](../src/qca/forward/types/session_resource_add_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[SessionResource](../src/qca/forward/types/session_resource.py)。

### `sessions.threads.list`

`GET /sessions/{session_id}/threads`

```python
def list(
    session_id: str,
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
) -> SyncPage[SessionThread]: ...
```

调用：`client.sessions.threads.list(...)`。实现：[同步](../src/qca/forward/resources/sessions/threads/threads.py#L23) / [异步](../src/qca/forward/resources/sessions/threads/threads.py#L103)。异步返回 `AsyncPaginator[SessionThread]`。

路径：`session_id`。

查询：`limit`、`after_id`、`before_id`。

请求字段：[TypedDict](../src/qca/forward/types/session_thread_list_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[SessionThread](../src/qca/forward/types/session_thread.py)、[SyncPage](../src/qca/common/pagination.py)。

分页协议：`Page`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

### `sessions.threads.retrieve`

`GET /sessions/{session_id}/threads/{thread_id}`

```python
def retrieve(
    thread_id: str,
    *,
    session_id: str,
) -> SessionThread: ...
```

调用：`client.sessions.threads.retrieve(...)`。实现：[同步](../src/qca/forward/resources/sessions/threads/threads.py#L48) / [异步](../src/qca/forward/resources/sessions/threads/threads.py#L130)。

路径：`thread_id`、`session_id`。

类型定义：[SessionThread](../src/qca/forward/types/session_thread.py)。

### `sessions.threads.archive`

`POST /sessions/{session_id}/threads/{thread_id}/archive`

```python
def archive(
    thread_id: str,
    *,
    session_id: str,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
) -> SessionThread: ...
```

调用：`client.sessions.threads.archive(...)`。实现：[同步](../src/qca/forward/resources/sessions/threads/threads.py#L71) / [异步](../src/qca/forward/resources/sessions/threads/threads.py#L153)。

路径：`thread_id`、`session_id`。

请求头：`idempotency_key` → `Idempotency-Key`。

请求字段：[TypedDict](../src/qca/forward/types/session_thread_archive_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[SessionThread](../src/qca/forward/types/session_thread.py)。

### `sessions.threads.events.list`

`GET /sessions/{session_id}/threads/{thread_id}/events`

```python
def list(
    thread_id: str,
    *,
    session_id: str,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
) -> SyncPage[SessionEvent]: ...
```

调用：`client.sessions.threads.events.list(...)`。实现：[同步](../src/qca/forward/resources/sessions/threads/events.py#L18) / [异步](../src/qca/forward/resources/sessions/threads/events.py#L74)。异步返回 `AsyncPaginator[SessionEvent]`。

路径：`thread_id`、`session_id`。

查询：`limit`、`after_id`、`before_id`。

请求字段：[TypedDict](../src/qca/forward/types/session_thread_event_list_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[SessionEvent](../src/qca/forward/types/session_event.py)、[SyncPage](../src/qca/common/pagination.py)。

分页协议：`Page`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

### `sessions.threads.events.stream`

`GET /sessions/{session_id}/threads/{thread_id}/stream`

```python
def stream(
    thread_id: str,
    *,
    session_id: str,
    last_event_id: Union[str, None, NotGiven] = NOT_GIVEN,
) -> Stream[SessionEvent]: ...
```

调用：`client.sessions.threads.events.stream(...)`。实现：[同步](../src/qca/forward/resources/sessions/threads/events.py#L46) / [异步](../src/qca/forward/resources/sessions/threads/events.py#L104)。异步返回 `AsyncStream[SessionEvent]`。

路径：`thread_id`、`session_id`。

请求头：`last_event_id` → `Last-Event-ID`。

请求字段：[TypedDict](../src/qca/forward/types/session_thread_event_stream_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[SessionEvent](../src/qca/forward/types/session_event.py)、[Stream](../src/qca/common/_streaming.py)。

SSE：读取事件直到业务终止条件，退出上下文关闭连接；保存 `last_event_id` 用于断点恢复。

## skills

上传 Skill 文件并管理版本；版本下载返回二进制响应。Skill 路径会保留在 multipart 文件名中。

### `skills.list`

`GET /skills`

```python
def list(
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    display_title: Union[str, None, NotGiven] = NOT_GIVEN,
    source: Union[str, None, NotGiven] = NOT_GIVEN,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
) -> SyncPage[Skill]: ...
```

调用：`client.skills.list(...)`。实现：[同步](../src/qca/forward/resources/skills/skills.py#L23) / [异步](../src/qca/forward/resources/skills/skills.py#L182)。异步返回 `AsyncPaginator[Skill]`。

查询：`limit`、`page`、`after_id`、`before_id`、`display_title`、`source`、`name`。

请求字段：[TypedDict](../src/qca/forward/types/skill_list_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[Skill](../src/qca/forward/types/skill.py)、[SyncPage](../src/qca/common/pagination.py)。

分页协议：`PageCursor`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

### `skills.create`

`POST /skills`

```python
def create(
    *,
    files: Union[List[FileTypes], None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    icon_id: Union[str, None, NotGiven] = NOT_GIVEN,
    file: Union[FileTypes, None, NotGiven] = NOT_GIVEN,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    type: Union[str, None, NotGiven] = NOT_GIVEN,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
) -> Skill: ...
```

调用：`client.skills.create(...)`。实现：[同步](../src/qca/forward/resources/skills/skills.py#L59) / [异步](../src/qca/forward/resources/skills/skills.py#L220)。

正文：`files`、`metadata`、`icon_id`、`file`、`name`、`description`、`type`。

请求头：`idempotency_key` → `Idempotency-Key`。

请求字段：[TypedDict](../src/qca/forward/types/skill_create_params.py)。类型定义：[FileTypes](../src/qca/common/_types.py)、[NotGiven](../src/qca/common/_types.py)、[Skill](../src/qca/forward/types/skill.py)。

### `skills.retrieve`

`GET /skills/{skill_id}`

```python
def retrieve(
    skill_id: str,
    *,
    include_content: Union[bool, None, NotGiven] = NOT_GIVEN,
) -> Skill: ...
```

调用：`client.skills.retrieve(...)`。实现：[同步](../src/qca/forward/resources/skills/skills.py#L96) / [异步](../src/qca/forward/resources/skills/skills.py#L257)。

路径：`skill_id`。

查询：`include_content`。

请求字段：[TypedDict](../src/qca/forward/types/skill_retrieve_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[Skill](../src/qca/forward/types/skill.py)。

### `skills.update`

`PUT /skills/{skill_id}`

```python
def update(
    skill_id: str,
    *,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    content: Union[str, None, NotGiven] = NOT_GIVEN,
    content_encoding: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    icon_id: Union[str, None, NotGiven] = NOT_GIVEN,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
) -> Skill: ...
```

调用：`client.skills.update(...)`。实现：[同步](../src/qca/forward/resources/skills/skills.py#L119) / [异步](../src/qca/forward/resources/skills/skills.py#L280)。

路径：`skill_id`。

正文：`description`、`content`、`content_encoding`、`metadata`、`icon_id`、`name`。

请求字段：[TypedDict](../src/qca/forward/types/skill_update_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[Skill](../src/qca/forward/types/skill.py)。

### `skills.delete`

`DELETE /skills/{skill_id}`

```python
def delete(
    skill_id: str,
) -> None: ...
```

调用：`client.skills.delete(...)`。实现：[同步](../src/qca/forward/resources/skills/skills.py#L154) / [异步](../src/qca/forward/resources/skills/skills.py#L315)。

路径：`skill_id`。


### `skills.versions.list`

`GET /skills/{skill_id}/versions`

```python
def list(
    skill_id: str,
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
) -> SyncPage[SkillVersion]: ...
```

调用：`client.skills.versions.list(...)`。实现：[同步](../src/qca/forward/resources/skills/versions.py#L19) / [异步](../src/qca/forward/resources/skills/versions.py#L137)。异步返回 `AsyncPaginator[SkillVersion]`。

路径：`skill_id`。

查询：`limit`、`page`。

请求字段：[TypedDict](../src/qca/forward/types/skill_version_list_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[SkillVersion](../src/qca/forward/types/skill_version.py)、[SyncPage](../src/qca/common/pagination.py)。

分页协议：`PageCursor`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

### `skills.versions.create`

`POST /skills/{skill_id}/versions`

```python
def create(
    skill_id: str,
    *,
    files: List[FileTypes],
) -> SkillVersion: ...
```

调用：`client.skills.versions.create(...)`。实现：[同步](../src/qca/forward/resources/skills/versions.py#L43) / [异步](../src/qca/forward/resources/skills/versions.py#L163)。

路径：`skill_id`。

正文：`files`。

请求字段：[TypedDict](../src/qca/forward/types/skill_version_create_params.py)。类型定义：[FileTypes](../src/qca/common/_types.py)、[SkillVersion](../src/qca/forward/types/skill_version.py)。

### `skills.versions.retrieve`

`GET /skills/{skill_id}/versions/{version}`

```python
def retrieve(
    version: str,
    *,
    skill_id: str,
) -> SkillVersion: ...
```

调用：`client.skills.versions.retrieve(...)`。实现：[同步](../src/qca/forward/resources/skills/versions.py#L66) / [异步](../src/qca/forward/resources/skills/versions.py#L186)。

路径：`version`、`skill_id`。

类型定义：[SkillVersion](../src/qca/forward/types/skill_version.py)。

### `skills.versions.delete`

`DELETE /skills/{skill_id}/versions/{version}`

```python
def delete(
    version: str,
    *,
    skill_id: str,
) -> DeletedSkillVersion: ...
```

调用：`client.skills.versions.delete(...)`。实现：[同步](../src/qca/forward/resources/skills/versions.py#L89) / [异步](../src/qca/forward/resources/skills/versions.py#L209)。

路径：`version`、`skill_id`。

类型定义：[DeletedSkillVersion](../src/qca/forward/types/deleted_skill_version.py)。

### `skills.versions.download`

`GET /skills/{skill_id}/versions/{version}/content`

```python
def download(
    version: str,
    *,
    skill_id: str,
) -> BinaryAPIResponse: ...
```

调用：`client.skills.versions.download(...)`。实现：[同步](../src/qca/forward/resources/skills/versions.py#L112) / [异步](../src/qca/forward/resources/skills/versions.py#L232)。异步返回 `AsyncBinaryAPIResponse`。

路径：`version`、`skill_id`。

类型定义：[BinaryAPIResponse](../src/qca/common/_response.py)。

下载返回二进制响应，使用上下文管理器关闭；通过 `write_to_file()` 写入文件。

## templates

管理可复用的模型、工具与环境配置；Identity 使用 Template 创建会话，可克隆或归档模板。

### `templates.list`

`GET /templates`

```python
def list(
    *,
    status: Union[str, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
) -> SyncPage[Template]: ...
```

调用：`client.templates.list(...)`。实现：[同步](../src/qca/forward/resources/templates.py#L24) / [异步](../src/qca/forward/resources/templates.py#L226)。异步返回 `AsyncPaginator[Template]`。

查询：`status`、`limit`、`after_id`、`before_id`。

请求字段：[TypedDict](../src/qca/forward/types/template_list_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[SyncPage](../src/qca/common/pagination.py)、[Template](../src/qca/forward/types/template.py)。

分页协议：`Page`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

### `templates.create`

`POST /templates`

```python
def create(
    *,
    name: str,
    model: Union[str, ModelConfigParam],
    environment_id: str,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    system: Union[str, None, NotGiven] = NOT_GIVEN,
    tools: Union[List[ToolParam], None, NotGiven] = NOT_GIVEN,
    mcp_servers: Union[List[MCPServerParam], None, NotGiven] = NOT_GIVEN,
    skills: Union[List[SkillBindingParam], None, NotGiven] = NOT_GIVEN,
    multiagent: Union[MultiagentConfigParam, None, NotGiven] = NOT_GIVEN,
    vaults: Union[Dict[str, ResourceBindingParam], None, NotGiven] = NOT_GIVEN,
    files: Union[Dict[str, ResourceBindingParam], None, NotGiven] = NOT_GIVEN,
    github_repositories: Union[Dict[str, GitHubRepositoryParam], None, NotGiven] = NOT_GIVEN,
    environment_variables: Union[Union[Dict[str, Any], str], None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
    beta: Union[str, None, NotGiven] = NOT_GIVEN,
) -> Template: ...
```

调用：`client.templates.create(...)`。实现：[同步](../src/qca/forward/resources/templates.py#L49) / [异步](../src/qca/forward/resources/templates.py#L253)。

正文：`name`、`model`、`environment_id`、`description`、`system`、`tools`、`mcp_servers`、`skills`、`multiagent`、`vaults`、`files`、`github_repositories`、`environment_variables`、`metadata`。

请求头：`idempotency_key` → `Idempotency-Key`、`beta` → `X-Qoder-Beta`。

请求字段：[TypedDict](../src/qca/forward/types/template_create_params.py)。类型定义：[GitHubRepositoryParam](../src/qca/forward/types/git_hub_repository_param.py)、[MCPServerParam](../src/qca/forward/types/mcp_server_param.py)、[ModelConfigParam](../src/qca/forward/types/model_config_param.py)、[MultiagentConfigParam](../src/qca/forward/types/multiagent_config_param.py)、[NotGiven](../src/qca/common/_types.py)、[ResourceBindingParam](../src/qca/forward/types/resource_binding_param.py)、[SkillBindingParam](../src/qca/forward/types/skill_binding_param.py)、[Template](../src/qca/forward/types/template.py)、[ToolParam](../src/qca/forward/types/tool_param.py)。

### `templates.retrieve`

`GET /templates/{template_id}`

```python
def retrieve(
    template_id: str,
) -> Template: ...
```

调用：`client.templates.retrieve(...)`。实现：[同步](../src/qca/forward/resources/templates.py#L101) / [异步](../src/qca/forward/resources/templates.py#L305)。

路径：`template_id`。

类型定义：[Template](../src/qca/forward/types/template.py)。

### `templates.update`

`POST /templates/{template_id}`

```python
def update(
    template_id: str,
    *,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    model: Union[Union[str, ModelConfigParam], None, NotGiven] = NOT_GIVEN,
    system: Union[str, None, NotGiven] = NOT_GIVEN,
    tools: Union[List[ToolParam], None, NotGiven] = NOT_GIVEN,
    mcp_servers: Union[List[MCPServerParam], None, NotGiven] = NOT_GIVEN,
    skills: Union[List[SkillBindingParam], None, NotGiven] = NOT_GIVEN,
    multiagent: Union[MultiagentConfigParam, None, NotGiven] = NOT_GIVEN,
    environment_id: Union[str, None, NotGiven] = NOT_GIVEN,
    vaults: Union[Dict[str, ResourceBindingParam], None, NotGiven] = NOT_GIVEN,
    files: Union[Dict[str, ResourceBindingParam], None, NotGiven] = NOT_GIVEN,
    github_repositories: Union[Dict[str, GitHubRepositoryParam], None, NotGiven] = NOT_GIVEN,
    environment_variables: Union[Union[Dict[str, Any], str], None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
    beta: Union[str, None, NotGiven] = NOT_GIVEN,
) -> Template: ...
```

调用：`client.templates.update(...)`。实现：[同步](../src/qca/forward/resources/templates.py#L123) / [异步](../src/qca/forward/resources/templates.py#L327)。

路径：`template_id`。

正文：`name`、`description`、`model`、`system`、`tools`、`mcp_servers`、`skills`、`multiagent`、`environment_id`、`vaults`、`files`、`github_repositories`、`environment_variables`、`metadata`。

请求头：`idempotency_key` → `Idempotency-Key`、`beta` → `X-Qoder-Beta`。

请求字段：[TypedDict](../src/qca/forward/types/template_update_params.py)。类型定义：[GitHubRepositoryParam](../src/qca/forward/types/git_hub_repository_param.py)、[MCPServerParam](../src/qca/forward/types/mcp_server_param.py)、[ModelConfigParam](../src/qca/forward/types/model_config_param.py)、[MultiagentConfigParam](../src/qca/forward/types/multiagent_config_param.py)、[NotGiven](../src/qca/common/_types.py)、[ResourceBindingParam](../src/qca/forward/types/resource_binding_param.py)、[SkillBindingParam](../src/qca/forward/types/skill_binding_param.py)、[Template](../src/qca/forward/types/template.py)、[ToolParam](../src/qca/forward/types/tool_param.py)。

### `templates.archive`

`POST /templates/{template_id}/archive`

```python
def archive(
    template_id: str,
    *,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
) -> Template: ...
```

调用：`client.templates.archive(...)`。实现：[同步](../src/qca/forward/resources/templates.py#L176) / [异步](../src/qca/forward/resources/templates.py#L380)。

路径：`template_id`。

请求头：`idempotency_key` → `Idempotency-Key`。

请求字段：[TypedDict](../src/qca/forward/types/template_archive_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[Template](../src/qca/forward/types/template.py)。

### `templates.clone`

`POST /templates/{template_id}/clone`

```python
def clone(
    template_id: str,
    *,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
) -> Template: ...
```

调用：`client.templates.clone(...)`。实现：[同步](../src/qca/forward/resources/templates.py#L199) / [异步](../src/qca/forward/resources/templates.py#L403)。

路径：`template_id`。

正文：`name`、`description`。

请求头：`idempotency_key` → `Idempotency-Key`。

请求字段：[TypedDict](../src/qca/forward/types/template_clone_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[Template](../src/qca/forward/types/template.py)。

## vaults

管理凭据仓库及仓库中的凭据。参数中可能包含令牌或密钥，业务日志应避免打印请求正文。

### `vaults.list`

`GET /vaults`

```python
def list(
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
) -> SyncPage[Vault]: ...
```

调用：`client.vaults.list(...)`。实现：[同步](../src/qca/forward/resources/vaults/vaults.py#L23) / [异步](../src/qca/forward/resources/vaults/vaults.py#L123)。异步返回 `AsyncPaginator[Vault]`。

查询：`limit`、`page`、`after_id`、`before_id`、`name`。

请求字段：[TypedDict](../src/qca/forward/types/vault_list_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[SyncPage](../src/qca/common/pagination.py)、[Vault](../src/qca/forward/types/vault.py)。

分页协议：`PageCursor`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

### `vaults.create`

`POST /vaults`

```python
def create(
    *,
    display_name: str,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
) -> Vault: ...
```

调用：`client.vaults.create(...)`。实现：[同步](../src/qca/forward/resources/vaults/vaults.py#L49) / [异步](../src/qca/forward/resources/vaults/vaults.py#L151)。

正文：`display_name`、`metadata`。

请求头：`idempotency_key` → `Idempotency-Key`。

请求字段：[TypedDict](../src/qca/forward/types/vault_create_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[Vault](../src/qca/forward/types/vault.py)。

### `vaults.retrieve`

`GET /vaults/{vault_id}`

```python
def retrieve(
    vault_id: str,
) -> Vault: ...
```

调用：`client.vaults.retrieve(...)`。实现：[同步](../src/qca/forward/resources/vaults/vaults.py#L73) / [异步](../src/qca/forward/resources/vaults/vaults.py#L175)。

路径：`vault_id`。

类型定义：[Vault](../src/qca/forward/types/vault.py)。

### `vaults.delete`

`DELETE /vaults/{vault_id}`

```python
def delete(
    vault_id: str,
) -> None: ...
```

调用：`client.vaults.delete(...)`。实现：[同步](../src/qca/forward/resources/vaults/vaults.py#L95) / [异步](../src/qca/forward/resources/vaults/vaults.py#L197)。

路径：`vault_id`。


### `vaults.credentials.list`

`GET /vaults/{vault_id}/credentials`

```python
def list(
    vault_id: str,
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
) -> SyncPage[VaultCredential]: ...
```

调用：`client.vaults.credentials.list(...)`。实现：[同步](../src/qca/forward/resources/vaults/credentials.py#L17) / [异步](../src/qca/forward/resources/vaults/credentials.py#L122)。异步返回 `AsyncPaginator[VaultCredential]`。

路径：`vault_id`。

查询：`limit`、`page`、`after_id`、`before_id`、`name`。

请求字段：[TypedDict](../src/qca/forward/types/vault_credential_list_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[SyncPage](../src/qca/common/pagination.py)、[VaultCredential](../src/qca/forward/types/vault_credential.py)。

分页协议：`PageCursor`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

### `vaults.credentials.create`

`POST /vaults/{vault_id}/credentials`

```python
def create(
    vault_id: str,
    *,
    auth: Dict[str, Any],
    display_name: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
) -> VaultCredential: ...
```

调用：`client.vaults.credentials.create(...)`。实现：[同步](../src/qca/forward/resources/vaults/credentials.py#L44) / [异步](../src/qca/forward/resources/vaults/credentials.py#L153)。

路径：`vault_id`。

正文：`auth`、`display_name`、`metadata`。

请求头：`idempotency_key` → `Idempotency-Key`。

请求字段：[TypedDict](../src/qca/forward/types/vault_credential_create_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[VaultCredential](../src/qca/forward/types/vault_credential.py)。

### `vaults.credentials.retrieve`

`GET /vaults/{vault_id}/credentials/{credential_id}`

```python
def retrieve(
    credential_id: str,
    *,
    vault_id: str,
) -> VaultCredential: ...
```

调用：`client.vaults.credentials.retrieve(...)`。实现：[同步](../src/qca/forward/resources/vaults/credentials.py#L70) / [异步](../src/qca/forward/resources/vaults/credentials.py#L179)。

路径：`credential_id`、`vault_id`。

类型定义：[VaultCredential](../src/qca/forward/types/vault_credential.py)。

### `vaults.credentials.delete`

`DELETE /vaults/{vault_id}/credentials/{credential_id}`

```python
def delete(
    credential_id: str,
    *,
    vault_id: str,
) -> None: ...
```

调用：`client.vaults.credentials.delete(...)`。实现：[同步](../src/qca/forward/resources/vaults/credentials.py#L95) / [异步](../src/qca/forward/resources/vaults/credentials.py#L204)。

路径：`credential_id`、`vault_id`。
