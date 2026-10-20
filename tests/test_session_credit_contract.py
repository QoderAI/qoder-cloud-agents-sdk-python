"""Official session schemas, retrieved 2026-10-20; no service credentials needed."""

import inspect
import json

import httpx
import pytest

from qca import AsyncForward, AsyncManaged, Forward, Managed


async def resolve(value):
    return await value if inspect.isawaitable(value) else value


@pytest.mark.parametrize("async_", [False, True])
@pytest.mark.parametrize("body", [{"budget": {"type": "limit", "max_credit_cost": "100.00"}}, {}, {"budget": None}])
async def test_budget_decimal_omission_and_clear(async_, body):
    def handle(req):
        assert json.loads(req.content) == body
        return httpx.Response(200, json={"id": "sess_one", **body})

    http = (httpx.AsyncClient if async_ else httpx.Client)(transport=httpx.MockTransport(handle))
    client = (AsyncManaged if async_ else Managed)(pat="test", http_client=http, _strict_response_validation=True)
    try:
        session = await resolve(client.sessions.update("sess_one", **body))
        if body.get("budget"):
            assert session.budget.max_credit_cost == "100.00"
    finally:
        await resolve(client.close())


@pytest.mark.parametrize("async_", [False, True])
@pytest.mark.parametrize("forward", [False, True])
async def test_session_credit_snapshot_and_absence(async_, forward):
    usage = {"model_credits": 7.66, "sandbox_runtime_credits": 0.34, "total_credits": 8}

    def handle(req):
        return httpx.Response(
            200, json={"id": "sess_one", **({"usage": usage} if req.url.path.endswith("sess_one") else {})}
        )

    http = (httpx.AsyncClient if async_ else httpx.Client)(transport=httpx.MockTransport(handle))
    client_type = (AsyncForward if async_ else Forward) if forward else (AsyncManaged if async_ else Managed)
    client = client_type(pat="test", http_client=http, _strict_response_validation=True)
    try:
        session = await resolve(client.sessions.retrieve("sess_one"))
        assert session.usage.model_credits == 7.66
        assert session.usage.sandbox_runtime_credits == 0.34
        assert session.usage.total_credits == 8
        assert "model_credits" in type(session.usage).model_fields
        empty = await resolve(client.sessions.retrieve("sess_empty"))
        assert empty.usage is None
    finally:
        await resolve(client.close())


@pytest.mark.parametrize("async_", [False, True])
async def test_credit_events_in_history_and_streams(async_):
    events = [
        {
            "id": "evt_1",
            "type": "session.usage",
            "model_credits": 7.66,
            "sandbox_runtime_credits": 0.34,
            "total_credits": 8,
        },
        {"id": "evt_2", "type": "agent.thread_context_compacted", "usage": {"credits": 0}},
        {"id": "evt_3", "type": "span.model_request_end", "model_usage": {"credits": 1.25}},
    ]

    def handle(req):
        if req.url.path.endswith("/stream"):
            wire = "".join(f"id: {e['id']}\nevent: {e['type']}\ndata: {json.dumps(e)}\n\n" for e in events)
            return httpx.Response(200, text=wire, headers={"Content-Type": "text/event-stream"})
        return httpx.Response(200, json={"data": events, "has_more": False, "next_page": None})

    http = (httpx.AsyncClient if async_ else httpx.Client)(transport=httpx.MockTransport(handle))
    client = (AsyncManaged if async_ else Managed)(pat="test", http_client=http, _strict_response_validation=True)

    def check(items):
        assert items[0].model_credits == 7.66 and items[0].total_credits == 8
        assert "total_credits" in type(items[0]).model_fields
        assert items[1].usage.credits == 0
        assert "credits" in type(items[1].usage).model_fields
        assert items[2].model_usage.credits == 1.25

    try:
        page = await resolve(client.sessions.events.list("sess_one"))
        check(page.data)
        stream = await resolve(client.sessions.events.stream("sess_one"))
        check([e async for e in stream] if async_ else list(stream))
        thread_stream = await resolve(client.sessions.threads.events.stream("thread_one", session_id="sess_one"))
        check([e async for e in thread_stream] if async_ else list(thread_stream))
    finally:
        await resolve(client.close())
