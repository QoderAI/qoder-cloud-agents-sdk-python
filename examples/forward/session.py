"""创建会话、发送用户消息，通过 SSE 读取并打印助手回复。

运行：python -m examples.forward.session
"""

from __future__ import annotations

from examples.common.live import Run, choose_model, name, run_cli
from qca import Forward

from ._cleanup import finish_session


def run(client: Forward, context: Run) -> None:
    environment = client.environments.create(name=name("env"), config={"type": "cloud"})
    environment_id = context.track("environment", environment.id, lambda: client.environments.archive(environment.id))

    identity = client.identities.create(external_id=name("identity"), name="SDK 示例用户")
    identity_id = context.track("identity", identity.id, lambda: client.identities.delete(identity.id))

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

    session = client.sessions.create(
        identity_id=identity_id,
        template_id=template_id,
    )
    session_id = context.track("session", session.id, lambda: finish_session(client, context, session.id))

    prompt = "请用一句话介绍你能提供什么帮助。"
    context.output("user", prompt)
    sent = client.sessions.events.send(
        session_id,
        events=[{"type": "user.message", "content": [{"type": "text", "text": prompt}]}],
        extra_headers={"Idempotency-Key": name("event")},
    )
    if not sent.data or not sent.data[0].id:
        raise RuntimeError("Send returned no user event")

    # 从刚发送的用户事件之后开始订阅，打印助手消息，遇到 idle 即停。
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
    run_cli("forward", Forward, {"session": run})
