# Managed API 参考

本文覆盖当前 Python SDK 的 **95 个 Managed HTTP 操作**，同步与异步客户端均支持相同资源树。方法与路由依据当前 [资源源码](../src/qca/managed/resources/) 核对。另一种模式见 [Forward API](forward-api.md)。

## 安装、初始化与鉴权

在仓库根目录执行 `python -m pip install .`，要求 Python 3.10+。将账号令牌放入 `QODER_ACCESS_TOKEN`；SDK 不读取 `.env` 文件。

```python
from qca import Managed, AsyncManaged

with Managed() as client:
    for model in client.models.list().data:
        if model.is_enabled:
            print(model.id)
```

也可从 `qca.managed` 导入 `Client` / `AsyncClient`。同步客户端使用 `with` 或 `close()`；异步客户端使用 `async with` 或 `await close()`。构造参数由 [公共客户端](../src/qca/common/_base_client.py) 实现，默认地址由 [Managed 客户端](../src/qca/managed/_client.py) 定义。

| 参数 | 类型和默认行为 |
|---|---|
| `access_token` | `str \| None`；显式值优先，否则读取 `QODER_ACCESS_TOKEN`，作为 Bearer 令牌发送。 |
| `base_url` | `str \| httpx.URL \| None`；显式值优先，否则读取 `QODER_BASE_URL`，默认 `https://api.qoder.com/api/v1/cloud/`。中国站可设为 `https://api.qoder.com.cn/api/v1/cloud/`。 |
| `timeout` | `float \| httpx.Timeout \| None`；单位秒，默认连接阶段 10 秒、其他 HTTP 阶段 60 秒。`None` 关闭 HTTP 超时。 |
| `max_retries` | 非负整数，默认 `2`。 |
| `default_headers` / `default_query` | 分别为 `Mapping[str, str]` / `Mapping[str, Any]`，设定默认请求头和查询参数。 |
| `http_client` | 同步传 `httpx.Client`，异步传 `httpx.AsyncClient`，可配置代理或测试用 transport。 |
| `credential` | [Credential / AsyncCredential](../src/qca/common/credentials.py)；每次 HTTP 尝试调用 `get_token()`。静态令牌优先，显式 `Authorization` 请求头优先级最高。 |

`client.with_options(timeout=20, max_retries=0)` 返回配置独立的客户端，但共享 HTTP 连接池；关闭其中任意客户端会关闭该池。

## 创建会话并读取 SSE

下面片段从当前账号选择已启用模型，再创建会话并发送一条消息。片段会创建资源；包含断言、失败处理与清理的完整实现见 [Managed 场景示例](../examples/managed/)。生产代码应复用同一会话 ID，并在不再需要时清理本次创建的资源。

```python
from uuid import uuid4
from qca import Managed

with Managed() as client:
    model_id = next(model.id for model in client.models.list().data if model.is_enabled)
    environment = client.environments.create(name="docs-example", config={"type": "cloud"})
    agent = client.agents.create(
        name="docs-assistant", model={"id": model_id},
        system="根据可读取的资料回答问题。",
        tools=[{"type": "agent_toolset_20260401"}],
    )
    session = client.sessions.create(environment_id=environment.id, agent=agent.id)
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
from qca import AsyncManaged

async def main():
    async with AsyncManaged() as client:
        async for session in client.sessions.list(limit=20):
            print(session.id)
        page = await client.sessions.list(limit=10)
        print(page.data)

asyncio.run(main())
```

异步 SSE 使用 `async with await client.sessions.events.stream(session_id) as stream:`，内部用 `async for event in stream:`。异步二进制下载使用 `async with await client.files.download(file_id) as response:`，通过 `await response.write_to_file(path)` 保存。

同步分页返回 [SyncPage](../src/qca/common/pagination.py)：

```python
with Managed() as client:
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
with Managed() as client:
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
from qca import Managed

with Managed() as client:
    uploaded = client.files.upload(file=Path("report.txt"))
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
    with Managed() as client:
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
| [agents](#agents) | 6 | 管理 Agent 的模型、系统提示词、工具、Skill、MCP 与版本；会话通过 agent 参数引用 Agent。 |
| [deployments](#deployments) | 8 | 管理 Agent 的持续或定时部署，支持暂停、恢复与手动运行。执行记录位于 deployment_runs。 |
| [deployment_runs](#deployment_runs) | 2 | 列出和读取部署运行，关联会话承载实际执行过程与结果。 |
| [dreams](#dreams) | 5 | 从输入记忆存储创建记忆整理任务，查询运行状态、输出记忆存储，支持取消和归档。 |
| [environments](#environments) | 14 | 管理运行环境。Managed 的 work 子资源还用于自托管执行器轮询任务、确认、心跳和上报结果。 |
| [files](#files) | 5 | 上传和管理文件元数据，按 ID 下载内容。upload 使用 multipart，download 返回需关闭的二进制响应。 |
| [memory_stores](#memory_stores) | 14 | 管理记忆存储、记忆正文与历史版本；Memory Store 通过会话资源挂载后可供助手访问。 |
| [models](#models) | 1 | 获取当前账号的模型列表与启用状态，创建 Agent 或 Template 前可从中选择可用模型。 |
| [sessions](#sessions) | 19 | 创建、查询和管理会话。events 发送输入并读取历史或 SSE；threads 访问子线程，resources 管理挂载资源。 |
| [skills](#skills) | 9 | 上传 Skill 文件并管理版本；版本下载返回二进制响应。Skill 路径会保留在 multipart 文件名中。 |
| [vaults](#vaults) | 12 | 管理凭据仓库及仓库中的凭据。参数中可能包含令牌或密钥，业务日志应避免打印请求正文。 |

## agents

管理 Agent 的模型、系统提示词、工具、Skill、MCP 与版本；会话通过 agent 参数引用 Agent。

### `agents.create`

`POST /agents`

```python
def create(
    *,
    model: Union[str, ModelConfigParams],
    name: str,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    system: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    mcp_servers: Union[List[URLMCPServerParams], None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
    multiagent: Union[MultiagentParams, None, NotGiven] = NOT_GIVEN,
    skills: Union[List[Union[QoderSkillParams, CustomSkillParams]], None, NotGiven] = NOT_GIVEN,
    tools: Union[List[Union[AgentToolset20260401Params, MCPToolsetParams, CustomToolParams]], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> Agent: ...
```

调用：`client.agents.create(...)`。实现：[同步](../src/qca/managed/resources/agents/agents.py#L32) / [异步](../src/qca/managed/resources/agents/agents.py#L212)。

正文：`model`、`name`、`description`、`system`、`mcp_servers`、`metadata`、`multiagent`、`skills`、`tools`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/agent_create_params.py)。类型定义：[Agent](../src/qca/managed/types/agent.py)、[AgentToolset20260401Params](../src/qca/managed/types/agent_toolset20260401_params.py)、[CustomSkillParams](../src/qca/managed/types/custom_skill_params.py)、[CustomToolParams](../src/qca/managed/types/custom_tool_params.py)、[MCPToolsetParams](../src/qca/managed/types/mcp_toolset_params.py)、[ModelConfigParams](../src/qca/managed/types/model_config_params.py)、[MultiagentParams](../src/qca/managed/types/multiagent_params.py)、[NotGiven](../src/qca/common/_types.py)、[QoderSkillParams](../src/qca/managed/types/qoder_skill_params.py)、[URLMCPServerParams](../src/qca/managed/types/urlmcp_server_params.py)。

### `agents.retrieve`

`GET /agents/{agent_id}`

```python
def retrieve(
    agent_id: str,
    *,
    version: Union[int, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> Agent: ...
```

调用：`client.agents.retrieve(...)`。实现：[同步](../src/qca/managed/resources/agents/agents.py#L76) / [异步](../src/qca/managed/resources/agents/agents.py#L256)。

路径：`agent_id`。

查询：`version`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/agent_retrieve_params.py)。类型定义：[Agent](../src/qca/managed/types/agent.py)、[NotGiven](../src/qca/common/_types.py)。

### `agents.update`

`POST /agents/{agent_id}`

```python
def update(
    agent_id: str,
    *,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    system: Union[str, None, NotGiven] = NOT_GIVEN,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    version: Union[int, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    mcp_servers: Union[List[URLMCPServerParams], None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    skills: Union[List[Union[QoderSkillParams, CustomSkillParams]], None, NotGiven] = NOT_GIVEN,
    tools: Union[List[Union[AgentToolset20260401Params, MCPToolsetParams, CustomToolParams]], None, NotGiven] = NOT_GIVEN,
    model: Union[Union[str, ModelConfigParams], None, NotGiven] = NOT_GIVEN,
    multiagent: Union[MultiagentParams, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> Agent: ...
```

调用：`client.agents.update(...)`。实现：[同步](../src/qca/managed/resources/agents/agents.py#L101) / [异步](../src/qca/managed/resources/agents/agents.py#L281)。

路径：`agent_id`。

正文：`description`、`system`、`name`、`version`、`mcp_servers`、`metadata`、`skills`、`tools`、`model`、`multiagent`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/agent_update_params.py)。类型定义：[Agent](../src/qca/managed/types/agent.py)、[AgentToolset20260401Params](../src/qca/managed/types/agent_toolset20260401_params.py)、[CustomSkillParams](../src/qca/managed/types/custom_skill_params.py)、[CustomToolParams](../src/qca/managed/types/custom_tool_params.py)、[MCPToolsetParams](../src/qca/managed/types/mcp_toolset_params.py)、[ModelConfigParams](../src/qca/managed/types/model_config_params.py)、[MultiagentParams](../src/qca/managed/types/multiagent_params.py)、[NotGiven](../src/qca/common/_types.py)、[QoderSkillParams](../src/qca/managed/types/qoder_skill_params.py)、[URLMCPServerParams](../src/qca/managed/types/urlmcp_server_params.py)。

### `agents.list`

`GET /agents`

```python
def list(
    *,
    created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> SyncPage[Agent]: ...
```

调用：`client.agents.list(...)`。实现：[同步](../src/qca/managed/resources/agents/agents.py#L148) / [异步](../src/qca/managed/resources/agents/agents.py#L328)。异步返回 `AsyncPaginator[Agent]`。

查询：`created_at_gte` → `created_at[gte]`、`created_at_lte` → `created_at[lte]`、`include_archived`、`limit`、`page`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/agent_list_params.py)。类型定义：[Agent](../src/qca/managed/types/agent.py)、[NotGiven](../src/qca/common/_types.py)、[SyncPage](../src/qca/common/pagination.py)。

分页协议：`PageCursor`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

### `agents.archive`

`POST /agents/{agent_id}/archive`

```python
def archive(
    agent_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> Agent: ...
```

调用：`client.agents.archive(...)`。实现：[同步](../src/qca/managed/resources/agents/agents.py#L182) / [异步](../src/qca/managed/resources/agents/agents.py#L364)。

路径：`agent_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/agent_archive_params.py)。类型定义：[Agent](../src/qca/managed/types/agent.py)、[NotGiven](../src/qca/common/_types.py)。

### `agents.versions.list`

`GET /agents/{agent_id}/versions`

```python
def list(
    agent_id: str,
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> SyncPage[Agent]: ...
```

调用：`client.agents.versions.list(...)`。实现：[同步](../src/qca/managed/resources/agents/versions.py#L17) / [异步](../src/qca/managed/resources/agents/versions.py#L45)。异步返回 `AsyncPaginator[Agent]`。

路径：`agent_id`。

查询：`limit`、`page`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/agent_version_list_params.py)。类型定义：[Agent](../src/qca/managed/types/agent.py)、[NotGiven](../src/qca/common/_types.py)、[SyncPage](../src/qca/common/pagination.py)。

分页协议：`PageCursor`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

## deployments

管理 Agent 的持续或定时部署，支持暂停、恢复与手动运行。执行记录位于 deployment_runs。

### `deployments.create`

`POST /deployments`

```python
def create(
    *,
    agent: Union[str, AgentParams],
    environment_id: str,
    initial_events: List[Union[UserMessageEventParams, UserDefineOutcomeEventParams, SystemMessageEventParams]],
    name: str,
    environment_variables: Union[str, None, NotGiven] = NOT_GIVEN,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    budget: Union[BudgetLimitParam, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
    resources: Union[List[Union[GitHubRepositoryResourceParams, FileResourceParams, MemoryStoreResourceParam]], None, NotGiven] = NOT_GIVEN,
    schedule: Union[ScheduleParams, None, NotGiven] = NOT_GIVEN,
    vault_ids: Union[List[str], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> Deployment: ...
```

调用：`client.deployments.create(...)`。实现：[同步](../src/qca/managed/resources/deployments.py#L28) / [异步](../src/qca/managed/resources/deployments.py#L291)。

正文：`environment_variables`、`agent`、`environment_id`、`initial_events`、`name`、`description`、`budget`、`metadata`、`resources`、`schedule`、`vault_ids`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/deployment_create_params.py)。类型定义：[AgentParams](../src/qca/managed/types/agent_params.py)、[BudgetLimitParam](../src/qca/managed/types/budget_limit_param.py)、[Deployment](../src/qca/managed/types/deployment.py)、[FileResourceParams](../src/qca/managed/types/file_resource_params.py)、[GitHubRepositoryResourceParams](../src/qca/managed/types/git_hub_repository_resource_params.py)、[MemoryStoreResourceParam](../src/qca/managed/types/memory_store_resource_param.py)、[NotGiven](../src/qca/common/_types.py)、[ScheduleParams](../src/qca/managed/types/schedule_params.py)、[SystemMessageEventParams](../src/qca/managed/types/system_message_event_params.py)、[UserDefineOutcomeEventParams](../src/qca/managed/types/user_define_outcome_event_params.py)、[UserMessageEventParams](../src/qca/managed/types/user_message_event_params.py)。

### `deployments.retrieve`

`GET /deployments/{deployment_id}`

```python
def retrieve(
    deployment_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> Deployment: ...
```

调用：`client.deployments.retrieve(...)`。实现：[同步](../src/qca/managed/resources/deployments.py#L76) / [异步](../src/qca/managed/resources/deployments.py#L339)。

路径：`deployment_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/deployment_retrieve_params.py)。类型定义：[Deployment](../src/qca/managed/types/deployment.py)、[NotGiven](../src/qca/common/_types.py)。

### `deployments.update`

`POST /deployments/{deployment_id}`

```python
def update(
    deployment_id: str,
    *,
    environment_variables: Union[str, None, NotGiven] = NOT_GIVEN,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    environment_id: Union[str, None, NotGiven] = NOT_GIVEN,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    resources: Union[List[Union[GitHubRepositoryResourceParams, FileResourceParams, MemoryStoreResourceParam]], None, NotGiven] = NOT_GIVEN,
    vault_ids: Union[List[str], None, NotGiven] = NOT_GIVEN,
    agent: Union[Union[str, AgentParams], None, NotGiven] = NOT_GIVEN,
    budget: Union[BudgetLimitParam, None, NotGiven] = NOT_GIVEN,
    initial_events: Union[List[Union[UserMessageEventParams, UserDefineOutcomeEventParams, SystemMessageEventParams]], None, NotGiven] = NOT_GIVEN,
    schedule: Union[ScheduleParams, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> Deployment: ...
```

调用：`client.deployments.update(...)`。实现：[同步](../src/qca/managed/resources/deployments.py#L100) / [异步](../src/qca/managed/resources/deployments.py#L363)。

路径：`deployment_id`。

正文：`environment_variables`、`description`、`environment_id`、`name`、`metadata`、`resources`、`vault_ids`、`agent`、`budget`、`initial_events`、`schedule`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/deployment_update_params.py)。类型定义：[AgentParams](../src/qca/managed/types/agent_params.py)、[BudgetLimitParam](../src/qca/managed/types/budget_limit_param.py)、[Deployment](../src/qca/managed/types/deployment.py)、[FileResourceParams](../src/qca/managed/types/file_resource_params.py)、[GitHubRepositoryResourceParams](../src/qca/managed/types/git_hub_repository_resource_params.py)、[MemoryStoreResourceParam](../src/qca/managed/types/memory_store_resource_param.py)、[NotGiven](../src/qca/common/_types.py)、[ScheduleParams](../src/qca/managed/types/schedule_params.py)、[SystemMessageEventParams](../src/qca/managed/types/system_message_event_params.py)、[UserDefineOutcomeEventParams](../src/qca/managed/types/user_define_outcome_event_params.py)、[UserMessageEventParams](../src/qca/managed/types/user_message_event_params.py)。

### `deployments.list`

`GET /deployments`

```python
def list(
    *,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    agent_id: Union[str, None, NotGiven] = NOT_GIVEN,
    created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    status: Union[Literal['active', 'paused'], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> SyncPage[Deployment]: ...
```

调用：`client.deployments.list(...)`。实现：[同步](../src/qca/managed/resources/deployments.py#L151) / [异步](../src/qca/managed/resources/deployments.py#L414)。异步返回 `AsyncPaginator[Deployment]`。

查询：`before_id`、`after_id`、`agent_id`、`created_at_gte` → `created_at[gte]`、`created_at_lte` → `created_at[lte]`、`include_archived`、`limit`、`page`、`status`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/deployment_list_params.py)。类型定义：[Deployment](../src/qca/managed/types/deployment.py)、[NotGiven](../src/qca/common/_types.py)、[SyncPage](../src/qca/common/pagination.py)。

分页协议：`PageCursor`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

### `deployments.archive`

`POST /deployments/{deployment_id}/archive`

```python
def archive(
    deployment_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> Deployment: ...
```

调用：`client.deployments.archive(...)`。实现：[同步](../src/qca/managed/resources/deployments.py#L193) / [异步](../src/qca/managed/resources/deployments.py#L458)。

路径：`deployment_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/deployment_archive_params.py)。类型定义：[Deployment](../src/qca/managed/types/deployment.py)、[NotGiven](../src/qca/common/_types.py)。

### `deployments.pause`

`POST /deployments/{deployment_id}/pause`

```python
def pause(
    deployment_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> Deployment: ...
```

调用：`client.deployments.pause(...)`。实现：[同步](../src/qca/managed/resources/deployments.py#L217) / [异步](../src/qca/managed/resources/deployments.py#L482)。

路径：`deployment_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/deployment_pause_params.py)。类型定义：[Deployment](../src/qca/managed/types/deployment.py)、[NotGiven](../src/qca/common/_types.py)。

### `deployments.run`

`POST /deployments/{deployment_id}/run`

```python
def run(
    deployment_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> DeploymentRun: ...
```

调用：`client.deployments.run(...)`。实现：[同步](../src/qca/managed/resources/deployments.py#L241) / [异步](../src/qca/managed/resources/deployments.py#L506)。

路径：`deployment_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/deployment_run_params.py)。类型定义：[DeploymentRun](../src/qca/managed/types/deployment_run.py)、[NotGiven](../src/qca/common/_types.py)。

### `deployments.unpause`

`POST /deployments/{deployment_id}/unpause`

```python
def unpause(
    deployment_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> Deployment: ...
```

调用：`client.deployments.unpause(...)`。实现：[同步](../src/qca/managed/resources/deployments.py#L265) / [异步](../src/qca/managed/resources/deployments.py#L530)。

路径：`deployment_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/deployment_unpause_params.py)。类型定义：[Deployment](../src/qca/managed/types/deployment.py)、[NotGiven](../src/qca/common/_types.py)。

## deployment_runs

列出和读取部署运行，关联会话承载实际执行过程与结果。

### `deployment_runs.retrieve`

`GET /deployment_runs/{deployment_run_id}`

```python
def retrieve(
    deployment_run_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> DeploymentRun: ...
```

调用：`client.deployment_runs.retrieve(...)`。实现：[同步](../src/qca/managed/resources/deployment_runs.py#L18) / [异步](../src/qca/managed/resources/deployment_runs.py#L90)。

路径：`deployment_run_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/deployment_run_retrieve_params.py)。类型定义：[DeploymentRun](../src/qca/managed/types/deployment_run.py)、[NotGiven](../src/qca/common/_types.py)。

### `deployment_runs.list`

`GET /deployment_runs`

```python
def list(
    *,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    created_at_gt: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lt: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    deployment_id: Union[str, None, NotGiven] = NOT_GIVEN,
    has_error: Union[bool, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    trigger_type: Union[Literal['schedule', 'manual'], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> SyncPage[DeploymentRun]: ...
```

调用：`client.deployment_runs.list(...)`。实现：[同步](../src/qca/managed/resources/deployment_runs.py#L42) / [异步](../src/qca/managed/resources/deployment_runs.py#L114)。异步返回 `AsyncPaginator[DeploymentRun]`。

查询：`before_id`、`after_id`、`created_at_gt` → `created_at[gt]`、`created_at_gte` → `created_at[gte]`、`created_at_lt` → `created_at[lt]`、`created_at_lte` → `created_at[lte]`、`deployment_id`、`has_error`、`limit`、`page`、`trigger_type`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/deployment_run_list_params.py)。类型定义：[DeploymentRun](../src/qca/managed/types/deployment_run.py)、[NotGiven](../src/qca/common/_types.py)、[SyncPage](../src/qca/common/pagination.py)。

分页协议：`PageCursor`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

## dreams

从输入记忆存储创建记忆整理任务，查询运行状态、输出记忆存储，支持取消和归档。

### `dreams.create`

`POST /dreams`

```python
def create(
    *,
    inputs: List[Union[DreamMemoryStoreInputParam, DreamSessionsInputParam]],
    model: Union[str, DreamModelConfigParam],
    instructions: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    output_behavior: Union[Union[OutputBehaviorCreateNewParam, OutputBehaviorUpdateExistingParam], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> Dream: ...
```

调用：`client.dreams.create(...)`。实现：[同步](../src/qca/managed/resources/dreams.py#L23) / [异步](../src/qca/managed/resources/dreams.py#L164)。

正文：`inputs`、`model`、`instructions`、`output_behavior`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/dream_create_params.py)。类型定义：[Dream](../src/qca/managed/types/dream.py)、[DreamMemoryStoreInputParam](../src/qca/managed/types/dream_memory_store_input_param.py)、[DreamModelConfigParam](../src/qca/managed/types/dream_model_config_param.py)、[DreamSessionsInputParam](../src/qca/managed/types/dream_sessions_input_param.py)、[NotGiven](../src/qca/common/_types.py)、[OutputBehaviorCreateNewParam](../src/qca/managed/types/output_behavior_create_new_param.py)、[OutputBehaviorUpdateExistingParam](../src/qca/managed/types/output_behavior_update_existing_param.py)。

### `dreams.retrieve`

`GET /dreams/{dream_id}`

```python
def retrieve(
    dream_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> Dream: ...
```

调用：`client.dreams.retrieve(...)`。实现：[同步](../src/qca/managed/resources/dreams.py#L52) / [异步](../src/qca/managed/resources/dreams.py#L193)。

路径：`dream_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/dream_retrieve_params.py)。类型定义：[Dream](../src/qca/managed/types/dream.py)、[NotGiven](../src/qca/common/_types.py)。

### `dreams.list`

`GET /dreams`

```python
def list(
    *,
    created_at_gt: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lt: Union[datetime, None, NotGiven] = NOT_GIVEN,
    include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    statuses: Union[List[Literal['pending', 'running', 'completed', 'failed', 'canceled']], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> SyncPage[Dream]: ...
```

调用：`client.dreams.list(...)`。实现：[同步](../src/qca/managed/resources/dreams.py#L76) / [异步](../src/qca/managed/resources/dreams.py#L217)。异步返回 `AsyncPaginator[Dream]`。

查询：`created_at_gt` → `created_at[gt]`、`created_at_lt` → `created_at[lt]`、`include_archived`、`limit`、`page`、`statuses` → `statuses[]`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/dream_list_params.py)。类型定义：[Dream](../src/qca/managed/types/dream.py)、[NotGiven](../src/qca/common/_types.py)、[SyncPage](../src/qca/common/pagination.py)。

分页协议：`PageCursor`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

### `dreams.archive`

`POST /dreams/{dream_id}/archive`

```python
def archive(
    dream_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> Dream: ...
```

调用：`client.dreams.archive(...)`。实现：[同步](../src/qca/managed/resources/dreams.py#L114) / [异步](../src/qca/managed/resources/dreams.py#L257)。

路径：`dream_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/dream_archive_params.py)。类型定义：[Dream](../src/qca/managed/types/dream.py)、[NotGiven](../src/qca/common/_types.py)。

### `dreams.cancel`

`POST /dreams/{dream_id}/cancel`

```python
def cancel(
    dream_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> Dream: ...
```

调用：`client.dreams.cancel(...)`。实现：[同步](../src/qca/managed/resources/dreams.py#L138) / [异步](../src/qca/managed/resources/dreams.py#L281)。

路径：`dream_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/dream_cancel_params.py)。类型定义：[Dream](../src/qca/managed/types/dream.py)、[NotGiven](../src/qca/common/_types.py)。

## environments

管理运行环境。Managed 的 work 子资源还用于自托管执行器轮询任务、确认、心跳和上报结果。

### `environments.create`

`POST /environments`

```python
def create(
    *,
    name: str,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    config: Union[Union[CloudConfigParams, SelfHostedConfigParams], None, NotGiven] = NOT_GIVEN,
    scope: Union[Literal['organization', 'account'], None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> Environment: ...
```

调用：`client.environments.create(...)`。实现：[同步](../src/qca/managed/resources/environments/environments.py#L27) / [异步](../src/qca/managed/resources/environments/environments.py#L196)。

正文：`name`、`description`、`config`、`scope`、`metadata`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/environment_create_params.py)。类型定义：[CloudConfigParams](../src/qca/managed/types/cloud_config_params.py)、[Environment](../src/qca/managed/types/environment.py)、[NotGiven](../src/qca/common/_types.py)、[SelfHostedConfigParams](../src/qca/managed/types/self_hosted_config_params.py)。

### `environments.retrieve`

`GET /environments/{environment_id}`

```python
def retrieve(
    environment_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> Environment: ...
```

调用：`client.environments.retrieve(...)`。实现：[同步](../src/qca/managed/resources/environments/environments.py#L55) / [异步](../src/qca/managed/resources/environments/environments.py#L224)。

路径：`environment_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/environment_retrieve_params.py)。类型定义：[Environment](../src/qca/managed/types/environment.py)、[NotGiven](../src/qca/common/_types.py)。

### `environments.update`

`POST /environments/{environment_id}`

```python
def update(
    environment_id: str,
    *,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    config: Union[Union[CloudConfigParams, SelfHostedConfigParams], None, NotGiven] = NOT_GIVEN,
    scope: Union[Literal['organization', 'account'], None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> Environment: ...
```

调用：`client.environments.update(...)`。实现：[同步](../src/qca/managed/resources/environments/environments.py#L79) / [异步](../src/qca/managed/resources/environments/environments.py#L248)。

路径：`environment_id`。

正文：`description`、`name`、`config`、`scope`、`metadata`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/environment_update_params.py)。类型定义：[CloudConfigParams](../src/qca/managed/types/cloud_config_params.py)、[Environment](../src/qca/managed/types/environment.py)、[NotGiven](../src/qca/common/_types.py)、[SelfHostedConfigParams](../src/qca/managed/types/self_hosted_config_params.py)。

### `environments.list`

`GET /environments`

```python
def list(
    *,
    created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> SyncPage[Environment]: ...
```

调用：`client.environments.list(...)`。实现：[同步](../src/qca/managed/resources/environments/environments.py#L108) / [异步](../src/qca/managed/resources/environments/environments.py#L277)。异步返回 `AsyncPaginator[Environment]`。

查询：`created_at_gte` → `created_at[gte]`、`created_at_lte` → `created_at[lte]`、`page`、`include_archived`、`limit`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/environment_list_params.py)。类型定义：[Environment](../src/qca/managed/types/environment.py)、[NotGiven](../src/qca/common/_types.py)、[SyncPage](../src/qca/common/pagination.py)。

分页协议：`PageCursor`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

### `environments.delete`

`DELETE /environments/{environment_id}`

```python
def delete(
    environment_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> EnvironmentDeleteResponse: ...
```

调用：`client.environments.delete(...)`。实现：[同步](../src/qca/managed/resources/environments/environments.py#L142) / [异步](../src/qca/managed/resources/environments/environments.py#L313)。

路径：`environment_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/environment_delete_params.py)。类型定义：[EnvironmentDeleteResponse](../src/qca/managed/types/environment_delete_response.py)、[NotGiven](../src/qca/common/_types.py)。

### `environments.archive`

`POST /environments/{environment_id}/archive`

```python
def archive(
    environment_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> Environment: ...
```

调用：`client.environments.archive(...)`。实现：[同步](../src/qca/managed/resources/environments/environments.py#L166) / [异步](../src/qca/managed/resources/environments/environments.py#L337)。

路径：`environment_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/environment_archive_params.py)。类型定义：[Environment](../src/qca/managed/types/environment.py)、[NotGiven](../src/qca/common/_types.py)。

### `environments.work.retrieve`

`GET /environments/{environment_id}/work/{work_id}`

```python
def retrieve(
    work_id: str,
    *,
    environment_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> SelfHostedWork: ...
```

调用：`client.environments.work.retrieve(...)`。实现：[同步](../src/qca/managed/resources/environments/work.py#L19) / [异步](../src/qca/managed/resources/environments/work.py#L235)。

路径：`work_id`、`environment_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/environment_work_retrieve_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[SelfHostedWork](../src/qca/managed/types/self_hosted_work.py)。

### `environments.work.update`

`POST /environments/{environment_id}/work/{work_id}`

```python
def update(
    work_id: str,
    *,
    environment_id: str,
    metadata: Dict[str, Any],
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> SelfHostedWork: ...
```

调用：`client.environments.work.update(...)`。实现：[同步](../src/qca/managed/resources/environments/work.py#L46) / [异步](../src/qca/managed/resources/environments/work.py#L262)。

路径：`work_id`、`environment_id`。

正文：`metadata`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/environment_work_update_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[SelfHostedWork](../src/qca/managed/types/self_hosted_work.py)。

### `environments.work.list`

`GET /environments/{environment_id}/work`

```python
def list(
    environment_id: str,
    *,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> SyncPage[SelfHostedWork]: ...
```

调用：`client.environments.work.list(...)`。实现：[同步](../src/qca/managed/resources/environments/work.py#L74) / [异步](../src/qca/managed/resources/environments/work.py#L290)。异步返回 `AsyncPaginator[SelfHostedWork]`。

路径：`environment_id`。

查询：`before_id`、`after_id`、`page`、`limit`。

请求头：`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/environment_work_list_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[SelfHostedWork](../src/qca/managed/types/self_hosted_work.py)、[SyncPage](../src/qca/common/pagination.py)。

分页协议：`PageCursor`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

### `environments.work.ack`

`POST /environments/{environment_id}/work/{work_id}/ack`

```python
def ack(
    work_id: str,
    *,
    environment_id: str,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> SelfHostedWork: ...
```

调用：`client.environments.work.ack(...)`。实现：[同步](../src/qca/managed/resources/environments/work.py#L101) / [异步](../src/qca/managed/resources/environments/work.py#L319)。

路径：`work_id`、`environment_id`。

请求头：`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/environment_work_ack_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[SelfHostedWork](../src/qca/managed/types/self_hosted_work.py)。

### `environments.work.heartbeat`

`POST /environments/{environment_id}/work/{work_id}/heartbeat`

```python
def heartbeat(
    work_id: str,
    *,
    environment_id: str,
    desired_ttl_seconds: Union[int, None, NotGiven] = NOT_GIVEN,
    expected_last_heartbeat: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> SelfHostedWorkHeartbeatResponse: ...
```

调用：`client.environments.work.heartbeat(...)`。实现：[同步](../src/qca/managed/resources/environments/work.py#L127) / [异步](../src/qca/managed/resources/environments/work.py#L345)。

路径：`work_id`、`environment_id`。

查询：`desired_ttl_seconds`、`expected_last_heartbeat`。

请求头：`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/environment_work_heartbeat_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[SelfHostedWorkHeartbeatResponse](../src/qca/managed/types/self_hosted_work_heartbeat_response.py)。

### `environments.work.poll`

`GET /environments/{environment_id}/work/poll`

```python
def poll(
    environment_id: str,
    *,
    block_ms: Union[int, None, NotGiven] = NOT_GIVEN,
    reclaim_older_than_ms: Union[int, None, NotGiven] = NOT_GIVEN,
    worker_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> Optional[SelfHostedWork]: ...
```

调用：`client.environments.work.poll(...)`。实现：[同步](../src/qca/managed/resources/environments/work.py#L155) / [异步](../src/qca/managed/resources/environments/work.py#L373)。

路径：`environment_id`。

查询：`block_ms`、`reclaim_older_than_ms`。

请求头：`worker_id` → `Worker-ID`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/environment_work_poll_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[SelfHostedWork](../src/qca/managed/types/self_hosted_work.py)。

### `environments.work.stats`

`GET /environments/{environment_id}/work/stats`

```python
def stats(
    environment_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> SelfHostedWorkQueueStats: ...
```

调用：`client.environments.work.stats(...)`。实现：[同步](../src/qca/managed/resources/environments/work.py#L181) / [异步](../src/qca/managed/resources/environments/work.py#L399)。

路径：`environment_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/environment_work_stats_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[SelfHostedWorkQueueStats](../src/qca/managed/types/self_hosted_work_queue_stats.py)。

### `environments.work.stop`

`POST /environments/{environment_id}/work/{work_id}/stop`

```python
def stop(
    work_id: str,
    *,
    environment_id: str,
    force: Union[bool, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> SelfHostedWork: ...
```

调用：`client.environments.work.stop(...)`。实现：[同步](../src/qca/managed/resources/environments/work.py#L205) / [异步](../src/qca/managed/resources/environments/work.py#L423)。

路径：`work_id`、`environment_id`。

正文：`force`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/environment_work_stop_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[SelfHostedWork](../src/qca/managed/types/self_hosted_work.py)。

## files

上传和管理文件元数据，按 ID 下载内容。upload 使用 multipart，download 返回需关闭的二进制响应。

### `files.list`

`GET /files`

```python
def list(
    *,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    scope_id: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    i_ds: Union[List[str], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> SyncPage[FileMetadata]: ...
```

调用：`client.files.list(...)`。实现：[同步](../src/qca/managed/resources/files.py#L19) / [异步](../src/qca/managed/resources/files.py#L158)。异步返回 `AsyncPaginator[FileMetadata]`。

查询：`name`、`before_id`、`after_id`、`page`、`limit`、`scope_id`、`i_ds` → `ids[]`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/file_list_params.py)。类型定义：[FileMetadata](../src/qca/managed/types/file_metadata.py)、[NotGiven](../src/qca/common/_types.py)、[SyncPage](../src/qca/common/pagination.py)。

分页协议：`PageCursor`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

### `files.delete`

`DELETE /files/{file_id}`

```python
def delete(
    file_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> DeletedFile: ...
```

调用：`client.files.delete(...)`。实现：[同步](../src/qca/managed/resources/files.py#L57) / [异步](../src/qca/managed/resources/files.py#L198)。

路径：`file_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/file_delete_params.py)。类型定义：[DeletedFile](../src/qca/managed/types/deleted_file.py)、[NotGiven](../src/qca/common/_types.py)。

### `files.download`

`GET /files/{file_id}/content`

```python
def download(
    file_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> BinaryAPIResponse: ...
```

调用：`client.files.download(...)`。实现：[同步](../src/qca/managed/resources/files.py#L81) / [异步](../src/qca/managed/resources/files.py#L222)。异步返回 `AsyncBinaryAPIResponse`。

路径：`file_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/file_download_params.py)。类型定义：[BinaryAPIResponse](../src/qca/common/_response.py)、[NotGiven](../src/qca/common/_types.py)。

下载返回二进制响应，使用上下文管理器关闭；通过 `write_to_file()` 写入文件。

### `files.retrieve_metadata`

`GET /files/{file_id}`

```python
def retrieve_metadata(
    file_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> FileMetadata: ...
```

调用：`client.files.retrieve_metadata(...)`。实现：[同步](../src/qca/managed/resources/files.py#L105) / [异步](../src/qca/managed/resources/files.py#L246)。

路径：`file_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

类型定义：[FileMetadata](../src/qca/managed/types/file_metadata.py)、[NotGiven](../src/qca/common/_types.py)。

### `files.upload`

`POST /files`

```python
def upload(
    *,
    file: FileTypes,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
    expires_in_seconds: Union[int, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> FileMetadata: ...
```

调用：`client.files.upload(...)`。实现：[同步](../src/qca/managed/resources/files.py#L129) / [异步](../src/qca/managed/resources/files.py#L270)。

正文：`name`、`metadata`、`file`、`expires_in_seconds`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/file_upload_params.py)。类型定义：[FileMetadata](../src/qca/managed/types/file_metadata.py)、[FileTypes](../src/qca/common/_types.py)、[NotGiven](../src/qca/common/_types.py)。

## memory_stores

管理记忆存储、记忆正文与历史版本；Memory Store 通过会话资源挂载后可供助手访问。

### `memory_stores.create`

`POST /memory_stores`

```python
def create(
    *,
    name: str,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> MemoryStore: ...
```

调用：`client.memory_stores.create(...)`。实现：[同步](../src/qca/managed/resources/memory_stores/memory_stores.py#L30) / [异步](../src/qca/managed/resources/memory_stores/memory_stores.py#L201)。

正文：`name`、`description`、`metadata`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/memory_store_create_params.py)。类型定义：[MemoryStore](../src/qca/managed/types/memory_store.py)、[NotGiven](../src/qca/common/_types.py)。

### `memory_stores.retrieve`

`GET /memory_stores/{memory_store_id}`

```python
def retrieve(
    memory_store_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> MemoryStore: ...
```

调用：`client.memory_stores.retrieve(...)`。实现：[同步](../src/qca/managed/resources/memory_stores/memory_stores.py#L56) / [异步](../src/qca/managed/resources/memory_stores/memory_stores.py#L227)。

路径：`memory_store_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/memory_store_retrieve_params.py)。类型定义：[MemoryStore](../src/qca/managed/types/memory_store.py)、[NotGiven](../src/qca/common/_types.py)。

### `memory_stores.update`

`POST /memory_stores/{memory_store_id}`

```python
def update(
    memory_store_id: str,
    *,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> MemoryStore: ...
```

调用：`client.memory_stores.update(...)`。实现：[同步](../src/qca/managed/resources/memory_stores/memory_stores.py#L80) / [异步](../src/qca/managed/resources/memory_stores/memory_stores.py#L251)。

路径：`memory_store_id`。

正文：`description`、`name`、`metadata`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/memory_store_update_params.py)。类型定义：[MemoryStore](../src/qca/managed/types/memory_store.py)、[NotGiven](../src/qca/common/_types.py)。

### `memory_stores.list`

`GET /memory_stores`

```python
def list(
    *,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> SyncPage[MemoryStore]: ...
```

调用：`client.memory_stores.list(...)`。实现：[同步](../src/qca/managed/resources/memory_stores/memory_stores.py#L107) / [异步](../src/qca/managed/resources/memory_stores/memory_stores.py#L278)。异步返回 `AsyncPaginator[MemoryStore]`。

查询：`name`、`created_at_gte` → `created_at[gte]`、`created_at_lte` → `created_at[lte]`、`include_archived`、`limit`、`page`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/memory_store_list_params.py)。类型定义：[MemoryStore](../src/qca/managed/types/memory_store.py)、[NotGiven](../src/qca/common/_types.py)、[SyncPage](../src/qca/common/pagination.py)。

分页协议：`PageCursor`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

### `memory_stores.delete`

`DELETE /memory_stores/{memory_store_id}`

```python
def delete(
    memory_store_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> DeletedMemoryStore: ...
```

调用：`client.memory_stores.delete(...)`。实现：[同步](../src/qca/managed/resources/memory_stores/memory_stores.py#L143) / [异步](../src/qca/managed/resources/memory_stores/memory_stores.py#L316)。

路径：`memory_store_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/memory_store_delete_params.py)。类型定义：[DeletedMemoryStore](../src/qca/managed/types/deleted_memory_store.py)、[NotGiven](../src/qca/common/_types.py)。

### `memory_stores.archive`

`POST /memory_stores/{memory_store_id}/archive`

```python
def archive(
    memory_store_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> MemoryStore: ...
```

调用：`client.memory_stores.archive(...)`。实现：[同步](../src/qca/managed/resources/memory_stores/memory_stores.py#L167) / [异步](../src/qca/managed/resources/memory_stores/memory_stores.py#L340)。

路径：`memory_store_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/memory_store_archive_params.py)。类型定义：[MemoryStore](../src/qca/managed/types/memory_store.py)、[NotGiven](../src/qca/common/_types.py)。

### `memory_stores.memories.create`

`POST /memory_stores/{memory_store_id}/memories`

```python
def create(
    memory_store_id: str,
    *,
    content: str,
    path: str,
    metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    view: Union[Literal['basic', 'full'], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> Memory: ...
```

调用：`client.memory_stores.memories.create(...)`。实现：[同步](../src/qca/managed/resources/memory_stores/memories.py#L34) / [异步](../src/qca/managed/resources/memory_stores/memories.py#L196)。

路径：`memory_store_id`。

正文：`metadata`、`content`、`path`。

查询：`view`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/memory_store_memory_create_params.py)。类型定义：[Memory](../src/qca/managed/types/memory.py)、[NotGiven](../src/qca/common/_types.py)。

### `memory_stores.memories.retrieve`

`GET /memory_stores/{memory_store_id}/memories/{memory_id}`

```python
def retrieve(
    memory_id: str,
    *,
    memory_store_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    view: Union[Literal['basic', 'full'], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> Memory: ...
```

调用：`client.memory_stores.memories.retrieve(...)`。实现：[同步](../src/qca/managed/resources/memory_stores/memories.py#L62) / [异步](../src/qca/managed/resources/memory_stores/memories.py#L224)。

路径：`memory_id`、`memory_store_id`。

查询：`view`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/memory_store_memory_retrieve_params.py)。类型定义：[Memory](../src/qca/managed/types/memory.py)、[NotGiven](../src/qca/common/_types.py)。

### `memory_stores.memories.update`

`POST /memory_stores/{memory_store_id}/memories/{memory_id}`

```python
def update(
    memory_id: str,
    *,
    memory_store_id: str,
    content_sha256: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    content: Union[str, None, NotGiven] = NOT_GIVEN,
    path: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    view: Union[Literal['basic', 'full'], None, NotGiven] = NOT_GIVEN,
    precondition: Union[PreconditionParam, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> Memory: ...
```

调用：`client.memory_stores.memories.update(...)`。实现：[同步](../src/qca/managed/resources/memory_stores/memories.py#L92) / [异步](../src/qca/managed/resources/memory_stores/memories.py#L254)。

路径：`memory_id`、`memory_store_id`。

正文：`content_sha256`、`metadata`、`content`、`path`、`precondition`。

查询：`view`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/memory_store_memory_update_params.py)。类型定义：[Memory](../src/qca/managed/types/memory.py)、[NotGiven](../src/qca/common/_types.py)、[PreconditionParam](../src/qca/managed/types/precondition_param.py)。

兼容参数 `precondition={"type": "content_sha256", "content_sha256": expected}` 会转换成正文字段 `content_sha256`，不发送 `precondition` 本身；同时给出不同哈希值时抛出 `ValueError`。

### `memory_stores.memories.list`

`GET /memory_stores/{memory_store_id}/memories`

```python
def list(
    memory_store_id: str,
    *,
    depth: Union[int, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    path_prefix: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    view: Union[Literal['basic', 'full'], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> SyncPage[MemoryListItemUnion]: ...
```

调用：`client.memory_stores.memories.list(...)`。实现：[同步](../src/qca/managed/resources/memory_stores/memories.py#L135) / [异步](../src/qca/managed/resources/memory_stores/memories.py#L297)。异步返回 `AsyncPaginator[MemoryListItemUnion]`。

路径：`memory_store_id`。

查询：`depth`、`limit`、`page`、`path_prefix`、`view`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/memory_store_memory_list_params.py)。类型定义：[MemoryListItemUnion](../src/qca/managed/types/memory_list_item_union.py)、[NotGiven](../src/qca/common/_types.py)、[SyncPage](../src/qca/common/pagination.py)。

分页协议：`PageCursor`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

### `memory_stores.memories.delete`

`DELETE /memory_stores/{memory_store_id}/memories/{memory_id}`

```python
def delete(
    memory_id: str,
    *,
    memory_store_id: str,
    expected_content_sha256: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> DeletedMemory: ...
```

调用：`client.memory_stores.memories.delete(...)`。实现：[同步](../src/qca/managed/resources/memory_stores/memories.py#L164) / [异步](../src/qca/managed/resources/memory_stores/memories.py#L330)。

路径：`memory_id`、`memory_store_id`。

查询：`expected_content_sha256`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/memory_store_memory_delete_params.py)。类型定义：[DeletedMemory](../src/qca/managed/types/deleted_memory.py)、[NotGiven](../src/qca/common/_types.py)。

### `memory_stores.memory_versions.retrieve`

`GET /memory_stores/{memory_store_id}/memory_versions/{memory_version_id}`

```python
def retrieve(
    memory_version_id: str,
    *,
    memory_store_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    view: Union[Literal['basic', 'full'], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> MemoryVersion: ...
```

调用：`client.memory_stores.memory_versions.retrieve(...)`。实现：[同步](../src/qca/managed/resources/memory_stores/memory_versions.py#L18) / [异步](../src/qca/managed/resources/memory_stores/memory_versions.py#L124)。

路径：`memory_version_id`、`memory_store_id`。

查询：`view`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/memory_store_memory_version_retrieve_params.py)。类型定义：[MemoryVersion](../src/qca/managed/types/memory_version.py)、[NotGiven](../src/qca/common/_types.py)。

### `memory_stores.memory_versions.list`

`GET /memory_stores/{memory_store_id}/memory_versions`

```python
def list(
    memory_store_id: str,
    *,
    api_key_id: Union[str, None, NotGiven] = NOT_GIVEN,
    created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    memory_id: Union[str, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    service_account_id: Union[str, None, NotGiven] = NOT_GIVEN,
    session_id: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    operation: Union[Literal['created', 'modified', 'deleted'], None, NotGiven] = NOT_GIVEN,
    view: Union[Literal['basic', 'full'], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> SyncPage[MemoryVersion]: ...
```

调用：`client.memory_stores.memory_versions.list(...)`。实现：[同步](../src/qca/managed/resources/memory_stores/memory_versions.py#L48) / [异步](../src/qca/managed/resources/memory_stores/memory_versions.py#L154)。异步返回 `AsyncPaginator[MemoryVersion]`。

路径：`memory_store_id`。

查询：`api_key_id`、`created_at_gte` → `created_at[gte]`、`created_at_lte` → `created_at[lte]`、`limit`、`memory_id`、`page`、`service_account_id`、`session_id`、`operation`、`view`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/memory_store_memory_version_list_params.py)。类型定义：[MemoryVersion](../src/qca/managed/types/memory_version.py)、[NotGiven](../src/qca/common/_types.py)、[SyncPage](../src/qca/common/pagination.py)。

分页协议：`PageCursor`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

### `memory_stores.memory_versions.redact`

`POST /memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact`

```python
def redact(
    memory_version_id: str,
    *,
    memory_store_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> MemoryVersion: ...
```

调用：`client.memory_stores.memory_versions.redact(...)`。实现：[同步](../src/qca/managed/resources/memory_stores/memory_versions.py#L93) / [异步](../src/qca/managed/resources/memory_stores/memory_versions.py#L201)。

路径：`memory_version_id`、`memory_store_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/memory_store_memory_version_redact_params.py)。类型定义：[MemoryVersion](../src/qca/managed/types/memory_version.py)、[NotGiven](../src/qca/common/_types.py)。

## models

获取当前账号的模型列表与启用状态，创建 Agent 或 Template 前可从中选择可用模型。

### `models.list`

`GET /models`

```python
def list(
    *,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> SyncPage[ModelInfo]: ...
```

调用：`client.models.list(...)`。实现：[同步](../src/qca/managed/resources/models.py#L17) / [异步](../src/qca/managed/resources/models.py#L45)。异步返回 `AsyncPaginator[ModelInfo]`。

查询：`after_id`、`before_id`、`limit`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/model_list_params.py)。类型定义：[ModelInfo](../src/qca/managed/types/model_info.py)、[NotGiven](../src/qca/common/_types.py)、[SyncPage](../src/qca/common/pagination.py)。

分页协议：`Page`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

## sessions

创建、查询和管理会话。events 发送输入并读取历史或 SSE；threads 访问子线程，resources 管理挂载资源。

### `sessions.create`

`POST /sessions`

```python
def create(
    *,
    agent: Union[str, AgentParams, AgentWithOverridesParams],
    environment_id: str,
    environment_variables: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
    title: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    budget: Union[BudgetLimitParam, None, NotGiven] = NOT_GIVEN,
    initial_events: Union[List[Union[UserMessageEventParams, UserDefineOutcomeEventParams]], None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
    resources: Union[List[Union[GitHubRepositoryResourceParams, FileResourceParams, MemoryStoreResourceParam]], None, NotGiven] = NOT_GIVEN,
    vault_ids: Union[List[str], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> Session: ...
```

调用：`client.sessions.create(...)`。实现：[同步](../src/qca/managed/resources/sessions/sessions.py#L44) / [异步](../src/qca/managed/resources/sessions/sessions.py#L265)。

正文：`environment_variables`、`agent`、`environment_id`、`title`、`budget`、`initial_events`、`metadata`、`resources`、`vault_ids`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/session_create_params.py)。类型定义：[AgentParams](../src/qca/managed/types/agent_params.py)、[AgentWithOverridesParams](../src/qca/managed/types/agent_with_overrides_params.py)、[BudgetLimitParam](../src/qca/managed/types/budget_limit_param.py)、[FileResourceParams](../src/qca/managed/types/file_resource_params.py)、[GitHubRepositoryResourceParams](../src/qca/managed/types/git_hub_repository_resource_params.py)、[MemoryStoreResourceParam](../src/qca/managed/types/memory_store_resource_param.py)、[NotGiven](../src/qca/common/_types.py)、[Session](../src/qca/managed/types/session.py)、[UserDefineOutcomeEventParams](../src/qca/managed/types/user_define_outcome_event_params.py)、[UserMessageEventParams](../src/qca/managed/types/user_message_event_params.py)。

### `sessions.retrieve`

`GET /sessions/{session_id}`

```python
def retrieve(
    session_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> Session: ...
```

调用：`client.sessions.retrieve(...)`。实现：[同步](../src/qca/managed/resources/sessions/sessions.py#L90) / [异步](../src/qca/managed/resources/sessions/sessions.py#L311)。

路径：`session_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/session_retrieve_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[Session](../src/qca/managed/types/session.py)。

### `sessions.update`

`POST /sessions/{session_id}`

```python
def update(
    session_id: str,
    *,
    environment_variables: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
    title: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    agent: Union[SessionAgentUpdateParam, None, NotGiven] = NOT_GIVEN,
    budget: Union[BudgetLimitParam, None, NotGiven] = NOT_GIVEN,
    vault_ids: Union[List[str], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> Session: ...
```

调用：`client.sessions.update(...)`。实现：[同步](../src/qca/managed/resources/sessions/sessions.py#L114) / [异步](../src/qca/managed/resources/sessions/sessions.py#L335)。

路径：`session_id`。

正文：`environment_variables`、`title`、`metadata`、`agent`、`budget`、`vault_ids`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/session_update_params.py)。类型定义：[BudgetLimitParam](../src/qca/managed/types/budget_limit_param.py)、[NotGiven](../src/qca/common/_types.py)、[Session](../src/qca/managed/types/session.py)、[SessionAgentUpdateParam](../src/qca/managed/types/session_agent_update_param.py)。

### `sessions.list`

`GET /sessions`

```python
def list(
    *,
    agent_id: Union[str, None, NotGiven] = NOT_GIVEN,
    agent_version: Union[int, None, NotGiven] = NOT_GIVEN,
    created_at_gt: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lt: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    deployment_id: Union[str, None, NotGiven] = NOT_GIVEN,
    include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    memory_store_id: Union[str, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    order: Union[Literal['asc', 'desc'], None, NotGiven] = NOT_GIVEN,
    statuses: Union[List[str], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> SyncPage[Session]: ...
```

调用：`client.sessions.list(...)`。实现：[同步](../src/qca/managed/resources/sessions/sessions.py#L151) / [异步](../src/qca/managed/resources/sessions/sessions.py#L372)。异步返回 `AsyncPaginator[Session]`。

查询：`agent_id`、`agent_version`、`created_at_gt` → `created_at[gt]`、`created_at_gte` → `created_at[gte]`、`created_at_lt` → `created_at[lt]`、`created_at_lte` → `created_at[lte]`、`deployment_id`、`include_archived`、`limit`、`memory_store_id`、`page`、`order`、`statuses` → `statuses[]`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/session_list_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[Session](../src/qca/managed/types/session.py)、[SyncPage](../src/qca/common/pagination.py)。

分页协议：`BidirectionalPageCursor`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

### `sessions.delete`

`DELETE /sessions/{session_id}`

```python
def delete(
    session_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> DeletedSession: ...
```

调用：`client.sessions.delete(...)`。实现：[同步](../src/qca/managed/resources/sessions/sessions.py#L203) / [异步](../src/qca/managed/resources/sessions/sessions.py#L426)。

路径：`session_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/session_delete_params.py)。类型定义：[DeletedSession](../src/qca/managed/types/deleted_session.py)、[NotGiven](../src/qca/common/_types.py)。

### `sessions.archive`

`POST /sessions/{session_id}/archive`

```python
def archive(
    session_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> Session: ...
```

调用：`client.sessions.archive(...)`。实现：[同步](../src/qca/managed/resources/sessions/sessions.py#L227) / [异步](../src/qca/managed/resources/sessions/sessions.py#L450)。

路径：`session_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/session_archive_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[Session](../src/qca/managed/types/session.py)。

### `sessions.events.list`

`GET /sessions/{session_id}/events`

```python
def list(
    session_id: str,
    *,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    created_at_gt: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lt: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    order: Union[Literal['asc', 'desc'], None, NotGiven] = NOT_GIVEN,
    types: Union[List[str], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> SyncPage[SessionEvent]: ...
```

调用：`client.sessions.events.list(...)`。实现：[同步](../src/qca/managed/resources/sessions/events.py#L28) / [异步](../src/qca/managed/resources/sessions/events.py#L135)。异步返回 `AsyncPaginator[SessionEvent]`。

路径：`session_id`。

查询：`before_id`、`after_id`、`created_at_gt` → `created_at[gt]`、`created_at_gte` → `created_at[gte]`、`created_at_lt` → `created_at[lt]`、`created_at_lte` → `created_at[lte]`、`limit`、`page`、`order`、`types` → `types[]`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/session_event_list_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[SessionEvent](../src/qca/managed/types/session_event.py)、[SyncPage](../src/qca/common/pagination.py)。

分页协议：`PageCursor`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

### `sessions.events.send`

`POST /sessions/{session_id}/events`

```python
def send(
    session_id: str,
    *,
    events: List[Union[UserMessageEventParams, UserInterruptEventParams, UserToolConfirmationEventParams, UserCustomToolResultEventParams, UserDefineOutcomeEventParams, UserToolResultEventParams, SystemMessageEventParams]],
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> SendSessionEvents: ...
```

调用：`client.sessions.events.send(...)`。实现：[同步](../src/qca/managed/resources/sessions/events.py#L73) / [异步](../src/qca/managed/resources/sessions/events.py#L182)。

路径：`session_id`。

正文：`events`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/session_event_send_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[SendSessionEvents](../src/qca/managed/types/send_session_events.py)、[SystemMessageEventParams](../src/qca/managed/types/system_message_event_params.py)、[UserCustomToolResultEventParams](../src/qca/managed/types/user_custom_tool_result_event_params.py)、[UserDefineOutcomeEventParams](../src/qca/managed/types/user_define_outcome_event_params.py)、[UserInterruptEventParams](../src/qca/managed/types/user_interrupt_event_params.py)、[UserMessageEventParams](../src/qca/managed/types/user_message_event_params.py)、[UserToolConfirmationEventParams](../src/qca/managed/types/user_tool_confirmation_event_params.py)、[UserToolResultEventParams](../src/qca/managed/types/user_tool_result_event_params.py)。

### `sessions.events.stream`

`GET /sessions/{session_id}/events/stream`

```python
def stream(
    session_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    event_deltas: Union[List[Literal['agent.message', 'agent.thinking']], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> Stream[SessionStreamEvent]: ...
```

调用：`client.sessions.events.stream(...)`。实现：[同步](../src/qca/managed/resources/sessions/events.py#L108) / [异步](../src/qca/managed/resources/sessions/events.py#L217)。异步返回 `AsyncStream[SessionStreamEvent]`。

路径：`session_id`。

查询：`event_deltas` → `event_deltas[]`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/session_event_stream_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[SessionStreamEvent](../src/qca/managed/types/session_stream_event.py)、[Stream](../src/qca/common/_streaming.py)。

SSE：读取事件直到业务终止条件，退出上下文关闭连接；保存 `last_event_id` 用于断点恢复。

### `sessions.resources.retrieve`

`GET /sessions/{session_id}/resources/{resource_id}`

```python
def retrieve(
    resource_id: str,
    *,
    session_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> SessionResourceGetResponseUnion: ...
```

调用：`client.sessions.resources.retrieve(...)`。实现：[同步](../src/qca/managed/resources/sessions/resources.py#L21) / [异步](../src/qca/managed/resources/sessions/resources.py#L163)。

路径：`resource_id`、`session_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/session_resource_retrieve_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[SessionResourceGetResponseUnion](../src/qca/managed/types/session_resource_get_response_union.py)。

### `sessions.resources.update`

`POST /sessions/{session_id}/resources/{resource_id}`

```python
def update(
    resource_id: str,
    *,
    session_id: str,
    password: Union[str, None, NotGiven] = NOT_GIVEN,
    authorization_token: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> SessionResourceUpdateResponseUnion: ...
```

调用：`client.sessions.resources.update(...)`。实现：[同步](../src/qca/managed/resources/sessions/resources.py#L48) / [异步](../src/qca/managed/resources/sessions/resources.py#L190)。

路径：`resource_id`、`session_id`。

正文：`password`、`authorization_token`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/session_resource_update_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[SessionResourceUpdateResponseUnion](../src/qca/managed/types/session_resource_update_response_union.py)。

### `sessions.resources.list`

`GET /sessions/{session_id}/resources`

```python
def list(
    session_id: str,
    *,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> SyncPage[SessionResourceUnion]: ...
```

调用：`client.sessions.resources.list(...)`。实现：[同步](../src/qca/managed/resources/sessions/resources.py#L77) / [异步](../src/qca/managed/resources/sessions/resources.py#L219)。异步返回 `AsyncPaginator[SessionResourceUnion]`。

路径：`session_id`。

查询：`before_id`、`after_id`、`limit`、`page`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/session_resource_list_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[SessionResourceUnion](../src/qca/managed/types/session_resource_union.py)、[SyncPage](../src/qca/common/pagination.py)。

分页协议：`PageCursor`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

### `sessions.resources.delete`

`DELETE /sessions/{session_id}/resources/{resource_id}`

```python
def delete(
    resource_id: str,
    *,
    session_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> DeleteSessionResource: ...
```

调用：`client.sessions.resources.delete(...)`。实现：[同步](../src/qca/managed/resources/sessions/resources.py#L107) / [异步](../src/qca/managed/resources/sessions/resources.py#L251)。

路径：`resource_id`、`session_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/session_resource_delete_params.py)。类型定义：[DeleteSessionResource](../src/qca/managed/types/delete_session_resource.py)、[NotGiven](../src/qca/common/_types.py)。

### `sessions.resources.add`

`POST /sessions/{session_id}/resources`

```python
def add(
    session_id: str,
    *,
    file_id: str,
    type: Literal['file'],
    mount_path: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> FileResource: ...
```

调用：`client.sessions.resources.add(...)`。实现：[同步](../src/qca/managed/resources/sessions/resources.py#L134) / [异步](../src/qca/managed/resources/sessions/resources.py#L278)。

路径：`session_id`。

正文：`file_id`、`type`、`mount_path`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/session_resource_add_params.py)。类型定义：[FileResource](../src/qca/managed/types/file_resource.py)、[NotGiven](../src/qca/common/_types.py)。

### `sessions.threads.retrieve`

`GET /sessions/{session_id}/threads/{thread_id}`

```python
def retrieve(
    thread_id: str,
    *,
    session_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> SessionThread: ...
```

调用：`client.sessions.threads.retrieve(...)`。实现：[同步](../src/qca/managed/resources/sessions/threads/threads.py#L23) / [异步](../src/qca/managed/resources/sessions/threads/threads.py#L107)。

路径：`thread_id`、`session_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/session_thread_retrieve_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[SessionThread](../src/qca/managed/types/session_thread.py)。

### `sessions.threads.list`

`GET /sessions/{session_id}/threads`

```python
def list(
    session_id: str,
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> SyncPage[SessionThread]: ...
```

调用：`client.sessions.threads.list(...)`。实现：[同步](../src/qca/managed/resources/sessions/threads/threads.py#L48) / [异步](../src/qca/managed/resources/sessions/threads/threads.py#L132)。异步返回 `AsyncPaginator[SessionThread]`。

路径：`session_id`。

查询：`limit`、`page`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/session_thread_list_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[SessionThread](../src/qca/managed/types/session_thread.py)、[SyncPage](../src/qca/common/pagination.py)。

分页协议：`PageCursor`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

### `sessions.threads.archive`

`POST /sessions/{session_id}/threads/{thread_id}/archive`

```python
def archive(
    thread_id: str,
    *,
    session_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> SessionThread: ...
```

调用：`client.sessions.threads.archive(...)`。实现：[同步](../src/qca/managed/resources/sessions/threads/threads.py#L74) / [异步](../src/qca/managed/resources/sessions/threads/threads.py#L160)。

路径：`thread_id`、`session_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/session_thread_archive_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[SessionThread](../src/qca/managed/types/session_thread.py)。

### `sessions.threads.events.list`

`GET /sessions/{session_id}/threads/{thread_id}/events`

```python
def list(
    thread_id: str,
    *,
    session_id: str,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> SyncPage[SessionEvent]: ...
```

调用：`client.sessions.threads.events.list(...)`。实现：[同步](../src/qca/managed/resources/sessions/threads/events.py#L19) / [异步](../src/qca/managed/resources/sessions/threads/events.py#L80)。异步返回 `AsyncPaginator[SessionEvent]`。

路径：`thread_id`、`session_id`。

查询：`before_id`、`after_id`、`limit`、`page`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/session_thread_event_list_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[SessionEvent](../src/qca/managed/types/session_event.py)、[SyncPage](../src/qca/common/pagination.py)。

分页协议：`PageCursor`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

### `sessions.threads.events.stream`

`GET /sessions/{session_id}/threads/{thread_id}/stream`

```python
def stream(
    thread_id: str,
    *,
    session_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    event_deltas: Union[List[Literal['agent.message', 'agent.thinking']], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> Stream[StreamSessionThreadEventsUnion]: ...
```

调用：`client.sessions.threads.events.stream(...)`。实现：[同步](../src/qca/managed/resources/sessions/threads/events.py#L50) / [异步](../src/qca/managed/resources/sessions/threads/events.py#L113)。异步返回 `AsyncStream[StreamSessionThreadEventsUnion]`。

路径：`thread_id`、`session_id`。

查询：`event_deltas` → `event_deltas[]`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/session_thread_event_stream_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[Stream](../src/qca/common/_streaming.py)、[StreamSessionThreadEventsUnion](../src/qca/managed/types/stream_session_thread_events_union.py)。

SSE：读取事件直到业务终止条件，退出上下文关闭连接；保存 `last_event_id` 用于断点恢复。

## skills

上传 Skill 文件并管理版本；版本下载返回二进制响应。Skill 路径会保留在 multipart 文件名中。

### `skills.create`

`POST /skills`

```python
def create(
    *,
    files: List[FileTypes],
    metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
    display_title: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> Skill: ...
```

调用：`client.skills.create(...)`。实现：[同步](../src/qca/managed/resources/skills/skills.py#L24) / [异步](../src/qca/managed/resources/skills/skills.py#L142)。

正文：`metadata`、`files`、`display_title`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/skill_create_params.py)。类型定义：[FileTypes](../src/qca/common/_types.py)、[NotGiven](../src/qca/common/_types.py)、[Skill](../src/qca/managed/types/skill.py)。

### `skills.retrieve`

`GET /skills/{skill_id}`

```python
def retrieve(
    skill_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> Skill: ...
```

调用：`client.skills.retrieve(...)`。实现：[同步](../src/qca/managed/resources/skills/skills.py#L50) / [异步](../src/qca/managed/resources/skills/skills.py#L168)。

路径：`skill_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/skill_retrieve_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[Skill](../src/qca/managed/types/skill.py)。

### `skills.list`

`GET /skills`

```python
def list(
    *,
    display_name: Union[str, None, NotGiven] = NOT_GIVEN,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    source: Union[str, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> SyncPage[Skill]: ...
```

调用：`client.skills.list(...)`。实现：[同步](../src/qca/managed/resources/skills/skills.py#L74) / [异步](../src/qca/managed/resources/skills/skills.py#L192)。异步返回 `AsyncPaginator[Skill]`。

查询：`display_name` → `display_title`、`name`、`before_id`、`after_id`、`page`、`source`、`limit`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/skill_list_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[Skill](../src/qca/managed/types/skill.py)、[SyncPage](../src/qca/common/pagination.py)。

分页协议：`PageCursor`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

### `skills.delete`

`DELETE /skills/{skill_id}`

```python
def delete(
    skill_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> DeletedSkill: ...
```

调用：`client.skills.delete(...)`。实现：[同步](../src/qca/managed/resources/skills/skills.py#L112) / [异步](../src/qca/managed/resources/skills/skills.py#L232)。

路径：`skill_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/skill_delete_params.py)。类型定义：[DeletedSkill](../src/qca/managed/types/deleted_skill.py)、[NotGiven](../src/qca/common/_types.py)。

### `skills.versions.create`

`POST /skills/{skill_id}/versions`

```python
def create(
    skill_id: str,
    *,
    files: List[FileTypes],
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> SkillVersion: ...
```

调用：`client.skills.versions.create(...)`。实现：[同步](../src/qca/managed/resources/skills/versions.py#L19) / [异步](../src/qca/managed/resources/skills/versions.py#L147)。

路径：`skill_id`。

正文：`files`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/skill_version_create_params.py)。类型定义：[FileTypes](../src/qca/common/_types.py)、[NotGiven](../src/qca/common/_types.py)、[SkillVersion](../src/qca/managed/types/skill_version.py)。

### `skills.versions.retrieve`

`GET /skills/{skill_id}/versions/{version}`

```python
def retrieve(
    version: str,
    *,
    skill_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> SkillVersion: ...
```

调用：`client.skills.versions.retrieve(...)`。实现：[同步](../src/qca/managed/resources/skills/versions.py#L44) / [异步](../src/qca/managed/resources/skills/versions.py#L172)。

路径：`version`、`skill_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/skill_version_retrieve_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[SkillVersion](../src/qca/managed/types/skill_version.py)。

### `skills.versions.list`

`GET /skills/{skill_id}/versions`

```python
def list(
    skill_id: str,
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> SyncPage[SkillVersion]: ...
```

调用：`client.skills.versions.list(...)`。实现：[同步](../src/qca/managed/resources/skills/versions.py#L69) / [异步](../src/qca/managed/resources/skills/versions.py#L197)。异步返回 `AsyncPaginator[SkillVersion]`。

路径：`skill_id`。

查询：`limit`、`page`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/skill_version_list_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[SkillVersion](../src/qca/managed/types/skill_version.py)、[SyncPage](../src/qca/common/pagination.py)。

分页协议：`PageCursor`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

### `skills.versions.delete`

`DELETE /skills/{skill_id}/versions/{version}`

```python
def delete(
    version: str,
    *,
    skill_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> DeletedSkillVersion: ...
```

调用：`client.skills.versions.delete(...)`。实现：[同步](../src/qca/managed/resources/skills/versions.py#L95) / [异步](../src/qca/managed/resources/skills/versions.py#L225)。

路径：`version`、`skill_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/skill_version_delete_params.py)。类型定义：[DeletedSkillVersion](../src/qca/managed/types/deleted_skill_version.py)、[NotGiven](../src/qca/common/_types.py)。

### `skills.versions.download`

`GET /skills/{skill_id}/versions/{version}/content`

```python
def download(
    version: str,
    *,
    skill_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> BinaryAPIResponse: ...
```

调用：`client.skills.versions.download(...)`。实现：[同步](../src/qca/managed/resources/skills/versions.py#L120) / [异步](../src/qca/managed/resources/skills/versions.py#L250)。异步返回 `AsyncBinaryAPIResponse`。

路径：`version`、`skill_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/skill_version_download_params.py)。类型定义：[BinaryAPIResponse](../src/qca/common/_response.py)、[NotGiven](../src/qca/common/_types.py)。

下载返回二进制响应，使用上下文管理器关闭；通过 `write_to_file()` 写入文件。

## vaults

管理凭据仓库及仓库中的凭据。参数中可能包含令牌或密钥，业务日志应避免打印请求正文。

### `vaults.create`

`POST /vaults`

```python
def create(
    *,
    display_name: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> Vault: ...
```

调用：`client.vaults.create(...)`。实现：[同步](../src/qca/managed/resources/vaults/vaults.py#L24) / [异步](../src/qca/managed/resources/vaults/vaults.py#L163)。

正文：`display_name`、`metadata`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/vault_create_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[Vault](../src/qca/managed/types/vault.py)。

### `vaults.retrieve`

`GET /vaults/{vault_id}`

```python
def retrieve(
    vault_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> Vault: ...
```

调用：`client.vaults.retrieve(...)`。实现：[同步](../src/qca/managed/resources/vaults/vaults.py#L49) / [异步](../src/qca/managed/resources/vaults/vaults.py#L188)。

路径：`vault_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/vault_retrieve_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[Vault](../src/qca/managed/types/vault.py)。

### `vaults.list`

`GET /vaults`

```python
def list(
    *,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> SyncPage[Vault]: ...
```

调用：`client.vaults.list(...)`。实现：[同步](../src/qca/managed/resources/vaults/vaults.py#L73) / [异步](../src/qca/managed/resources/vaults/vaults.py#L212)。异步返回 `AsyncPaginator[Vault]`。

查询：`name`、`before_id`、`after_id`、`include_archived`、`limit`、`page`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/vault_list_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[SyncPage](../src/qca/common/pagination.py)、[Vault](../src/qca/managed/types/vault.py)。

分页协议：`PageCursor`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

### `vaults.delete`

`DELETE /vaults/{vault_id}`

```python
def delete(
    vault_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> DeletedVault: ...
```

调用：`client.vaults.delete(...)`。实现：[同步](../src/qca/managed/resources/vaults/vaults.py#L109) / [异步](../src/qca/managed/resources/vaults/vaults.py#L250)。

路径：`vault_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/vault_delete_params.py)。类型定义：[DeletedVault](../src/qca/managed/types/deleted_vault.py)、[NotGiven](../src/qca/common/_types.py)。

### `vaults.archive`

`POST /vaults/{vault_id}/archive`

```python
def archive(
    vault_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> Vault: ...
```

调用：`client.vaults.archive(...)`。实现：[同步](../src/qca/managed/resources/vaults/vaults.py#L133) / [异步](../src/qca/managed/resources/vaults/vaults.py#L274)。

路径：`vault_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/vault_archive_params.py)。类型定义：[NotGiven](../src/qca/common/_types.py)、[Vault](../src/qca/managed/types/vault.py)。

### `vaults.credentials.create`

`POST /vaults/{vault_id}/credentials`

```python
def create(
    vault_id: str,
    *,
    auth: Union[MCPOAuthCreateParams, StaticBearerCreateParams, EnvironmentVariableCreateParams],
    display_name: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> Credential: ...
```

调用：`client.vaults.credentials.create(...)`。实现：[同步](../src/qca/managed/resources/vaults/credentials.py#L25) / [异步](../src/qca/managed/resources/vaults/credentials.py#L232)。

路径：`vault_id`。

正文：`auth`、`display_name`、`metadata`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/vault_credential_create_params.py)。类型定义：[Credential](../src/qca/managed/types/credential.py)、[EnvironmentVariableCreateParams](../src/qca/managed/types/environment_variable_create_params.py)、[MCPOAuthCreateParams](../src/qca/managed/types/mcpo_auth_create_params.py)、[NotGiven](../src/qca/common/_types.py)、[StaticBearerCreateParams](../src/qca/managed/types/static_bearer_create_params.py)。

### `vaults.credentials.retrieve`

`GET /vaults/{vault_id}/credentials/{credential_id}`

```python
def retrieve(
    credential_id: str,
    *,
    vault_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> Credential: ...
```

调用：`client.vaults.credentials.retrieve(...)`。实现：[同步](../src/qca/managed/resources/vaults/credentials.py#L52) / [异步](../src/qca/managed/resources/vaults/credentials.py#L259)。

路径：`credential_id`、`vault_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/vault_credential_retrieve_params.py)。类型定义：[Credential](../src/qca/managed/types/credential.py)、[NotGiven](../src/qca/common/_types.py)。

### `vaults.credentials.update`

`POST /vaults/{vault_id}/credentials/{credential_id}`

```python
def update(
    credential_id: str,
    *,
    vault_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    auth: Union[Union[MCPOAuthUpdateParams, StaticBearerUpdateParams, EnvironmentVariableUpdateParams], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> Credential: ...
```

调用：`client.vaults.credentials.update(...)`。实现：[同步](../src/qca/managed/resources/vaults/credentials.py#L79) / [异步](../src/qca/managed/resources/vaults/credentials.py#L286)。

路径：`credential_id`、`vault_id`。

正文：`metadata`、`auth`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/vault_credential_update_params.py)。类型定义：[Credential](../src/qca/managed/types/credential.py)、[EnvironmentVariableUpdateParams](../src/qca/managed/types/environment_variable_update_params.py)、[MCPOAuthUpdateParams](../src/qca/managed/types/mcpo_auth_update_params.py)、[NotGiven](../src/qca/common/_types.py)、[StaticBearerUpdateParams](../src/qca/managed/types/static_bearer_update_params.py)。

### `vaults.credentials.list`

`GET /vaults/{vault_id}/credentials`

```python
def list(
    vault_id: str,
    *,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> SyncPage[Credential]: ...
```

调用：`client.vaults.credentials.list(...)`。实现：[同步](../src/qca/managed/resources/vaults/credentials.py#L110) / [异步](../src/qca/managed/resources/vaults/credentials.py#L317)。异步返回 `AsyncPaginator[Credential]`。

路径：`vault_id`。

查询：`name`、`before_id`、`after_id`、`include_archived`、`limit`、`page`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/vault_credential_list_params.py)。类型定义：[Credential](../src/qca/managed/types/credential.py)、[NotGiven](../src/qca/common/_types.py)、[SyncPage](../src/qca/common/pagination.py)。

分页协议：`PageCursor`；同步返回可迭代页对象，异步支持 `await` 第一页或 `async for` 全量迭代。

### `vaults.credentials.delete`

`DELETE /vaults/{vault_id}/credentials/{credential_id}`

```python
def delete(
    credential_id: str,
    *,
    vault_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> DeletedCredential: ...
```

调用：`client.vaults.credentials.delete(...)`。实现：[同步](../src/qca/managed/resources/vaults/credentials.py#L147) / [异步](../src/qca/managed/resources/vaults/credentials.py#L356)。

路径：`credential_id`、`vault_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/vault_credential_delete_params.py)。类型定义：[DeletedCredential](../src/qca/managed/types/deleted_credential.py)、[NotGiven](../src/qca/common/_types.py)。

### `vaults.credentials.archive`

`POST /vaults/{vault_id}/credentials/{credential_id}/archive`

```python
def archive(
    credential_id: str,
    *,
    vault_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> Credential: ...
```

调用：`client.vaults.credentials.archive(...)`。实现：[同步](../src/qca/managed/resources/vaults/credentials.py#L174) / [异步](../src/qca/managed/resources/vaults/credentials.py#L383)。

路径：`credential_id`、`vault_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

请求字段：[TypedDict](../src/qca/managed/types/vault_credential_archive_params.py)。类型定义：[Credential](../src/qca/managed/types/credential.py)、[NotGiven](../src/qca/common/_types.py)。

### `vaults.credentials.mcp_oauth_validate`

`POST /vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate`

```python
def mcp_oauth_validate(
    credential_id: str,
    *,
    vault_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
) -> CredentialValidation: ...
```

调用：`client.vaults.credentials.mcp_oauth_validate(...)`。实现：[同步](../src/qca/managed/resources/vaults/credentials.py#L201) / [异步](../src/qca/managed/resources/vaults/credentials.py#L410)。

路径：`credential_id`、`vault_id`。

请求头：`workspace_id` → `qoder-workspace-id`、`betas` → `x-qoder-beta`。

类型定义：[CredentialValidation](../src/qca/managed/types/credential_validation.py)、[NotGiven](../src/qca/common/_types.py)。
