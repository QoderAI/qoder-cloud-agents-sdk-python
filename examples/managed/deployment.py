"""创建 Deployment，手动运行并验证关联会话的回复。

运行：python -m examples.managed.deployment
"""

from __future__ import annotations

from examples.common.live import Run, choose_model, marker, name, run_cli, wait_reply
from qca import Managed

from ._cleanup import finish_session


def run(client: Managed, context: Run) -> None:
    environment = client.environments.create(name=name("env"), config={"type": "cloud"})
    environment_id = context.track("environment", environment.id, lambda: client.environments.archive(environment.id))

    model = choose_model(client.models.list(), context.config.model)
    context.output("selected_model", model)
    agent = client.agents.create(
        name=name("agent"),
        model={"id": model},
        system="你是一个 SDK 示例助手。必要时调用工具，只使用可实际读取的数据回答问题。",
        tools=[{"type": "agent_toolset_20260401"}],
    )
    agent_id = context.track("agent", agent.id, lambda: client.agents.archive(agent.id))

    expected = marker()
    deployment = client.deployments.create(
        name=name("deployment"),
        environment_id=environment_id,
        agent=agent_id,
        initial_events=[
            {"type": "user.message", "content": [{"type": "text", "text": "Reply with exactly " + expected}]}
        ],
    )
    context.track("deployment", deployment.id, lambda: client.deployments.archive(deployment.id))
    execution = client.deployments.run(deployment.id)
    if not execution.session_id:
        raise AssertionError("Deployment Run returned no session")
    context.track("session", execution.session_id, lambda: finish_session(client, context, execution.session_id))
    saved = client.deployment_runs.retrieve(execution.id)
    if saved.session_id != execution.session_id:
        raise AssertionError("Deployment Run session ID changed")
    wait_reply(client.sessions.events, context, execution.session_id).verify([expected])


if __name__ == "__main__":
    run_cli("managed", Managed, {"deployment": run})
