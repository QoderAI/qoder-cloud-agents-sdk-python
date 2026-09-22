"""两个 Identity 共用一个 Template，写入各自的个性化配置，再读取生效配置并在会话中验证。

运行：python -m examples.forward.identity_config
"""

from __future__ import annotations

from examples.common.live import Run, choose_model, marker, name, run_cli
from qca import Forward

from ._cleanup import finish_session


def run(client: Forward, context: Run) -> None:
    environment = client.environments.create(name=name("env"), config={"type": "cloud"})
    environment_id = context.track("environment", environment.id, lambda: client.environments.archive(environment.id))

    model = choose_model(client.models.list(), context.config.model)
    context.output("selected_model", model)
    shared, baseline = marker(), marker()
    template = client.templates.create(
        name=name("template"),
        environment_id=environment_id,
        model=model,
        system="你是一个 SDK 示例助手。必要时调用工具，只使用可实际读取的数据回答问题。",
        tools=[{"type": "agent_toolset_20260401"}],
        environment_variables={"SDK_SHARED_VALUE": shared, "SDK_PERSONAL_VALUE": baseline},
    )
    template_id = context.track("template", template.id, lambda: client.templates.archive(template.id))

    # 先创建两个 Identity 并写入个性化配置：SDK_SHARED_VALUE 继承模板默认，SDK_PERSONAL_VALUE 被各自覆盖。
    identities: list[str] = []
    personal: list[str] = []
    for index in range(2):
        identity = client.identities.create(external_id=name("identity"), name=f"SDK 示例用户 {index + 1}")
        identity_id = context.track("identity", identity.id, lambda ref=identity.id: client.identities.delete(ref))
        identities.append(identity_id)
        value = marker()
        personal.append(value)
        client.identities.configs.upsert(
            template_id,
            identity_id=identity_id,
            identity_config={"environment_variables": {"SDK_PERSONAL_VALUE": {"op": "set", "value": value}}},
        )
        effective = client.identities.configs.retrieve_effective(template_id, identity_id=identity_id)
        context.output(
            f"identity_{index + 1}_effective_env",
            effective.session.environment_variables if effective.session else None,
        )

    # 每个 Identity 各起一个会话，读取自己实际生效的环境变量。
    for index, identity_id in enumerate(identities):
        session = client.sessions.create(identity_id=identity_id, template_id=template_id)
        session_id = context.track("session", session.id, lambda ref=session.id: finish_session(client, context, ref))
        prompt = "请使用工具读取 SDK_SHARED_VALUE 和 SDK_PERSONAL_VALUE 两个环境变量，只返回这两个变量的实际值。"
        context.output(f"identity_{index + 1}_user", prompt)
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
                    context.output(f"identity_{index + 1}_assistant", event.to_json())
                elif event.type in ("session.error", "session.status_terminated"):
                    raise RuntimeError(f"Session stopped: {event.type}")
                elif event.type == "session.status_idle":
                    break


if __name__ == "__main__":
    run_cli("forward", Forward, {"identity_config": run})
