"""Search wire contracts from the official API pages, captured 2026-10-27."""

import copy
import importlib
import inspect
import json
from datetime import datetime, timezone
from pathlib import Path

import httpx
import pytest

from qca import AsyncForward, AsyncManaged, Forward, Managed
from qca.common import APIStatusError

FIXTURE = json.loads((Path(__file__).parent / "fixtures/search-contracts.json").read_text())
CASES = FIXTURE["cases"]
BETA = FIXTURE["beta"]


async def resolve(value):
    return await value if inspect.isawaitable(value) else value


def client_for(case, async_, handler, **options):
    cls = {
        ("forward", False): Forward,
        ("forward", True): AsyncForward,
        ("managed", False): Managed,
        ("managed", True): AsyncManaged,
    }[case["mode"], async_]
    http = httpx.AsyncClient if async_ else httpx.Client
    return cls(
        pat="test",
        base_url="https://search.test/",
        http_client=http(transport=httpx.MockTransport(handler)),
        max_retries=0,
        **options,
    )


@pytest.mark.parametrize("async_", [False, True])
@pytest.mark.parametrize("case", CASES, ids=lambda c: c["mode"] + "." + c["resource"])
async def test_search_filters_body_pagination_and_empty_intermediate_page(case, async_):
    expected = copy.deepcopy(case["body"])
    before = copy.deepcopy(expected)
    calls = []

    def handler(request):
        body = json.loads(request.content)
        calls.append(body)
        assert request.method == "POST" and request.url.path == case["path"]
        assert dict(request.url.params) == (
            {"identity_id": "idn +/", "trace": "keep"} if case["mode"] == "forward" else {"trace": "keep"}
        )
        assert set(request.headers["x-qoder-beta"].split(",")) == {"extra-beta", BETA}
        assert request.headers["x-search-test"] == "kept"
        want = {**expected, "page": [expected["page"], "opaque +/=? one", "opaque +/=? two"][len(calls) - 1]}
        assert body == want
        response = copy.deepcopy(case["response"])
        if len(calls) == 2:
            response["data"] = []
        response.update(has_more=len(calls) < 3, next_page=["opaque +/=? one", "opaque +/=? two", None][len(calls) - 1])
        return httpx.Response(200, json=response)

    client = client_for(case, async_, handler, default_headers={"x-qoder-beta": "client-beta"})
    try:
        params = {k.replace("[", "_").replace("]", ""): v for k, v in expected.items()}
        if case["mode"] == "forward":
            params["identity_id"] = "idn +/"
        params.update(
            extra_headers={"X-Qoder-Beta": "extra-beta", "x-search-test": "kept"}, extra_query={"trace": "keep"}
        )
        result = getattr(client, case["resource"]).search(**params)
        items = [item async for item in result] if async_ else list(result)
        assert len(items) == 2 * len(case["response"]["data"])
        assert len(calls) == 3 and expected == before
    finally:
        await resolve(client.close())


@pytest.mark.parametrize("async_", [False, True])
@pytest.mark.parametrize("case", CASES, ids=lambda c: c["mode"] + "." + c["resource"])
async def test_search_no_filters_is_empty_object_and_exported_params(case, async_):
    def handler(request):
        assert request.content == b"{}"
        assert not request.url.query
        assert request.headers["x-qoder-beta"] == "client-beta," + BETA
        return httpx.Response(200, json={"data": [], "has_more": False, "next_page": None, "total": None})

    client = client_for(case, async_, handler, default_headers={"X-Qoder-Beta": "client-beta"})
    try:
        page = await resolve(getattr(client, case["resource"]).search())
        assert not page.has_next_page() and page.total is None
        types = importlib.import_module("qca." + case["mode"] + ".types")
        assert getattr(types, case["service"].removesuffix("Service") + "SearchParams")
    finally:
        await resolve(client.close())


@pytest.mark.parametrize("async_", [False, True])
@pytest.mark.parametrize("status", [400, 403, 429, 503])
async def test_search_errors_keep_request_id(async_, status):
    def handler(request):
        return httpx.Response(
            status,
            headers={"x-request-id": "req_search"},
            json={"error": {"type": "invalid_request_error", "message": "search failed"}},
        )

    client = client_for(CASES[0], async_, handler)
    try:
        with pytest.raises(APIStatusError) as error:
            await resolve(client.environments.search())
        assert error.value.status_code == status and error.value.request_id == "req_search"
    finally:
        await resolve(client.close())


@pytest.mark.parametrize("async_", [False, True])
async def test_search_cursor_does_not_advance(async_):
    calls = []

    def handler(request):
        calls.append(request)
        return httpx.Response(200, json={"data": [], "has_more": True, "next_page": "same"})

    client = client_for(CASES[0], async_, handler)
    try:
        page = await resolve(client.environments.search(page="same"))
        with pytest.raises(RuntimeError, match="did not advance"):
            await resolve(page.get_next_page())
        assert len(calls) == 1
    finally:
        await resolve(client.close())


async def test_search_datetime_and_raw_response():
    def handler(request):
        assert json.loads(request.content) == {"created_at[gte]": "2026-01-01T00:00:00+00:00"}
        return httpx.Response(200, headers={"x-request-id": "req_search"}, json={"data": [], "has_more": False})

    client = client_for(CASES[0], False, handler)
    try:
        raw = client.environments.with_raw_response.search(created_at_gte=datetime(2026, 1, 1, tzinfo=timezone.utc))
        assert raw.headers["x-request-id"] == "req_search"
        assert raw.parse().data == []
    finally:
        client.close()


@pytest.mark.parametrize("async_", [False, True])
async def test_search_retry_and_body_override_keep_filters(async_):
    calls = []

    def handler(request):
        body = json.loads(request.content)
        calls.append(body)
        assert body == {"metadata": {"team": "core"}, "page": "start" if len(calls) <= 2 else "next"}
        assert request.headers["x-qoder-beta"] == BETA
        if len(calls) == 1:
            return httpx.Response(429, headers={"retry-after-ms": "0"}, json={"error": {"message": "retry"}})
        return httpx.Response(
            200, json={"data": [], "has_more": len(calls) == 2, "next_page": "next" if len(calls) == 2 else None}
        )

    cls = AsyncForward if async_ else Forward
    http_cls = httpx.AsyncClient if async_ else httpx.Client
    client = cls(pat="test", http_client=http_cls(transport=httpx.MockTransport(handler)), max_retries=1)
    try:
        page = await resolve(
            client.files.search(
                metadata={"team": "core"}, extra_body={"page": "start"}, extra_headers={"x-qoder-beta": BETA}
            )
        )
        next_page = await resolve(page.get_next_page())
        assert not next_page.has_next_page() and len(calls) == 3
    finally:
        await resolve(client.close())
