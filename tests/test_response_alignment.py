from __future__ import annotations

import inspect
from datetime import date, datetime, timezone
from email.utils import formatdate

import httpx
import pytest
from pydantic import Field

import qca
import qca.common
from qca import APIResponseValidationError, APIStatusError, AsyncForward, AsyncManaged, Forward, Managed
from qca.common._models import BaseModel, parse_response

# Shared response semantics: anthropics/anthropic-sdk-python v1.7.0,
# commit 0af0190679a9e80388bd1b0328d557c9a91a11b2 (_models.py and _base_client.py).
# Retry eligibility remains QCA-specific; these tests cover the delay once a retry is allowed.


async def resolve(value):
    return await value if inspect.isawaitable(value) else value


@pytest.fixture(params=[Forward, Managed, AsyncForward, AsyncManaged])
async def make_client(request):
    clients = []

    def make(handler, **kwargs):
        http_cls = httpx.AsyncClient if request.param in (AsyncForward, AsyncManaged) else httpx.Client
        client = request.param(
            pat="test-token",
            http_client=http_cls(transport=httpx.MockTransport(handler)),
            **kwargs,
        )
        clients.append(client)
        return client

    yield make
    for client in clients:
        await resolve(client.close())


@pytest.mark.parametrize("status,name", [(413, "RequestTooLargeError"), (529, "OverloadedError")])
async def test_status_error_types_and_metadata(make_client, status, name):
    body = {"error": {"message": "rejected", "type": "upstream_error", "code": "test-code"}}
    client = make_client(
        lambda _: httpx.Response(status, json=body, headers={"request-id": "req-status"}), max_retries=0
    )
    error_cls = getattr(qca, name)
    assert error_cls is getattr(qca.common, name)
    assert error_cls.__bases__ == (APIStatusError,)
    with pytest.raises(error_cls) as caught:
        await resolve(client.models.list())
    error = caught.value
    assert type(error) is error_cls
    assert error.status_code == status
    assert error.request_id == "req-status"
    assert error.body == body
    assert (error.type, error.code) == ("upstream_error", "test-code")
    assert error.response.request is error.request


@pytest.mark.parametrize(
    "headers,expected",
    [
        ({"retry-after": "120"}, 120),
        ({"retry-after": "0.25"}, 0.25),
        ({"retry-after-ms": "125000", "retry-after": "120"}, 125),
        ({"retry-after-ms": "bad", "retry-after": "120"}, 120),
        ({"retry-after": formatdate(1_700_000_120, usegmt=True)}, 120),
        ({"retry-after": "999999999999"}, 4_294_967),
        ({"retry-after-ms": "999999999999999"}, 4_294_967),
        ({"retry-after": "inf"}, 4_294_967),
        ({"retry-after": "0"}, 0.5),
        ({"retry-after": "-1"}, 0.5),
        ({"retry-after": "nan"}, 0.5),
        ({"retry-after": "invalid"}, 0.5),
        ({"retry-after": formatdate(1_699_999_999, usegmt=True)}, 0.5),
        ({"retry-after-ms": "0", "retry-after": "120"}, 0.5),
        ({"retry-after-ms": "-1", "retry-after": "120"}, 0.5),
        ({"retry-after-ms": formatdate(1_700_000_120, usegmt=True)}, 0.5),
        ({}, 0.5),
    ],
)
async def test_server_retry_delay_reaches_sync_and_async_sleep(make_client, monkeypatch, headers, expected):
    sleeps = []

    async def async_sleep(delay):
        sleeps.append(delay)

    monkeypatch.setattr("qca.common._base_client.time.sleep", sleeps.append)
    monkeypatch.setattr("qca.common._base_client.anyio.sleep", async_sleep)
    monkeypatch.setattr("qca.common._base_client.time.time", lambda: 1_700_000_000)
    monkeypatch.setattr("qca.common._base_client.random.random", lambda: 0)
    calls = []

    def handler(request):
        calls.append(request)
        return httpx.Response(429 if len(calls) == 1 else 200, headers=headers, json={"data": []})

    client = make_client(handler, max_retries=1)
    await resolve(client.models.list())
    assert sleeps == [expected]
    assert len(calls) == 2


async def read_models(client, view):
    if view == "raw":
        return await resolve((await resolve(client.models.with_raw_response.list())).parse())
    if view == "streaming_response":
        manager = client.models.with_streaming_response.list()
        if hasattr(manager, "__aenter__"):
            async with manager as response:
                return await response.parse()
        with manager as response:
            return response.parse()
    return await resolve(client.models.list())


@pytest.mark.parametrize("strict", [False, True])
@pytest.mark.parametrize("view", ["normal", "raw", "streaming_response"])
async def test_response_validation_modes_survive_client_and_response_views(make_client, strict, view):
    payload = {"data": [{"id": "model-1", "is_enabled": "future-value", "future_field": "kept"}]}
    # Omitting the option must select lenient construction.
    options = {"_strict_response_validation": True} if strict else {}
    client = make_client(
        lambda _: httpx.Response(200, json=payload, headers={"x-request-id": "req-model"}), **options
    ).with_options(timeout=30)
    if strict:
        with pytest.raises(APIResponseValidationError) as caught:
            await read_models(client, view)
        assert caught.value.body == payload
        assert caught.value.status_code == 200
        assert caught.value.response.headers["x-request-id"] == "req-model"
    else:
        result = await read_models(client, view)
        assert isinstance(result, BaseModel)
        assert isinstance(result.data[0], BaseModel)
        assert result.data[0].id == "model-1"
        assert result.data[0].is_enabled == "future-value"
        assert result.data[0].future_field == "kept"
        assert result._request_id == "req-model"


@pytest.mark.parametrize("strict", [False, True])
async def test_validation_mode_survives_raw_pagination_followup(make_client, strict):
    requests = []

    def handler(request):
        requests.append(request)
        if len(requests) == 1:
            return httpx.Response(
                200,
                json={"data": [{"id": "sess-1"}], "has_more": True, "last_id": "sess-1", "next_page": "sess-1"},
            )
        return httpx.Response(200, json={"data": [{"id": {"future": "shape"}}], "has_more": False})

    client = make_client(handler, _strict_response_validation=strict)
    raw = await resolve(client.sessions.with_raw_response.list())
    page = await resolve(raw.parse())
    assert page.data[0].id == "sess-1"
    if strict:
        with pytest.raises(APIResponseValidationError):
            await resolve(page.get_next_page())
    else:
        page = await resolve(page.get_next_page())
        assert isinstance(page.data[0], BaseModel)
        assert page.data[0].id == {"future": "shape"}
        assert not page.has_next_page()
    cursor_key = "page" if isinstance(client, (Managed, AsyncManaged)) else "after_id"
    assert requests[1].url.params[cursor_key] == "sess-1"


@pytest.mark.parametrize("strict", [False, True])
async def test_sse_uses_response_validation_mode(make_client, strict):
    client = make_client(
        lambda _: httpx.Response(
            200,
            headers={"content-type": "text/event-stream", "request-id": "req-sse"},
            text='id: evt-1\nevent: custom\ndata: {"id": "evt-1", "type": "custom", "result": {"new": "shape"}}\n\n',
        ),
        _strict_response_validation=strict,
    )
    stream = await resolve(client.with_options(timeout=30).sessions.events.stream("sess-1"))

    async def read_event():
        return await stream.__anext__() if hasattr(stream, "__anext__") else next(stream)

    try:
        if strict:
            with pytest.raises(APIResponseValidationError):
                await read_event()
            assert stream.last_event_id is None
        else:
            event = await read_event()
            assert event.result == {"new": "shape"}
            assert event._request_id == "req-sse"
            assert stream.last_event_id == "evt-1"
    finally:
        await resolve(stream.close())


class Child(BaseModel):
    count: int


class Document(BaseModel):
    title: str = Field(alias="apiTitle")
    child: Child
    children: list[Child] = Field(default_factory=list)
    by_name: dict[str, Child] = Field(default_factory=dict)
    created_at: datetime | None = None
    day: date | None = None
    score: float | None = None


def test_lenient_construction_preserves_nested_models_aliases_dates_extras_and_field_presence():
    payload = {
        "apiTitle": 42,
        "child": {"count": "future-count", "extra": True},
        "children": [{"count": 1}, {"count": "future-count"}],
        "by_name": {"example": {"count": "future-count"}},
        "created_at": "2026-09-24T00:00:00Z",
        "day": "2026-09-24",
        "score": 2,
        "extra": "kept",
    }
    response = httpx.Response(200, request=httpx.Request("GET", "https://api.test/"))
    result = parse_response(Document, payload, response)
    assert result.title == 42
    assert isinstance(result.child, Child)
    assert result.child.count == "future-count"
    assert result.child.extra is True
    assert all(isinstance(child, Child) for child in result.children)
    assert result.children[1].count == "future-count"
    assert result.by_name["example"].count == "future-count"
    assert result.created_at == datetime(2026, 9, 24, tzinfo=timezone.utc)
    assert result.day == date(2026, 9, 24)
    assert type(result.score) is float
    assert result.extra == "kept"
    assert result.model_fields_set == (payload.keys() - {"apiTitle", "extra"}) | {"title"}
    missing = parse_response(Document, {}, response)
    assert missing.title is None
    assert missing.child is None
    assert missing.children == []
    assert missing.by_name == {}
    assert missing.to_dict() == {}
    missing.children.append(Child(count=1))
    assert parse_response(Document, {}, response).children == []


@pytest.mark.parametrize("value", [None, "different-shape", 123, []])
def test_lenient_construction_preserves_unexpected_top_level_shapes(value):
    assert parse_response(Child, value, httpx.Response(200)) == value


def test_lenient_construction_preserves_invalid_container_and_date_fields():
    payload = {"children": {"new": "shape"}, "by_name": [], "created_at": "not-a-date", "day": "not-a-day"}
    result = parse_response(Document, payload, httpx.Response(200))
    assert result.children == {"new": "shape"}
    assert result.by_name == []
    assert result.created_at == "not-a-date"
    assert result.day == "not-a-day"
