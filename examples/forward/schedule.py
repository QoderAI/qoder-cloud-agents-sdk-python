"""创建手动 Schedule，触发执行并打印关联会话的回复。

运行：python -m examples.forward.schedule
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

    schedule = client.schedules.create(
        identity_id=identity_id,
        template_id=template_id,
        environment_id=environment_id,
        name=name("schedule"),
        initial_events=[{"type": "user.message", "content": "请用一句话打个招呼。"}],
        trigger_policy={"type": "manual"},
        execution={"max_attempts": 1, "max_concurrent_runs": 1},
    )
    context.track("schedule", schedule.id, lambda: client.schedules.archive(schedule.id))
    execution = client.schedules.run(schedule.id, idempotency_key=name("run"))

    def cleanup_run() -> None:
        while True:
            current = client.schedule_runs.retrieve(execution.id, identity_id=identity_id)
            if current.session_id:
                finish_session(client, context, current.session_id)
                return
            if current.status in ("failed", "skipped"):
                return
            context.pause()

    context.track("schedule_run", execution.id, cleanup_run)
    while True:
        current = client.schedule_runs.retrieve(execution.id, identity_id=identity_id)
        context.output("run_status", current.status)
        if current.status in ("completed", "failed", "skipped"):
            break
        context.pause()

    if not current.session_id:
        return
    context.output("session_id", current.session_id)
    for event in client.sessions.events.list(current.session_id, order="asc"):
        if event.type == "agent.message":
            context.output("assistant", event.to_json())


if __name__ == "__main__":
    run_cli("forward", Forward, {"schedule": run})
