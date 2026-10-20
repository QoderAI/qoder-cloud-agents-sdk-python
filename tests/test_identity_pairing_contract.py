"""Official Forward ownership and pairing wire contracts (2026-10-20)."""

import inspect
import json

import httpx
import pytest

from qca import AsyncForward, Forward


async def resolve(value):
    return await value if inspect.isawaitable(value) else value


OPERATIONS = [
    ("GET", "environments", lambda c, scope, file: c.environments.list(**scope)),
    ("POST", "environments", lambda c, scope, file: c.environments.create(name="env", **scope)),
    ("GET", "environments/env", lambda c, scope, file: c.environments.retrieve("env", **scope)),
    ("POST", "environments/env", lambda c, scope, file: c.environments.update("env", name="renamed", **scope)),
    ("POST", "environments/env/archive", lambda c, scope, file: c.environments.archive("env", **scope)),
    ("DELETE", "environments/env", lambda c, scope, file: c.environments.delete("env", **scope)),
    ("GET", "skills", lambda c, scope, file: c.skills.list(**scope)),
    ("POST", "skills", lambda c, scope, file: c.skills.create(files=[file], **scope)),
    ("GET", "skills/skill", lambda c, scope, file: c.skills.retrieve("skill", **scope)),
    ("PUT", "skills/skill", lambda c, scope, file: c.skills.update("skill", description="desc", **scope)),
    ("DELETE", "skills/skill", lambda c, scope, file: c.skills.delete("skill", **scope)),
    ("GET", "skills/skill/versions", lambda c, scope, file: c.skills.versions.list("skill", **scope)),
    ("POST", "skills/skill/versions", lambda c, scope, file: c.skills.versions.create("skill", files=[file], **scope)),
    (
        "GET",
        "skills/skill/versions/1",
        lambda c, scope, file: c.skills.versions.retrieve("1", skill_id="skill", **scope),
    ),
    (
        "DELETE",
        "skills/skill/versions/1",
        lambda c, scope, file: c.skills.versions.delete("1", skill_id="skill", **scope),
    ),
    (
        "GET",
        "skills/skill/versions/1/content",
        lambda c, scope, file: c.skills.versions.download("1", skill_id="skill", **scope),
    ),
    ("GET", "vaults", lambda c, scope, file: c.vaults.list(**scope)),
    ("POST", "vaults", lambda c, scope, file: c.vaults.create(display_name="vault", **scope)),
    ("GET", "vaults/vault", lambda c, scope, file: c.vaults.retrieve("vault", **scope)),
    ("DELETE", "vaults/vault", lambda c, scope, file: c.vaults.delete("vault", **scope)),
    ("GET", "vaults/vault/credentials", lambda c, scope, file: c.vaults.credentials.list("vault", **scope)),
    (
        "POST",
        "vaults/vault/credentials",
        lambda c, scope, file: c.vaults.credentials.create(
            "vault", auth={"type": "static_bearer", "token": "secret"}, **scope
        ),
    ),
    (
        "GET",
        "vaults/vault/credentials/cred",
        lambda c, scope, file: c.vaults.credentials.retrieve("cred", vault_id="vault", **scope),
    ),
    (
        "POST",
        "vaults/vault/credentials/cred",
        lambda c, scope, file: c.vaults.credentials.update(
            "cred", vault_id="vault", metadata={"note": "rotation"}, **scope
        ),
    ),
    (
        "DELETE",
        "vaults/vault/credentials/cred",
        lambda c, scope, file: c.vaults.credentials.delete("cred", vault_id="vault", **scope),
    ),
    ("GET", "files", lambda c, scope, file: c.files.list(**scope)),
    ("POST", "files", lambda c, scope, file: c.files.upload(file=file, **scope)),
    ("GET", "files/file", lambda c, scope, file: c.files.retrieve_metadata("file", **scope)),
    ("DELETE", "files/file", lambda c, scope, file: c.files.delete("file", **scope)),
    ("GET", "files/file/content", lambda c, scope, file: c.files.download("file", **scope)),
]


@pytest.mark.parametrize("async_", [False, True])
@pytest.mark.parametrize("identity", ["idn_ /?&", "", None])
@pytest.mark.parametrize("method,path,call", OPERATIONS)
async def test_identity_query_scope(async_, identity, method, path, call):
    api_calls = 0

    def handle(req):
        nonlocal api_calls
        if req.url.host == "storage.test":
            assert req.url.query == b"signature=ok"
            assert "authorization" not in req.headers
            return httpx.Response(200, content=b"content")
        api_calls += 1
        assert req.method == method
        assert req.url.path == "/api/v1/forward/" + path
        assert req.url.params.get("identity_id") == identity
        assert list(req.url.params.keys()) == ([] if identity is None else ["identity_id"])
        assert b"identity_id" not in req.read()
        if path == "files/file/content":
            return httpx.Response(200, json={"url": "https://storage.test/content?signature=ok"})
        if path.endswith("/content"):
            return httpx.Response(200, content=b"archive")
        return httpx.Response(200, json={"id": "resource", "data": [], "has_more": False})

    http = (httpx.AsyncClient if async_ else httpx.Client)(transport=httpx.MockTransport(handle))
    c = (AsyncForward if async_ else Forward)(pat="test", http_client=http)
    try:
        result = await resolve(call(c, {} if identity is None else {"identity_id": identity}, ("SKILL.md", b"# skill")))
        if path.endswith("/content"):
            await resolve(result.close())
        assert api_calls == 1
    finally:
        await resolve(c.close())


@pytest.mark.parametrize("async_", [False, True])
async def test_identity_query_overrides_and_pagination(async_):
    calls = 0

    def handle(req):
        nonlocal calls
        assert req.url.params["identity_id"] == "idn_override"
        calls += 1
        return httpx.Response(
            200,
            json={
                "data": [{"id": f"env_{calls}"}],
                "has_more": calls == 1,
                "next_page": "cursor" if calls == 1 else None,
            },
        )

    http = (httpx.AsyncClient if async_ else httpx.Client)(transport=httpx.MockTransport(handle))
    c = (AsyncForward if async_ else Forward)(pat="test", http_client=http)
    try:
        page = await resolve(c.environments.list(identity_id="idn_typed", extra_query={"identity_id": "idn_override"}))
        items = [e async for e in page] if async_ else list(page)
        assert len(items) == 2
        await resolve(
            c.environments.retrieve("env", identity_id="idn_typed", extra_query={"identity_id": "idn_override"})
        )
    finally:
        await resolve(c.close())


PAIRING = {
    "id": "pair_one",
    "type": "channel_pairing",
    "channel_id": "channel_one",
    "scope_type": "room",
    "scope_external_id": "room_one",
    "scope_display_name": "Team",
    "identity_id": "idn_one",
    "template_id": "tmpl_one",
    "status": "active",
    "paired_at": "2026-10-20T01:00:00Z",
}


@pytest.mark.parametrize("async_", [False, True])
@pytest.mark.parametrize("selector", [{"code": "K7MP92"}, {"channel_pairing_id": "pair_one"}])
async def test_pair_by_code_or_id(async_, selector):
    def handle(req):
        assert not req.url.query
        assert req.headers["idempotency-key"] == "pair-once"
        assert json.loads(req.content) == {**selector, "identity_id": "idn_one", "template_id": "tmpl_one"}
        return httpx.Response(200, json=PAIRING)

    http = (httpx.AsyncClient if async_ else httpx.Client)(transport=httpx.MockTransport(handle))
    c = (AsyncForward if async_ else Forward)(pat="test", http_client=http, _strict_response_validation=True)
    try:
        result = await resolve(
            c.channel_pairings.create(
                **selector, identity_id="idn_one", template_id="tmpl_one", idempotency_key="pair-once"
            )
        )
        assert result.scope_type == "room"
        assert result.scope_external_id == "room_one"
        assert result.scope_display_name == "Team"
        assert {"scope_type", "scope_external_id", "scope_display_name"} <= type(result).model_fields.keys()
    finally:
        await resolve(c.close())
