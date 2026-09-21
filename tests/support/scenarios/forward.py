"""Forward 综合断言场景（逐字迁自 examples/forward/*.py）。

各场景与 batch_rows 保持原样，仅将对 examples.common.live / examples.forward._cleanup
的 import 改指 tests.support.*；SCENARIOS 顺序与来源一致。
"""

from __future__ import annotations

import json
from typing import Any

import httpx

from qca import Forward
from tests.support.assertions import TurnResult, turn, wait_reply
from tests.support.cleanup import finish_session_forward as finish_session
from tests.support.harness import Run, choose_model, marker, name
from tests.support.memory import ProjectMemory


def models(client: Forward, context: Run) -> None:
    models = client.models.list()
    context.output("models", [{"id": model.id, "is_enabled": model.is_enabled} for model in models.data])
    context.output("selected_model", choose_model(models, context.config.model))


def session(client: Forward, context: Run) -> None:
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


def resources(client: Forward, context: Run) -> None:
    environment = client.environments.create(name=name("env"), config={"type": "cloud"})
    environment_id = context.track("environment", environment.id, lambda: client.environments.archive(environment.id))

    identity = client.identities.create(external_id=name("identity"), name="SDK 示例用户")
    identity_id = context.track("identity", identity.id, lambda: client.identities.delete(identity.id))

    file_value, env_value, skill_value = marker(), marker(), marker()
    file = client.files.upload(file=("sdk-example.txt", file_value.encode()), purpose="session_resource")
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
    template = client.templates.create(
        name=name("template"),
        environment_id=environment_id,
        model=model,
        system="你是一个 SDK 示例助手。必要时调用工具，只使用可实际读取的数据回答问题。",
        tools=[{"type": "agent_toolset_20260401"}],
        skills=[{"type": "custom", "skill_id": skill.id, "version": skill.latest_version}],
        environment_variables={"SDK_EXAMPLE_VALUE": "template-default"},
    )
    template_id = context.track("template", template.id, lambda: client.templates.archive(template.id))

    client.identities.configs.upsert(
        template_id,
        identity_id=identity_id,
        identity_config={"environment_variables": {"SDK_EXAMPLE_VALUE": {"op": "set", "value": env_value}}},
    )
    session = client.sessions.create(
        identity_id=identity_id,
        template_id=template_id,
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


def memory(client: Forward, context: Run) -> None:
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


def schedule(client: Forward, context: Run) -> None:
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

    expected = marker()
    schedule = client.schedules.create(
        identity_id=identity_id,
        template_id=template_id,
        environment_id=environment_id,
        name=name("schedule"),
        initial_events=[{"type": "user.message", "content": "Reply with exactly " + expected}],
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
        if current.status == "completed":
            break
        if current.status in ("failed", "skipped"):
            raise AssertionError(f"Schedule Run failed: {current.status}")
        context.pause()
    if not current.session_id:
        raise AssertionError("Completed Schedule Run has no session")
    context.output("session_id", current.session_id)
    wait_reply(client.sessions.events, context, current.session_id).verify([expected])


def batch(client: Forward, context: Run) -> None:
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

    expected, custom_id = marker(), name("task")
    data = {
        "custom_id": custom_id,
        "template_id": template_id,
        "identity_id": identity_id,
        "body": {"input": "Reply with exactly " + expected},
    }
    input_file = client.files.upload(
        file=("input.jsonl", (json.dumps(data) + "\n").encode()), purpose="session_resource"
    )
    context.track("input_file", input_file.id, lambda: client.files.delete(input_file.id))
    batch = client.batches.create(
        input_file_id=input_file.id,
        completion_window="24h",
        idempotency_key=name("batch"),
        extra_body={"ignore_idle_window": True},
    )
    terminal = {"completed", "failed", "cancelled", "expired"}

    def cleanup_batch() -> None:
        current = client.batches.retrieve(batch.id)
        if current.status not in terminal:
            client.batches.cancel(batch.id)
        while current.status not in terminal:
            context.pause()
            current = client.batches.retrieve(batch.id)
        if not current.output_file_id:
            if current.request_counts and current.request_counts.total == 0:
                return
            raise AssertionError("Batch has no output for session cleanup")
        rows = batch_rows(client, batch.id)
        if (
            len(rows) != 1
            or rows[0].get("custom_id") != custom_id
            or rows[0].get("identity_id") != identity_id
            or rows[0].get("template_id") != template_id
        ):
            raise AssertionError("Batch cleanup output does not match this run")
        if rows[0].get("session_id"):
            finish_session(client, context, rows[0]["session_id"])

    context.track("batch", batch.id, cleanup_batch)
    while batch.status not in terminal:
        context.pause()
        batch = client.batches.retrieve(batch.id)
    if (
        batch.status != "completed"
        or not batch.request_counts
        or batch.request_counts.completed != 1
        or batch.request_counts.failed != 0
        or not batch.output_file_id
    ):
        raise AssertionError("Batch did not complete exactly one successful task")
    tasks = client.batches.tasks.list(batch.id)
    if len(tasks.data) != 1 or tasks.data[0].custom_id != custom_id:
        raise AssertionError("Batch task did not round trip")
    rows = batch_rows(client, batch.id)
    if len(rows) != 1:
        raise AssertionError("Expected one Batch output row")
    row = rows[0]
    context.output("batch_output", row)
    if (
        row.get("custom_id") != custom_id
        or row.get("identity_id") != identity_id
        or row.get("template_id") != template_id
        or row.get("status") != "completed"
        or row.get("error")
        or not row.get("session_id")
    ):
        raise AssertionError("Batch output ownership or status mismatch")
    if expected not in json.dumps(row.get("response")):
        raise AssertionError("Batch response does not contain expected output")
    wait_reply(client.sessions.events, context, row["session_id"]).verify([expected])


def batch_rows(client: Forward, batch_id: str) -> list[dict[str, Any]]:
    link = client.batches.retrieve_output(batch_id)
    url = httpx.URL(link.url)
    if url.scheme not in ("http", "https") or not url.host or url.userinfo:
        raise AssertionError("Invalid Batch output URL")
    # A separate HTTP client prevents API credentials from reaching storage.
    with httpx.Client(timeout=30, follow_redirects=True) as download:
        with download.stream("GET", url) as response:
            response.raise_for_status()
            content = bytearray()
            for chunk in response.iter_bytes():
                content.extend(chunk)
                if len(content) > 4 * 1024 * 1024:
                    raise AssertionError("Batch output exceeds the example's 4 MiB limit")
    return [json.loads(line) for line in content.splitlines() if line.strip()]


SCENARIOS = {
    "models": models,
    "session": session,
    "resources": resources,
    "memory": memory,
    "schedule": schedule,
    "batch": batch,
}
