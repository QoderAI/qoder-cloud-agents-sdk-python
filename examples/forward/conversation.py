"""复用同一个 Session 进行多轮对话，并分页读取会话历史。

运行：python -m examples.forward.conversation
"""

from __future__ import annotations

from examples.common.live import Run, choose_model, marker, name, run_cli
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

    session = client.sessions.create(identity_id=identity_id, template_id=template_id)
    session_id = context.track("session", session.id, lambda: finish_session(client, context, session.id))

    def ask(prompt: str) -> None:
        context.output("user", prompt)
        sent = client.sessions.events.send(
            session_id,
            events=[{"type": "user.message", "content": [{"type": "text", "text": prompt}]}],
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

    # 同一个 Session 支持多轮：服务端在 session_id 下保留完整历史，无需客户端携带上文。
    code = "project-" + marker()
    ask(f"这次项目代号是 {code}。请在本次对话中记住它，不要使用工具或写入记忆库。现在只回复：已记住。")
    ask("只根据本次会话上文，告诉我刚才约定的项目代号。只回复代号，不要使用工具。")

    # 分页读取已有的用户消息和助手回复，重建对话文字记录。
    for event in client.sessions.events.list(session_id, order="asc", limit=100):
        if event.type in ("user.message", "agent.message"):
            context.output(f"history.{event.type}", event.to_json())


if __name__ == "__main__":
    run_cli("forward", Forward, {"conversation": run})
