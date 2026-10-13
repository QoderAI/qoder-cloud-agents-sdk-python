"""Forward SAT management contracts from the public docs, without account credentials."""

from __future__ import annotations

import inspect
import json
from pathlib import Path

import httpx
import pytest

from qca import APIConnectionError, APIStatusError, AsyncForward, Forward, Managed
from qca.forward.types import ServiceAccountToken, ServiceAccountTokenRevokeResponse

OPERATIONS = json.loads((Path(__file__).parent / "fixtures/service-account-tokens.json").read_text())["operations"]


async def result(value):
    return await value if inspect.isawaitable(value) else value


def invoke(client, op, **kwargs):
    resource = client
    for name in op["entry"].split("."):
        resource = getattr(resource, name)
    path_args = {name: "id /?%#" for name in ("identity_id", "auth_token_id") if "{" + name + "}" in op["path"]}
    return getattr(resource, op["method"])(**path_args, **kwargs)


@pytest.mark.parametrize("async_", [False, True])
@pytest.mark.parametrize("op", OPERATIONS, ids=lambda op: op["operation_id"])
async def test_documented_token_management_contract(async_, op):
    calls = []

    def handle(req):
        calls.append(req)
        path = op["path"].replace("{identity_id}", "id%20%2F%3F%25%23").replace("{auth_token_id}", "id%20%2F%3F%25%23")
        assert req.method == "POST"
        assert req.url.raw_path.decode() == "/api/v1/forward" + path
        assert req.headers["authorization"] == "Bearer explicit-sa-key"
        assert req.headers["content-type"] == "application/json"
        assert req.headers["x-trace"] == "test"
        assert json.loads(req.content) == op["body"]
        assert "explicit-sa-key" not in req.content.decode()
        return httpx.Response(
            200 if op["method"] == "revoke" else 201, json=op["response"], headers={"x-request-id": "req_sat"}
        )

    http = (httpx.AsyncClient if async_ else httpx.Client)(transport=httpx.MockTransport(handle))
    client = (AsyncForward if async_ else Forward)(
        pat="business-pat",
        http_client=http,
        base_url="https://api.test/api/v1/forward",
        default_headers={"authorization": "Bearer default-token"},
        _strict_response_validation=True,
    )
    try:
        data = await result(
            invoke(
                client,
                op,
                sa_key="explicit-sa-key",
                **op["body"],
                extra_headers={"AUTHORIZATION": "Bearer wrong", "x-trace": "test"},
            )
        )
        assert isinstance(data, ServiceAccountTokenRevokeResponse if op["method"] == "revoke" else ServiceAccountToken)
        assert data.model_dump(mode="json", exclude_unset=True) == op["response"]
        assert data._request_id == "req_sat"
        if op["method"] != "revoke":
            assert op["response"]["access_token"] not in repr(data)
        assert len(calls) == 1
    finally:
        await result(client.close())


class BusinessCredential:
    def __init__(self):
        self.calls = 0

    def get_token(self):
        self.calls += 1
        return "business-token"


@pytest.mark.parametrize("async_", [False, True])
@pytest.mark.parametrize("auth", ["none", "ambient", "static", "provider"])
async def test_key_is_required_and_scoped_to_management_requests(async_, auth, monkeypatch):
    monkeypatch.delenv("QODER_PAT", raising=False)
    monkeypatch.delenv("QODER_ACCESS_TOKEN", raising=False)
    if auth == "ambient":
        monkeypatch.setenv("QODER_PAT", "business-token")
        monkeypatch.setenv("QODER_ACCESS_TOKEN", "business-token")
    credential = BusinessCredential()
    requests = []

    def handle(req):
        requests.append(req)
        if req.method == "GET":
            assert req.headers["authorization"] == "Bearer business-token"
            return httpx.Response(200, json={"data": []})
        assert req.headers["authorization"] == "Bearer sa-key"
        assert req.content == b"{}"
        payload = {"revoked": True} if req.url.path.endswith("/revoke") else OPERATIONS[0]["response"]
        return httpx.Response(200 if "revoked" in payload else 201, json=payload)

    http = (httpx.AsyncClient if async_ else httpx.Client)(transport=httpx.MockTransport(handle))
    options = (
        {"credential": credential}
        if auth == "provider"
        else {"access_token": "business-token", "auth_mode": "sa"}
        if auth == "static"
        else {}
    )
    client = (AsyncForward if async_ else Forward)(http_client=http, **options)
    try:
        for op in OPERATIONS:
            await result(invoke(client, op, sa_key="sa-key"))
        assert credential.calls == 0
        if auth != "none":
            await result(client.models.list())
            assert credential.calls == (1 if auth == "provider" else 0)
    finally:
        await result(client.close())


@pytest.mark.parametrize("async_", [False, True])
@pytest.mark.parametrize("op", OPERATIONS, ids=lambda op: op["operation_id"])
@pytest.mark.parametrize("failure", [429, 503, "network"])
async def test_management_writes_never_retry(async_, op, failure):
    requests = []

    def handle(req):
        requests.append(req)
        if failure == "network":
            raise httpx.ConnectError("response uncertain", request=req)
        return httpx.Response(
            failure,
            json={"error": {"message": "response uncertain"}},
            headers={"x-should-retry": "true", "retry-after-ms": "1"},
        )

    http = (httpx.AsyncClient if async_ else httpx.Client)(transport=httpx.MockTransport(handle))
    client = (AsyncForward if async_ else Forward)(http_client=http, max_retries=3)
    try:
        with pytest.raises((APIConnectionError, APIStatusError)):
            await result(invoke(client, op, sa_key="sa-key", extra_headers={"Idempotency-Key": "unsupported-key"}))
        assert len(requests) == 1
    finally:
        await result(client.close())


@pytest.mark.parametrize("async_", [False, True])
@pytest.mark.parametrize("op", OPERATIONS, ids=lambda op: op["operation_id"])
@pytest.mark.parametrize("key", ["", " ", "key\nInjected:value", "key\t", "key\x00", None])
async def test_invalid_key_cannot_fall_back_to_business_auth(async_, op, key):
    def handle(req):
        pytest.fail("invalid SA Key reached transport")

    http = (httpx.AsyncClient if async_ else httpx.Client)(transport=httpx.MockTransport(handle))
    client = (AsyncForward if async_ else Forward)(pat="business-pat", http_client=http)
    try:
        with pytest.raises(ValueError, match="sa_key"):
            await result(invoke(client, op, sa_key=key))
    finally:
        await result(client.close())


def test_token_management_is_forward_only():
    with Managed(pat="unused") as client:
        assert not hasattr(client, "service_account_tokens")
