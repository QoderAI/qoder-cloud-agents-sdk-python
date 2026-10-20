"""Existing API contracts from docs.qoder.com/cloud-agents/api, 2026-10-20."""

import inspect
import json
from pathlib import Path

import httpx
import pytest

from qca import AsyncForward, AsyncManaged, Forward, Managed
from qca.forward import types as ft
from qca.managed import types as mt

FIXTURE = json.loads((Path(__file__).parent / "fixtures/contract-alignment-0.8.json").read_text())


async def resolve(value):
    return await value if inspect.isawaitable(value) else value


@pytest.mark.parametrize("async_", [False, True])
async def test_forward_request_contracts(async_):
    calls = []

    def handle(req):
        body = json.loads(req.content) if req.content else None
        calls.append((req, body))
        if req.method == "GET":
            assert req.url.params["search"] == "report & 中文"
            assert body is None
            return httpx.Response(200, json={"data": [], "has_more": False})
        if req.url.path.endswith("/batches"):
            return httpx.Response(
                200, json={"ignore_idle_window": body.get("ignore_idle_window", False), "queue_reason": "capacity"}
            )
        return httpx.Response(200, json={"id": "contract_one", **body})

    http = (httpx.AsyncClient if async_ else httpx.Client)(transport=httpx.MockTransport(handle))
    client = (AsyncForward if async_ else Forward)(pat="test", http_client=http, _strict_response_validation=True)
    try:
        for limits in [{}, {"max_tool_rounds": None}, {"max_tool_rounds": 3}]:
            base = {"name": "sdk-contract", "model": "model", "environment_id": "env_one"}
            await resolve(client.templates.create(**base, **limits))
            assert calls[-1][1] == {**base, **limits}
            await resolve(client.templates.update("tmpl_one", **limits))
            assert calls[-1][1] == limits
        for flag in [{}, {"ignore_idle_window": False}, {"ignore_idle_window": True}]:
            base = {"input_file_id": "file_one", "completion_window": "24h"}
            batch = await resolve(client.batches.create(**base, **flag))
            assert calls[-1][1] == {**base, **flag}
            assert batch.ignore_idle_window is flag.get("ignore_idle_window", False)
            assert batch.queue_reason == "capacity"
        await resolve(client.sessions.list(search="report & 中文"))
        before = len(calls)
        for _ in range(2):
            await resolve(
                client.memory_stores.create(name="sdk-contract", mount=FIXTURE["mount"], idempotency_key="mount-one")
            )
            assert calls[-1][0].headers["Idempotency-Key"] == "mount-one"
            assert calls[-1][1] == {"name": "sdk-contract", "mount": FIXTURE["mount"]}
        assert len(calls) == before + 2  # One server operation per create, including replay.
    finally:
        await resolve(client.close())


@pytest.mark.parametrize("async_", [False, True])
async def test_managed_resource_and_setup_contracts(async_):
    calls = []

    def handle(req):
        body = json.loads(req.content)
        calls.append(body)
        return httpx.Response(200, json={"id": "contract_one"})

    http = (httpx.AsyncClient if async_ else httpx.Client)(transport=httpx.MockTransport(handle))
    client = (AsyncManaged if async_ else Managed)(pat="test", http_client=http, _strict_response_validation=True)
    resources = [FIXTURE["git"], FIXTURE["github"]]
    try:
        await resolve(client.sessions.create(agent="agent_one", environment_id="env_one", resources=resources))
        assert calls[-1]["resources"] == resources
        await resolve(
            client.deployments.create(
                agent="agent_one", environment_id="env_one", name="sdk-contract", initial_events=[], resources=resources
            )
        )
        assert calls[-1]["resources"] == resources
        await resolve(client.deployments.update("dep_one", resources=resources))
        assert calls[-1] == {"resources": resources}
        config = FIXTURE["environment"]["config"]
        await resolve(client.environments.create(name="sdk-contract", config=config))
        assert calls[-1] == {"name": "sdk-contract", "config": config}
        await resolve(client.environments.update("env_one", config=config))
        assert calls[-1] == {"config": config}
        await resolve(
            client.sessions.resources.update("sesr_one", session_id="sess_one", password=" token with spaces ")
        )
        assert calls[-1] == {"password": " token with spaces "}
    finally:
        await resolve(client.close())


def test_typed_response_contracts():
    session = ft.Session.model_validate(FIXTURE["session"])
    assert session.outcome_evaluations[0].iteration == 0
    assert session.outcome_evaluations[0].explanation is None
    assert "outcome_evaluations" in ft.Session.model_fields
    thread = ft.SessionThread.model_validate(FIXTURE["thread"])
    assert thread.stats.active_seconds == thread.stats.startup_seconds == thread.usage.total_credits == 0
    assert ft.SessionThread.model_validate({"id": "empty"}).usage is None
    schedule = ft.Schedule.model_validate(FIXTURE["schedule"])
    assert schedule.source == "api" and schedule.source_session_id is None
    assert schedule.initial_events_version == 2
    assert schedule.trigger_policy.start_at.day == 20
    assert schedule.trigger_policy.stop_at.day == 21
    assert schedule.trigger_policy.last_run_at is None
    run = ft.ScheduleRun.model_validate(FIXTURE["run"])
    assert run.source == "tool" and run.source_session_id == "sess_one"
    assert run.initial_events_version is None
    for cls in [ft.Environment, mt.Environment]:
        env = cls.model_validate(FIXTURE["environment"])
        assert env.config.setup_script == "echo sdk-contract"
        assert "setup_script" in type(env.config).model_fields
    assert ft.Environment.model_validate(FIXTURE["environment"]).binding_info.agent_template_count == 0
    memory = mt.MemoryStore.model_validate(FIXTURE["memory_store"])
    assert memory.status == "active" and memory.entry_count == memory.total_size == 0
    assert mt.Dream.model_validate(FIXTURE["dream"]).outputs[0].files_touched == ["notes.md", "summary.md"]
    assert ft.Skill.model_validate({"latest_version": None}).latest_version is None
    assert mt.Skill.model_validate({"latest_version": None}).latest_version is None


@pytest.mark.parametrize("async_", [False, True])
async def test_artifact_and_diagnostic_history_and_streams(async_):
    events = FIXTURE["events"]

    def handle(req):
        if req.url.path.endswith("/stream"):
            wire = "".join(f"id: {e['id']}\nevent: {e['type']}\ndata: {json.dumps(e)}\n\n" for e in events)
            return httpx.Response(200, text=wire, headers={"Content-Type": "text/event-stream"})
        return httpx.Response(200, json={"data": events, "has_more": False})

    http = (httpx.AsyncClient if async_ else httpx.Client)(transport=httpx.MockTransport(handle))
    client = (AsyncManaged if async_ else Managed)(pat="test", http_client=http, _strict_response_validation=True)

    def check(items):
        artifact, error = items
        assert artifact.file_id == "file_one" and artifact.size == 0
        assert artifact.original_filename == "report.txt" and artifact.content_type == "text/plain"
        assert "file_id" in type(artifact).model_fields
        assert error.error.qoder_error_code == "TEST_DIAGNOSTIC"
        assert "qoder_error_code" in type(error.error).model_fields
        assert error.error.retry_status.type == "terminal"

    try:
        check((await resolve(client.sessions.events.list("sess_one"))).data)
        for stream in [
            await resolve(client.sessions.events.stream("sess_one")),
            await resolve(client.sessions.threads.events.stream("sthr_one", session_id="sess_one")),
        ]:
            check([e async for e in stream] if async_ else list(stream))
    finally:
        await resolve(client.close())
