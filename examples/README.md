# 可运行示例与测试

每个场景一个文件，按 Forward / Managed 分目录。打开场景文件即可从上到下阅读主要 API 调用，包括创建资源、执行和结果校验。每个文件顶部都有运行命令。

| 场景 | Forward 文件 | Managed 文件 | 验证内容 |
|---|---|---|---|
| models | [models.py](forward/models.py) | [models.py](managed/models.py) | 查询账号已启用的模型 |
| session | [session.py](forward/session.py) | [session.py](managed/session.py) | 创建会话、发送消息、SSE 最终回复 |
| resources | [resources.py](forward/resources.py) | [resources.py](managed/resources.py) | 文件挂载、环境变量、自定义 Skill、实际工具调用 |
| memory | [memory.py](forward/memory.py) | [memory.py](managed/memory.py) | 保存正文与索引，在新会话中按记忆回答 |
| schedule | [schedule.py](forward/schedule.py) | — | 手动 Schedule Run 与关联会话回复 |
| batch | [batch.py](forward/batch.py) | — | 单行 JSONL、任务归属、输出与会话回复 |
| deployment | — | [deployment.py](managed/deployment.py) | 手动 Deployment Run 和会话回复 |
| dream | — | [dream.py](managed/dream.py) | 整理记忆、读取输出正文、保留原始校验值 |
| async_session | [async_session.py](forward/async_session.py) | [async_session.py](managed/async_session.py) | 使用原生异步客户端继续已有会话并读取 SSE |

Forward 的 memory 示例通过 Identity + Template 绑定记忆；Managed 直接挂载到 Session。

## 单独运行

在仓库根目录执行：

```bash
python -m pip install -e '.[dev]'
cp .env.live.example .env.live
# 填入 PAT
python -m examples.forward.models
python -m examples.forward.session
python -m examples.forward.resources
python -m examples.managed.memory
python -m examples.managed.dream --timeout 600 --output json
```

建议从 `models.py` 开始，再看 `session.py`。每个同步场景支持 `--env`、`--region cn|international`、`--timeout` 和 `--output text|json`。

默认输出实际结果：`models` 展示模型 ID、启用状态和选中的模型；`session` 展示创建的资源 ID、用户消息和助手回复。其他场景也展示资源 ID、回复或记忆整理结果，最后打印清理结果和 `PASS` / `FAIL`。`PASS` 表示场景断言通过，且需要清理的资源已处理完成。

例如 `session` 的输出如下（ID 和回复为示意，实际内容以 API 返回为准）：

```text
[forward.session]
environment_id: env_...
identity_id: idn_...
selected_model: ultimate
template_id: tmpl_...
session_id: sess_...
user: 请用一句话介绍你能提供什么帮助，并在末尾原样附上：...
assistant: 我可以帮助你编写代码、分析问题和处理资料。...
cleanup: completed
session: PASS
```

使用 `--output json` 时，标准输出为一个 JSON 数组，每个场景包含 `scenario`、`passed`、`outputs` 和 `errors`。`outputs` 按执行顺序保存 `{ "label": "...", "value": ... }`，失败时也保留已经产生的结果。

HTTP 错误会展示请求方法、接口路径、服务端错误消息和请求 ID。例如 `Idempotency-Key header is required` 表示缺少幂等键；Forward 创建记忆库时必须传入 `idempotency_key`，`memory.py` 已包含该参数。

`run(client, context)` 包含该场景的实现。文件末尾的 `run_cli(...)` 负责读取配置、创建对应 mode 的客户端、调用 `run` 并在结束后清理。`common/live.py` 提供配置、等待回复、结果断言和清理登记；各 mode 的 `_cleanup.py` 处理其会话关闭方式。

`models` 只读。其他同步场景创建并清理资源、执行模型请求，可能消耗额度。清理逆序执行，即使前一项失败也继续；清理失败会导致非零退出码。

仍可通过 mode 入口选场景或依次运行全部同步场景，默认运行 `models`：

```bash
python -m examples.forward --scenario session
python -m examples.managed --scenario all --timeout 600 --output json
```

## 测试

pytest 直接调用各场景文件中的 `run` 函数：

```bash
QODER_RUN_LIVE=1 python -m pytest examples/forward -m live -v
QODER_RUN_LIVE=1 python -m pytest examples/managed -m live -v
QODER_RUN_LIVE=1 python -m pytest examples/forward -k memory -v
```

日常离线测试会跳过这 12 个 live 用例，通过 `tests/test_examples.py` 的模拟服务执行同样的 12 个场景。

## 异步会话

两个 mode 分别使用 `AsyncForward` 和 `AsyncManaged`：

```bash
QODER_SESSION_ID=sess_example python -m examples.forward.async_session
QODER_SESSION_ID=sess_example python -m examples.managed.async_session
```

这两个片段使用已有 Session 并发送一条消息，从 SDK 标准环境变量读取配置，不读取 `.env.live`，也不清理调用方提供的 Session。它们不在上述 12 个场景或 `--scenario all` 范围内。
