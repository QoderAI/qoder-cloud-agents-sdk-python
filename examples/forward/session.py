"""创建会话、发送用户消息，通过 SSE 读取最终回复。

运行：python -m examples.forward.session
"""

from __future__ import annotations

from examples.common.live import Run, TurnResult, choose_model, marker, name, run_cli
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

    expected = marker()
    prompt = "请用一句话介绍你能提供什么帮助，并在末尾原样附上：" + expected
    context.output("user", prompt)
    sent = client.sessions.events.send(
        session_id,
        events=[
            {
                "type": "user.message",
                "content": [{"type": "text", "text": prompt}],
            }
        ],
        extra_headers={"Idempotency-Key": name("event")},
    )
    if len(sent.data) != 1 or not sent.data[0].id:
        raise AssertionError("Send must return exactly one user event ID")

    reply = TurnResult(last_id=sent.data[0].id)
    with client.sessions.events.stream(
        session_id,
        extra_headers={"Last-Event-ID": sent.data[0].id},
        timeout=context.remaining(),
    ) as stream:
        for event in stream:
            context.remaining()
            reply.observe(event)
            if reply.complete:
                break
    context.output("assistant", reply.text)
    reply.verify([expected])


if __name__ == "__main__":
    run_cli("forward", Forward, {"session": run})
