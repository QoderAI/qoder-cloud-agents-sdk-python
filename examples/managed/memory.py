"""写入项目记忆，在新会话中挂载并验证助手按记忆回答。

运行：python -m examples.managed.memory
"""

from __future__ import annotations

from examples.common.live import ProjectMemory, Run, choose_model, name, run_cli, turn
from qca import Managed

from ._cleanup import finish_session


def run(client: Managed, context: Run) -> None:
    environment = client.environments.create(name=name("env"), config={"type": "cloud"})
    environment_id = context.track("environment", environment.id, lambda: client.environments.archive(environment.id))

    memory = ProjectMemory()
    store = client.memory_stores.create(name=name("memory"))
    context.track("memory_store", store.id, lambda: client.memory_stores.delete(store.id))
    for path, content in ((memory.path, memory.content()), ("MEMORY.md", memory.index())):
        entry = client.memory_stores.memories.create(store.id, path=path, content=content)
        saved = client.memory_stores.memories.retrieve(entry.id, memory_store_id=store.id)
        if saved.content != content:
            raise AssertionError("Persisted memory does not match the supplied content")
    model = choose_model(client.models.list(), context.config.model)
    context.output("selected_model", model)
    agent = client.agents.create(
        name=name("agent"),
        model={"id": model},
        system="你是一个 SDK 示例助手。必要时调用工具，只使用可实际读取的数据回答问题。",
        tools=[{"type": "agent_toolset_20260401"}],
    )
    agent_id = context.track("agent", agent.id, lambda: client.agents.archive(agent.id))

    session = client.sessions.create(
        environment_id=environment_id,
        agent=agent_id,
        resources=[{"type": "memory_store", "memory_store_id": store.id, "access": "read_only"}],
    )
    session_id = context.track("session", session.id, lambda: finish_session(client, context, session.id))

    if not any(
        resource.type == "memory_store" and resource.memory_store_id == store.id
        for resource in client.sessions.resources.list(session_id)
    ):
        raise AssertionError("Memory Store is not mounted in the new session")
    turn(client.sessions.events, context, session_id, memory.prompt(), memory.expected())


if __name__ == "__main__":
    run_cli("managed", Managed, {"memory": run})
