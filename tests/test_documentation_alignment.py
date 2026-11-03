"""Official Forward Session and Managed Memory/Environment/Vault schemas, 2026-11-03."""

import inspect
import json

import httpx
import pytest

from qca import AsyncForward, Forward
from qca.forward.types import SessionEvent
from qca.managed.types import Memory, MemoryListItemUnion, MemoryVersion, SessionThread, Vault


async def resolve(value):
    return await value if inspect.isawaitable(value) else value


@pytest.mark.parametrize("async_", [False, True])
@pytest.mark.parametrize(
    "body",
    [
        {},
        {"budget": None, "config": {"model": None}},
        {"budget": {"type": "limit", "max_credit_cost": "100.00"}, "config": {"model": "ultimate"}},
        {"config": {"model": {"id": "ultimate", "speed": "high", "effort": "none", "context_window": 200000}}},
    ],
)
async def test_forward_update_budget_and_model_three_states(async_, body):
    def handle(request):
        assert json.loads(request.content) == body
        return httpx.Response(200, json={"id": "sess_test", **body})

    http = (httpx.AsyncClient if async_ else httpx.Client)(transport=httpx.MockTransport(handle))
    client = (AsyncForward if async_ else Forward)(pat="test", http_client=http, _strict_response_validation=True)
    try:
        session = await resolve(client.sessions.update("sess_test", **body))
        assert ("budget" in session.model_fields_set) == ("budget" in body)
        if body.get("budget"):
            assert session.budget.max_credit_cost == "100.00"
        if body.get("config", {}).get("model") is None:
            if session.config:
                assert session.config.model is None
        elif isinstance(body["config"]["model"], str):
            assert session.config.model == "ultimate"
        else:
            assert session.config.model.speed == "high"
            assert "speed" in type(session.config.model).model_fields
    finally:
        await resolve(client.close())


@pytest.mark.parametrize("async_", [False, True])
@pytest.mark.parametrize("budget", [{"type": "limit", "max_credit_cost": "100.00"}, None])
async def test_forward_create_keeps_budget_and_metadata(async_, budget):
    metadata = {"business": "kept"}
    config = {"model": {"id": "ultimate", "speed": "high"}}

    def handle(request):
        body = json.loads(request.content)
        assert body["budget"] == budget
        assert body["config"] == config
        assert body["metadata"]["business"] == "kept"
        assert body["metadata"]["__qca_sdk_created"] == "true"
        return httpx.Response(200, json=body)

    http = (httpx.AsyncClient if async_ else httpx.Client)(transport=httpx.MockTransport(handle))
    client = (AsyncForward if async_ else Forward)(pat="test", http_client=http, _strict_response_validation=True)
    try:
        await resolve(
            client.sessions.create(
                identity_id="idn", template_id="tmpl", budget=budget, config=config, metadata=metadata
            )
        )
        assert metadata == {"business": "kept"}
    finally:
        await resolve(client.close())


@pytest.mark.parametrize(
    "result,policy,reason",
    [
        ("allow", "always_allow", None),
        ("ask", "always_ask", None),
        ("allow", "auto", None),
        ("ask", "auto", "indeterminate"),
        ("deny", "auto", "high_risk"),
    ],
)
def test_approval_root_and_nested_details(result, policy, reason):
    evaluation = {"type": policy}
    if policy == "auto":
        evaluation["evaluated_permission"] = {"type": result}
        if reason:
            evaluation["evaluated_permission"]["reason_code"] = reason
    event = SessionEvent.model_validate({"evaluated_permission": result, "evaluation": evaluation, "future": 17})
    assert event.evaluated_permission == result
    assert event.evaluation.type == policy
    if policy == "auto":
        assert event.evaluation.evaluated_permission.type == result
        assert event.evaluation.evaluated_permission.reason_code == reason
    else:
        assert event.evaluation.evaluated_permission is None
    assert event.model_extra == {"future": 17}


@pytest.mark.parametrize("async_", [False, True])
async def test_forward_history_and_both_streams_use_typed_event_fields(async_):
    events = [
        {"id": "zero", "type": "session.usage", "model_credits": 0, "sandbox_runtime_credits": 0, "total_credits": 0},
        {
            "id": "usage",
            "type": "session.usage",
            "model_credits": 0.68,
            "sandbox_runtime_credits": 0.04,
            "total_credits": 0.72,
        },
        {"id": "idle", "type": "session.status_idle", "reason": "outcome_evaluation"},
        {
            "id": "end",
            "type": "span.outcome_evaluation_end",
            "iteration": 2,
            "explanation": "done",
            "outcome_evaluation_start_id": "start",
        },
        {"id": "clear", "type": "session.updated", "budget": None},
        {"id": "set", "type": "session.updated", "budget": {"type": "limit", "max_credit_cost": "0.01"}},
    ]

    def handle(request):
        if request.url.path.endswith("/stream"):
            return httpx.Response(
                200,
                text="".join(f"id: {e['id']}\ndata: {json.dumps(e)}\n\n" for e in events),
                headers={"Content-Type": "text/event-stream"},
            )
        return httpx.Response(200, json={"data": events, "has_more": False})

    def check(items):
        assert items[0].total_credits == 0
        assert items[1].total_credits == 0.72
        assert items[1].model_credits == 0.68
        assert items[1].sandbox_runtime_credits == 0.04
        assert items[2].reason == "outcome_evaluation"
        assert items[3].iteration == 2 and items[3].explanation == "done"
        assert items[3].outcome_evaluation_start_id == "start"
        assert items[4].budget is None and "budget" in items[4].model_fields_set
        assert "budget" not in items[0].model_fields_set
        assert items[5].budget.max_credit_cost == "0.01"
        for item in items:
            assert not item.model_extra

    http = (httpx.AsyncClient if async_ else httpx.Client)(transport=httpx.MockTransport(handle))
    client = (AsyncForward if async_ else Forward)(pat="test", http_client=http, _strict_response_validation=True)
    try:
        check((await resolve(client.sessions.events.list("s"))).data)
        for stream in [
            await resolve(client.sessions.events.stream("s")),
            await resolve(client.sessions.threads.events.stream("t", session_id="s")),
        ]:
            try:
                check([e async for e in stream] if async_ else list(stream))
            finally:
                await resolve(stream.close())
    finally:
        await resolve(client.close())


def test_managed_memory_vault_and_legacy_usage():
    payload = {"version": 2, "metadata": {"source": "test"}}
    for model in [Memory, MemoryListItemUnion]:
        item = model.model_validate(payload)
        assert item.version == 2 and item.metadata == {"source": "test"}
        assert not item.model_extra
    for redacted in [False, True]:
        version = MemoryVersion.model_validate({"operation": "updated", "redacted": redacted})
        assert version.operation == "updated" and version.redacted is redacted
        assert not version.model_extra
    assert Vault.model_validate({"credentials": []}).credentials == []
    assert "credentials" in Vault.model_fields
    assert SessionThread.model_fields["usage"].deprecated
    assert "usage" not in SessionThread.model_validate({"id": "t"}).model_fields_set


def test_environment_startup_script_is_typed_and_preserved():
    from qca.forward.types import EnvironmentConfig
    from qca.managed.types import CloudConfigParams, EnvironmentConfigUnion, SelfHostedConfigParams

    script = "#!/bin/sh\necho ready\n"
    for model in [EnvironmentConfig, EnvironmentConfigUnion]:
        config = model.model_validate({"type": "cloud", "startup_script": script})
        assert config.startup_script == script
        assert not config.model_extra
    assert "startup_script" in CloudConfigParams.__annotations__
    assert "startup_script" in SelfHostedConfigParams.__annotations__
