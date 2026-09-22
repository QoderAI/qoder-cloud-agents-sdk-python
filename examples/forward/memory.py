"""写入项目记忆并挂载到新会话，发送消息并打印助手回复。

运行：python -m examples.forward.memory
"""

from __future__ import annotations

from examples.common.live import Run, choose_model, name, run_cli
from qca import Forward

from ._cleanup import finish_session

# 一段临时的项目记忆，仅用于演示如何写入并挂载 Memory Store。
MEMORY_PATH = "projects/release-conventions.md"
MEMORY_DOC = (
    "---\n"
    "name: release-conventions\n"
    "description: 青禾订单 的项目发布约定\n"
    "metadata:\n"
    "  type: project\n"
    "---\n\n"
    "# 青禾订单\n\n"
    "- 北京时间 22:30 开始发布。\n"
    "- 发布异常时联系值班负责人林岚。\n"
    "- 回滚使用已验证的稳定版本 v2.480.15。\n\n"
    "Why: 在值班窗口发布，并使用验证过的版本恢复服务。\n"
    "How to apply: 为这个项目拟定发布计划时遵循以上约定。\n"
)
MEMORY_INDEX = f"- [青禾订单 发布约定]({MEMORY_PATH}) — 发布窗口、异常联系人与回滚约定。\n"
MEMORY_PROMPT = "请根据你记得的项目约定，为「青禾订单」拟一份简短上线安排，涵盖开始时间、异常联系和回滚处理。不要执行发布；缺少信息时请明确说明。"


def run(client: Forward, context: Run) -> None:
    environment = client.environments.create(name=name("env"), config={"type": "cloud"})
    environment_id = context.track("environment", environment.id, lambda: client.environments.archive(environment.id))

    identity = client.identities.create(external_id=name("identity"), name="SDK 示例用户")
    identity_id = context.track("identity", identity.id, lambda: client.identities.delete(identity.id))

    store = client.memory_stores.create(name=name("memory"), idempotency_key=name("memory-key"))
    context.track("memory_store", store.id, lambda: client.memory_stores.delete(store.id))
    for path, content in ((MEMORY_PATH, MEMORY_DOC), ("MEMORY.md", MEMORY_INDEX)):
        client.memory_stores.memories.create(store.id, path=path, content=content)

    model = choose_model(client.models.list(), context.config.model)
    context.output("selected_model", model)
    template = client.templates.create(
        name=name("template"),
        environment_id=environment_id,
        model=model,
        system="你是一个 SDK 示例助手。必要时调用工具，只使用可实际读取的数据回答问题。",
        tools=[{"type": "agent_toolset_20260401"}],
    )
    template_id = context.track("template", template.id, lambda: client.templates.archive(template.id))

    client.identities.memory_stores.mount(template_id, identity_id=identity_id, memory_store_id=store.id)
    context.track(
        "memory_mount",
        store.id,
        lambda: client.identities.memory_stores.detach(store.id, template_id=template_id, identity_id=identity_id),
    )
    session = client.sessions.create(
        identity_id=identity_id,
        template_id=template_id,
    )
    session_id = context.track("session", session.id, lambda: finish_session(client, context, session.id))

    context.output("user", MEMORY_PROMPT)
    sent = client.sessions.events.send(
        session_id,
        events=[{"type": "user.message", "content": [{"type": "text", "text": MEMORY_PROMPT}]}],
        extra_headers={"Idempotency-Key": name("event")},
    )
    if not sent.data or not sent.data[0].id:
        raise RuntimeError("Send returned no user event")
    with client.sessions.events.stream(
        session_id,
        extra_headers={"Last-Event-ID": sent.data[0].id},
        timeout=context.remaining(),
    ) as stream:
        for event in stream:
            context.remaining()
            if event.type == "agent.message":
                context.output("assistant", event.to_json())
            elif event.type in ("session.error", "session.status_terminated"):
                raise RuntimeError(f"Session stopped: {event.type}")
            elif event.type == "session.status_idle":
                break


if __name__ == "__main__":
    run_cli("forward", Forward, {"memory": run})
