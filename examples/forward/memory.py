"""写入项目记忆，在新会话中挂载并验证助手按记忆回答。

运行：python -m examples.forward.memory
"""

from __future__ import annotations

from examples.common.live import ProjectMemory, Run, choose_model, name, run_cli, turn
from qca import Forward

from ._cleanup import finish_session


def run(client: Forward, context: Run) -> None:
    environment = client.environments.create(name=name("env"), config={"type": "cloud"})
    environment_id = context.track("environment", environment.id, lambda: client.environments.archive(environment.id))

    identity = client.identities.create(external_id=name("identity"), name="SDK 示例用户")

    def cleanup_identity() -> None:
        result = client.identities.clear(identity.id, reason="SDK example cleanup")
        if result.status != "completed":
            raise AssertionError("Dedicated Identity cleanup did not complete")
        client.identities.delete(identity.id)

    identity_id = context.track("identity", identity.id, cleanup_identity)

    memory = ProjectMemory()
    store = client.memory_stores.create(name=name("memory"), idempotency_key=name("memory-key"))
    context.track("memory_store", store.id, lambda: client.memory_stores.delete(store.id))
    for path, content in ((memory.path, memory.content()), ("MEMORY.md", memory.index())):
        entry = client.memory_stores.memories.create(store.id, path=path, content=content)
        saved = client.memory_stores.memories.retrieve(entry.id, memory_store_id=store.id)
        if saved.content != content:
            raise AssertionError("Persisted memory does not match the supplied content")
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
    mounts = client.identities.memory_stores.list(template_id, identity_id=identity_id)
    if not any(mount.memory_store_id == store.id for mount in mounts.data):
        raise AssertionError("Memory Store binding was not persisted")
    session = client.sessions.create(
        identity_id=identity_id,
        template_id=template_id,
    )
    session_id = context.track("session", session.id, lambda: finish_session(client, context, session.id))

    turn(client.sessions.events, context, session_id, memory.prompt(), memory.expected())


if __name__ == "__main__":
    run_cli("forward", Forward, {"memory": run})
