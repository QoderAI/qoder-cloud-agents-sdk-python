import inspect
import json
from copy import deepcopy

import httpx
import pytest

from qca import AsyncForward, AsyncManaged, Forward, Managed
from qca._version import __version__
from qca.common._types import NOT_GIVEN

STAMP = {
    "__qca_sdk_created": "true",
    "__qca_sdk_language": "python",
    "__qca_sdk_version": __version__,
}


async def resolve(value):
    return await value if inspect.isawaitable(value) else value


@pytest.fixture(params=[("forward", False), ("forward", True), ("managed", False), ("managed", True)])
async def session_client(request):
    mode, async_ = request.param
    recorded = []

    def handle(req):
        recorded.append(req)
        return httpx.Response(200, json={"id": "sess_test"})

    cls = {
        (False, "forward"): Forward,
        (True, "forward"): AsyncForward,
        (False, "managed"): Managed,
        (True, "managed"): AsyncManaged,
    }[async_, mode]
    http = (httpx.AsyncClient if async_ else httpx.Client)(transport=httpx.MockTransport(handle))
    client = cls(pat="test", http_client=http, max_retries=0)
    params = (
        {"identity_id": "idn", "template_id": "tmpl"}
        if mode == "forward"
        else {"agent": "agent", "environment_id": "env"}
    )
    yield client, params, recorded, mode
    await resolve(client.close())


@pytest.mark.parametrize("metadata", [NOT_GIVEN, None, {}, {"ticket": "A-123"}, STAMP])
async def test_create_stamps_metadata_without_mutating_input(session_client, metadata):
    client, params, recorded, _ = session_client
    original = deepcopy(metadata) if isinstance(metadata, dict) else metadata
    for _ in range(2):
        await resolve(client.sessions.create(**params, metadata=metadata))
    expected = {**(metadata if isinstance(metadata, dict) else {}), **STAMP}
    for req in recorded:
        assert req.method == "POST" and req.url.path.endswith("/sessions")
        assert json.loads(req.content) == {**params, "metadata": expected}
        assert req.headers["x-qoder-package-version"] == expected["__qca_sdk_version"]
    assert metadata == original


@pytest.mark.parametrize("key", STAMP)
@pytest.mark.parametrize("value", ["user-value", None, True, 12])
@pytest.mark.parametrize("extra", [False, True])
async def test_conflicts_fail_before_transport(session_client, key, value, extra):
    client, params, recorded, _ = session_client
    metadata = {"ticket": "A-123", key: value}
    kwargs = {"extra_body": {"metadata": metadata}} if extra else {"metadata": metadata}
    with pytest.raises(ValueError, match=f"conflicting SDK metadata field: {key}") as exc:
        await resolve(client.sessions.create(**params, **kwargs))
    assert "user-value" not in str(exc.value)
    assert metadata == {"ticket": "A-123", key: value}
    assert not recorded


async def test_extra_body_and_headers_keep_real_sdk_version(session_client):
    client, params, recorded, mode = session_client
    metadata = {"ticket": "extra", "__qca_sdk_future": "preserved"}
    if mode == "forward":
        metadata["nested"] = {"items": [1, False, None]}
    original = deepcopy(metadata)
    await resolve(
        client.sessions.create(
            **params,
            metadata={"replaced": "typed"},
            extra_body={"metadata": metadata},
            extra_headers={"X-Qoder-Package-Version": "custom-header"},
        )
    )
    assert json.loads(recorded[0].content) == {**params, "metadata": {**original, **STAMP}}
    assert metadata == original


@pytest.mark.parametrize("metadata", [[], "invalid", 1, False])
async def test_invalid_metadata_fails_before_transport(session_client, metadata):
    client, params, recorded, _ = session_client
    with pytest.raises(ValueError, match="metadata must be a JSON object or null"):
        await resolve(client.sessions.create(**params, extra_body={"metadata": metadata}))
    assert not recorded


async def test_update_and_retrieve_do_not_stamp_metadata(session_client):
    client, _, recorded, _ = session_client
    metadata = {"ticket": "A-123", "__qca_sdk_language": "historic"}
    await resolve(client.sessions.update("sess_test", metadata=metadata))
    await resolve(client.sessions.retrieve("sess_test"))
    assert json.loads(recorded[0].content) == {"metadata": metadata}
    assert not recorded[1].content
