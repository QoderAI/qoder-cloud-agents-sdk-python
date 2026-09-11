"""上传文件与 Skill，挂载到会话，并验证环境变量与工具调用。

运行：python -m examples.managed.resources
"""

from __future__ import annotations

from examples.common.live import Run, choose_model, marker, name, run_cli, turn
from qca import Managed

from ._cleanup import finish_session


def run(client: Managed, context: Run) -> None:
    environment = client.environments.create(name=name("env"), config={"type": "cloud"})
    environment_id = context.track("environment", environment.id, lambda: client.environments.archive(environment.id))

    file_value, env_value, skill_value = marker(), marker(), marker()
    file = client.files.upload(file=("sdk-example.txt", file_value.encode()))
    context.track("file", file.id, lambda: client.files.delete(file.id))
    skill_name = name("skill")
    skill = client.skills.create(
        files=[
            (
                f"{skill_name}/SKILL.md",
                f"---\nname: {skill_name}\ndescription: SDK example verification code.\n---\nEXAMPLE_SKILL_CODE: {skill_value}\n".encode(),
            )
        ]
    )
    context.track("skill", skill.id, lambda: client.skills.delete(skill.id))
    model = choose_model(client.models.list(), context.config.model)
    context.output("selected_model", model)
    agent = client.agents.create(
        name=name("agent"),
        model={"id": model},
        system="你是一个 SDK 示例助手。必要时调用工具，只使用可实际读取的数据回答问题。",
        tools=[{"type": "agent_toolset_20260401"}],
        skills=[{"type": "custom", "skill_id": skill.id, "version": skill.latest_version}],
    )
    agent_id = context.track("agent", agent.id, lambda: client.agents.archive(agent.id))

    session = client.sessions.create(
        environment_id=environment_id,
        agent=agent_id,
        environment_variables={"SDK_EXAMPLE_VALUE": env_value},
        resources=[{"type": "file", "file_id": file.id, "mount_path": "/data/workspace/sdk-example.txt"}],
    )
    session_id = context.track("session", session.id, lambda: finish_session(client, context, session.id))

    turn(
        client.sessions.events,
        context,
        session_id,
        "请使用工具读取 /data/workspace/sdk-example.txt 和 SDK_EXAMPLE_VALUE 环境变量，返回两个值。",
        [file_value, env_value],
        require_tool=True,
    )
    turn(
        client.sessions.events,
        context,
        session_id,
        f"请使用技能 {skill_name}，读取并返回 EXAMPLE_SKILL_CODE。",
        [skill_value],
        require_tool=True,
    )


if __name__ == "__main__":
    run_cli("managed", Managed, {"resources": run})
