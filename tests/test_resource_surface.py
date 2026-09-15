"""Every public resource method, exercised once against a mock transport.

The checks read each method's own route declaration and signature, so a new
endpoint is covered as soon as it is added, and a method that stops sending what
it accepts fails here rather than in production.
"""

import inspect
from functools import cached_property

import httpx
import pytest

from qca import Forward, NotFoundError
from qca.common._types import NOT_GIVEN

from ._surface import (
    ENDPOINTS,
    TOKEN,
    call,
    carriers,
    client_for,
    close_client,
    endpoint_id,
    method_names,
    plain_client,
    release,
    responder,
)

MODES = ("forward", "managed")


@pytest.mark.parametrize("endpoint", ENDPOINTS, ids=endpoint_id)
@pytest.mark.parametrize("async_", [False, True], ids=["sync", "async"])
async def test_endpoint_sends_its_documented_request(endpoint, async_):
    recorded = []
    client = client_for(endpoint, async_, responder(recorded, endpoint))
    try:
        result = await call(endpoint, client, raw=True)
        await release(result, async_)
    finally:
        await close_client(client, async_)

    request = recorded[0]
    assert request.method == endpoint.verb
    assert request.url.path == f"/api/v1/{endpoint.mode}{endpoint.path}"
    assert request.headers["authorization"] == f"Bearer {TOKEN}"
    assert request.headers["user-agent"].startswith("qca-python/")
    expected_accept = "text/event-stream" if endpoint.kind == "stream" else "application/json"
    assert request.headers["accept"] == expected_accept
    for name, value in endpoint.inputs.items():
        assert carriers(request, name, value), f"{name} never reached the request"


@pytest.mark.parametrize("endpoint", ENDPOINTS, ids=endpoint_id)
@pytest.mark.parametrize("async_", [False, True], ids=["sync", "async"])
async def test_endpoint_returns_its_annotated_type(endpoint, async_):
    client = client_for(endpoint, async_, responder([], endpoint))
    try:
        result = await call(endpoint, client)
        expected = endpoint.response_type(async_)
        assert result is None if endpoint.nullable and result is None else isinstance(result, expected)
        await release(result, async_)
    finally:
        await close_client(client, async_)


@pytest.mark.parametrize("endpoint", ENDPOINTS, ids=endpoint_id)
@pytest.mark.parametrize("async_", [False, True], ids=["sync", "async"])
async def test_endpoint_raises_typed_errors(endpoint, async_):
    client = client_for(endpoint, async_, responder([], endpoint, status=404))
    try:
        with pytest.raises(NotFoundError) as raised:
            await release(await call(endpoint, client), async_)
        assert raised.value.status_code == 404
        assert raised.value.request_id == "req-surface"
    finally:
        await close_client(client, async_)


@pytest.mark.parametrize("endpoint", [e for e in ENDPOINTS if e.path_params], ids=endpoint_id)
@pytest.mark.parametrize(
    "value,encoded",
    [
        ("", None),
        (".", None),
        ("..", None),
        ("with/slash", "with%2Fslash"),
        ("空 格", "%E7%A9%BA%20%E6%A0%BC"),
        ("a?b#c", "a%3Fb%23c"),
    ],
    ids=["empty", "dot", "dotdot", "slash", "unicode", "delimiters"],
)
async def test_path_parameters_are_encoded_or_rejected(endpoint, value, encoded):
    name = endpoint.path_params[0]
    recorded = []
    client = client_for(endpoint, False, responder(recorded, endpoint))
    try:
        if encoded is None:
            with pytest.raises(ValueError):
                await call(endpoint, client, **{name: value})
            assert recorded == []
            return
        await release(await call(endpoint, client, raw=True, **{name: value}), False)
        assert encoded in recorded[0].url.raw_path.decode().split("?")[0].split("/")
    finally:
        await close_client(client, False)


@pytest.mark.parametrize("mode", MODES)
async def test_sync_and_async_clients_expose_the_same_methods(mode):
    client, async_client = plain_client(mode, False), plain_client(mode, True)
    try:
        assert method_names(client) == method_names(async_client)
        assert {e.attribute for e in ENDPOINTS if e.mode == mode} == method_names(client)
    finally:
        await close_client(client, False)
        await close_client(async_client, True)


@pytest.mark.parametrize("endpoint", ENDPOINTS, ids=endpoint_id)
@pytest.mark.parametrize("async_", [False, True], ids=["sync", "async"])
def test_resources_offer_raw_and_streaming_views(endpoint, async_):
    client = client_for(endpoint, async_, responder([], endpoint))
    resource = endpoint.resource(client)
    name = endpoint.attribute.rsplit(".", 1)[-1]
    assert callable(getattr(resource.with_raw_response, name))
    assert callable(getattr(resource.with_streaming_response, name))


@pytest.mark.parametrize("mode", MODES)
@pytest.mark.parametrize("async_", [False, True], ids=["sync", "async"])
async def test_every_resource_method_documents_its_route(mode, async_):
    # _surface parses the declaration off the sync methods; async twins must match.
    client = plain_client(mode, async_)
    try:
        for endpoint in [e for e in ENDPOINTS if e.mode == mode]:
            name = endpoint.attribute.rsplit(".", 1)[-1]
            summary = getattr(type(endpoint.resource(client)), name).__doc__.strip()
            assert summary.startswith(f"{endpoint.verb} {endpoint.template}."), endpoint.id
    finally:
        await close_client(client, async_)


@pytest.mark.parametrize("mode", MODES)
@pytest.mark.parametrize("async_", [False, True], ids=["sync", "async"])
async def test_optional_parameters_are_keyword_only_and_default_to_not_given(mode, async_):
    client = plain_client(mode, async_)
    try:
        for endpoint in [e for e in ENDPOINTS if e.mode == mode]:
            name = endpoint.attribute.rsplit(".", 1)[-1]
            for parameter in inspect.signature(getattr(type(endpoint.resource(client)), name)).parameters.values():
                if parameter.name in ("self", "extra_headers", "extra_query", "extra_body"):
                    continue
                if parameter.default is inspect.Parameter.empty:
                    continue
                assert parameter.kind is parameter.KEYWORD_ONLY, f"{endpoint.id}.{parameter.name}"
                assert parameter.default is NOT_GIVEN, f"{endpoint.id}.{parameter.name}"
    finally:
        await close_client(client, async_)


@pytest.mark.parametrize("mode", MODES)
@pytest.mark.parametrize("async_", [False, True], ids=["sync", "async"])
async def test_resource_tree_is_built_once_and_reused(mode, async_):
    client = plain_client(mode, async_)
    try:
        top = [name for name, value in vars(type(client)).items() if isinstance(value, cached_property)]
        assert top, type(client).__name__
        for name in top:
            assert getattr(client, name) is getattr(client, name)
    finally:
        await close_client(client, async_)


def test_unknown_resource_attributes_fail_loudly():
    with Forward(pat=TOKEN, http_client=httpx.Client()) as client:
        with pytest.raises(AttributeError):
            client.sessions.no_such_method
        with pytest.raises(AttributeError):
            client.no_such_resource
