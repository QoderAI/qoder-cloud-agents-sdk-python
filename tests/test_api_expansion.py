"""New API contracts frozen from api-doc master; no credentials or network."""

from __future__ import annotations

import inspect
import json
import re
from pathlib import Path

import httpx
import pytest

from qca import APIConnectionError, APIStatusError, AsyncForward, AsyncManaged, Forward, Managed

OPERATIONS = json.loads((Path(__file__).parent / "fixtures/api-expansion.json").read_text())["operations"]
SEGMENT = "id /?%#"
CLIENTS = {
    (False, "forward"): Forward,
    (True, "forward"): AsyncForward,
    (False, "managed"): Managed,
    (True, "managed"): AsyncManaged,
}


def resource(client, entry):
    for name in entry.split("."):
        client = getattr(client, name)
    return client


def kwargs(op):
    args = {name: SEGMENT for name in re.findall(r"{(\w+)}", op["path"])}
    if op["entry"] == "vaults.credentials":
        args["vault_id"] = args.pop("id")
        args["credential_id"] = args.pop("cred_id")
    return {**args, **(op["body"] or {}), **op["query"]}


async def result(value):
    return await value if inspect.isawaitable(value) else value


@pytest.mark.parametrize("async_", [False, True])
@pytest.mark.parametrize("op", OPERATIONS, ids=lambda op: op["mode"] + "." + op["entry"] + "." + op["method"])
async def test_documented_api_expansion(op, async_):
    def handle(req):
        assert req.method == op["http"]
        path = re.sub(r"{\w+}", lambda _: "id%20%2F%3F%25%23", op["path"])
        assert req.url.raw_path.split(b"?")[0].decode() == "/api/v1/" + op["mode"] + path
        assert "x-qoder-beta" not in req.headers
        for key, value in op["query"].items():
            assert req.url.params.get_list(key) == [
                str(v).lower() if isinstance(v, bool) else str(v)
                for v in (value if isinstance(value, list) else [value])
            ]
        assert "identity_ids[]" not in req.url.params
        assert "template_ids[]" not in req.url.params
        if op["body"] is not None:
            assert json.loads(req.content) == op["body"]
        return httpx.Response(
            202 if op["entry"] == "sessions" else 201 if op["method"] == "create" else 200, json=op["response"]
        )

    http = (httpx.AsyncClient if async_ else httpx.Client)(transport=httpx.MockTransport(handle))
    client = CLIENTS[async_, op["mode"]](
        pat="test-token",
        base_url="https://api.test/api/v1/" + op["mode"],
        http_client=http,
        _strict_response_validation=True,
    )
    method = {"listIdentities": "list_identities", "listTemplates": "list_templates"}.get(op["method"], op["method"])
    try:
        data = await result(getattr(resource(client, op["entry"]), method)(**kwargs(op)))
        # Timestamp fields normalize to UTC; compare the full schema through JSON values.
        actual = data.model_dump(mode="json", exclude_unset=True)
        expected = op["response"]
        assert actual == expected
    finally:
        await result(client.close())
        await result(http.aclose() if async_ else http.close())


@pytest.mark.parametrize("async_", [False, True])
@pytest.mark.parametrize("method", ["list_identities", "list_templates"])
@pytest.mark.parametrize("backward", [False, True])
async def test_usage_pagination_keeps_hourly_filters(async_, method, backward):
    op = next(
        o for o in OPERATIONS if o["method"] == ("listIdentities" if method == "list_identities" else "listTemplates")
    )
    calls = []
    args = {**op["query"], **({"before_id": "initial"} if backward else {})}

    def handle(req):
        calls.append(req)
        assert req.url.params["start_at"] == args["start_at"]
        assert req.url.params["end_at"] == args["end_at"]
        assert req.url.params.get_list("identity_ids") == args["identity_ids"]
        assert req.url.params.get_list("template_ids") == args["template_ids"]
        assert "start_time" not in req.url.params and "end_time" not in req.url.params
        if len(calls) > 1:
            assert req.url.params["before_id" if backward else "after_id"] == ("first" if backward else "last")
        return httpx.Response(
            200,
            json={
                **op["response"],
                "data": [op["response"]["data"][0]],
                "first_id": "first",
                "last_id": "last",
                "has_more": len(calls) == 1,
            },
        )

    http = (httpx.AsyncClient if async_ else httpx.Client)(transport=httpx.MockTransport(handle))
    client = CLIENTS[async_, "forward"](pat="test-token", http_client=http)
    try:
        page = await result(getattr(client.usage, method)(**args))
        assert page.data[0].active_seconds == op["response"]["data"][0]["active_seconds"]
        assert page.start_at == args["start_at"]
        await result(page.get_next_page())
        assert len(calls) == 2
    finally:
        await result(client.close())
        await result(http.aclose() if async_ else http.close())


@pytest.mark.parametrize("async_", [False, True])
@pytest.mark.parametrize("status", [200, 202])
async def test_cancel_lightweight_acknowledgement(async_, status):
    http = (httpx.AsyncClient if async_ else httpx.Client)(
        transport=httpx.MockTransport(
            lambda r: httpx.Response(status, json={"id": "sess_one", "type": "session", "status": "canceling"})
        )
    )
    client = CLIENTS[async_, "managed"](pat="test-token", http_client=http, _strict_response_validation=True)
    try:
        assert (await result(client.sessions.cancel("sess_one"))).status == "canceling"
    finally:
        await result(client.close())
        await result(http.aclose() if async_ else http.close())


@pytest.mark.parametrize("async_", [False, True])
@pytest.mark.parametrize("failure", [429, 503, "network"])
async def test_credential_rotation_never_retries(async_, failure):
    calls = []

    def handle(req):
        calls.append(req)
        if failure == "network":
            raise httpx.ConnectError("rotation uncertain", request=req)
        return httpx.Response(
            failure,
            json={"error": {"type": "api_error", "message": "rotation uncertain"}},
            headers={"retry-after-ms": "1", "x-should-retry": "true"},
        )

    http = (httpx.AsyncClient if async_ else httpx.Client)(transport=httpx.MockTransport(handle))
    client = CLIENTS[async_, "forward"](pat="test-token", http_client=http, max_retries=3)
    try:
        with pytest.raises((APIStatusError, APIConnectionError)):
            await result(
                client.vaults.credentials.update(
                    "cred_one",
                    vault_id="vault_one",
                    auth={"type": "static_bearer", "token": "test-secret"},
                    extra_headers={"Idempotency-Key": "caller-key"},
                )
            )
        assert len(calls) == 1
    finally:
        await result(client.close())
        await result(http.aclose() if async_ else http.close())


@pytest.mark.parametrize("async_", [False, True])
async def test_deployment_runs_replay_scoped_cursor(async_):
    calls = []
    op = next(o for o in OPERATIONS if o["entry"] == "deployments.runs" and o["method"] == "list")

    def handle(req):
        calls.append(req)
        assert req.url.path.endswith("/deployments/dep_one/runs")
        assert req.url.params["triggered_after"] == "2026-06-01T00:00:00Z"
        assert req.headers["qoder-workspace-id"] == "workspace_one"
        if len(calls) > 1:
            assert req.url.params["page"] == "opaque +/=?"
        return httpx.Response(
            200,
            json={
                **op["response"],
                "has_more": len(calls) == 1,
                "next_page": "opaque +/=?" if len(calls) == 1 else None,
            },
        )

    http = (httpx.AsyncClient if async_ else httpx.Client)(transport=httpx.MockTransport(handle))
    client = CLIENTS[async_, "managed"](pat="test-token", http_client=http)
    try:
        page = await result(
            client.deployments.runs.list(
                "dep_one", triggered_after="2026-06-01T00:00:00Z", workspace_id="workspace_one"
            )
        )
        await result(page.get_next_page())
        assert len(calls) == 2
    finally:
        await result(client.close())
        await result(http.aclose() if async_ else http.close())


@pytest.mark.parametrize("async_", [False, True])
async def test_credential_null_patch_and_raw_response(async_):
    def handle(req):
        assert req.url.params["identity_id"] == "idn_one"
        assert json.loads(req.content) == {
            "auth": {"type": "mcp_oauth", "expires_at": None, "refresh": {"scope": None}},
            "metadata": None,
        }
        return httpx.Response(200, json=next(o for o in OPERATIONS if o["entry"] == "vaults.credentials")["response"])

    http = (httpx.AsyncClient if async_ else httpx.Client)(transport=httpx.MockTransport(handle))
    client = CLIENTS[async_, "forward"](pat="test-token", http_client=http)
    try:
        raw = await result(
            client.vaults.credentials.with_raw_response.update(
                "cred_one",
                vault_id="vault_one",
                identity_id="idn_one",
                auth={"type": "mcp_oauth", "expires_at": None, "refresh": {"scope": None}},
                metadata=None,
            )
        )
        assert raw.status_code == 200
        assert (await result(raw.parse())).id == "vcred_xxx"
    finally:
        await result(client.close())
        await result(http.aclose() if async_ else http.close())


@pytest.mark.parametrize("async_", [False, True])
async def test_usage_supports_comma_separated_ids_and_rejects_legacy_keywords(async_):
    def handle(req):
        assert req.url.params.get_list("identity_ids") == ["idn_one,idn_two"]
        assert req.url.params.get_list("template_ids") == ["tmpl_one,tmpl_two"]
        return httpx.Response(200, json={"data": [], "has_more": False})

    http = (httpx.AsyncClient if async_ else httpx.Client)(transport=httpx.MockTransport(handle))
    client = CLIENTS[async_, "forward"](pat="test-token", http_client=http)
    try:
        await result(
            client.usage.list_identities(
                start_at="2026-09-14T09:00:00",
                end_at="2026-09-14T12:00:00",
                identity_ids="idn_one,idn_two",
                template_ids="tmpl_one,tmpl_two",
            )
        )
        with pytest.raises(TypeError):
            client.usage.list_identities(start_time=123, end_time=456)
        assert not hasattr(client.vaults, "search")
    finally:
        await result(client.close())
        await result(http.aclose() if async_ else http.close())
