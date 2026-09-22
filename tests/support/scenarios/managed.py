"""Managed 综合断言场景（逐字迁自 examples/managed/*.py）。

各场景保持原样，仅将对 examples.common.live / examples.managed._cleanup / examples.managed.dream
的 import 改指 tests.support.*；finish_dream 迁至 tests.support.cleanup；SCENARIOS 顺序与来源一致。
"""

from __future__ import annotations

from qca import Managed
from tests.support.assertions import TurnResult, turn, wait_reply
from tests.support.cleanup import finish_dream
from tests.support.cleanup import finish_session_managed as finish_session
from tests.support.harness import Run, choose_model, marker, name
from tests.support.memory import ProjectMemory


def models(client: Managed, context: Run) -> None:
    models = client.models.list()
    context.output("models", [{"id": model.id, "is_enabled": model.is_enabled} for model in models.data])
    context.output("selected_model", choose_model(models, context.config.model))


def session(client: Managed, context: Run) -> None:
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

    session = client.sessions.create(
        environment_id=environment_id,
        agent=agent_id,
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


def resources(client: Managed, context: Run) -> None:
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


def memory(client: Managed, context: Run) -> None:
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


def deployment(client: Managed, context: Run) -> None:
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


def dream(client: Managed, context: Run) -> None:
    model = choose_model(client.models.list(), context.config.model)
    context.output("selected_model", model)
    store = client.memory_stores.create(name=name("dream-input"))
    context.track("input_memory_store", store.id, lambda: client.memory_stores.delete(store.id))
    expected = marker()
    client.memory_stores.memories.create(
        store.id,
        path="sdk-example/source.md",
        content=f"Permanent project verification code: {expected}. Preserve this exact code during consolidation.",
    )
    dream = client.dreams.create(
        inputs=[{"type": "memory_store", "memory_store_id": store.id}],
        model=model,
        instructions="Consolidate supplied memory into sdk-example/consolidated.md. Preserve the exact project verification code. Keep the original source.",
    )
    dream_id = dream.id
    context.track("dream", dream_id, lambda: finish_dream(client, context, dream_id, store.id))
    while dream.status in ("pending", "running"):
        context.pause()
        dream = client.dreams.retrieve(dream_id)
    if dream.status != "completed" or not dream.outputs:
        raise AssertionError(f"Dream did not complete: {dream.status}")
    for output in dream.outputs:
        for memory in client.memory_stores.memories.list(output.memory_store_id):
            if memory.path == "sdk-example/consolidated.md":
                saved = client.memory_stores.memories.retrieve(memory.id, memory_store_id=output.memory_store_id)
                context.output("output_memory_store_id", output.memory_store_id)
                context.output("memory_path", saved.path)
                context.output("memory_content", saved.content)
                if saved.content and expected in saved.content:
                    return
    raise AssertionError("Dream did not persist consolidated memory with the original value")


SCENARIOS = {
    "models": models,
    "session": session,
    "resources": resources,
    "memory": memory,
    "deployment": deployment,
    "dream": dream,
}
