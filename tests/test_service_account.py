from __future__ import annotations

import asyncio
import json
import threading
import time
import traceback
from concurrent.futures import ThreadPoolExecutor
from types import SimpleNamespace

import httpx
import pytest

from qca import (
    APIResponseValidationError,
    AsyncForward,
    AsyncManaged,
    AsyncServiceAccountCredential,
    Forward,
    InternalServerError,
    Managed,
    PermissionDeniedError,
    RateLimitError,
    ServiceAccountCredential,
)
from qca.common import service_account as sa


def token_response(token="sat-1", ttl=100):
    return httpx.Response(
        200,
        json={"access_token": token, "token_type": "Bearer", "expires_in": ttl, "expires_at": "2099-01-01T00:00:00Z"},
    )


def config(**overrides):
    return dict(sa_key="secret-key", region="global", scopes=["qca.access", "forward.access"], **overrides)


@pytest.mark.parametrize("cls,resource", [(Forward, "templates"), (Managed, "agents")])
def test_modes_and_copy(monkeypatch, cls, resource):
    monkeypatch.setenv("QODER_PAT", "ambient-pat")
    monkeypatch.delenv("QODER_ACCESS_TOKEN", raising=False)
    requests = []
    http = httpx.Client(
        transport=httpx.MockTransport(lambda r: requests.append(r) or httpx.Response(200, json={"data": []}))
    )
    client = cls(auth_mode="sa", access_token="static-sat", http_client=http)
    getattr(client.with_options(timeout=5), resource).list()
    getattr(client._raw_response_view(), resource).list().parse()
    getattr(client.with_options(auth_mode="pat"), resource).list()
    monkeypatch.setenv("QODER_ACCESS_TOKEN", "generic-token")
    getattr(cls(auth_mode="sa", http_client=http), resource).list()
    monkeypatch.delenv("QODER_ACCESS_TOKEN")
    with pytest.raises(TypeError, match="Could not resolve"):
        getattr(cls(auth_mode="sa", http_client=http), resource).list()
    assert [r.headers["authorization"] for r in requests] == [
        "Bearer static-sat",
        "Bearer static-sat",
        "Bearer ambient-pat",
        "Bearer generic-token",
    ]
    assert client.auth_mode == "sa"
    with pytest.raises(ValueError):
        cls(auth_mode="sa", pat="pat")
    with pytest.raises(ValueError):
        cls(access_token="")
    http.close()


def test_shared_credential_and_original_env_provenance(monkeypatch):
    monkeypatch.setenv("QODER_PAT", "ambient-pat")
    requests = []

    def handler(r):
        requests.append(r)
        if r.url.host == "openapi.qoder.sh":
            assert json.loads(r.content) == {
                "grant_type": "client_credentials",
                "audience": "qoder",
                "scope": "qca.access forward.access",
                "ttl_seconds": 3600,
            }
            assert r.headers["authorization"] == "Bearer secret-key"
            return token_response()
        assert r.headers["authorization"] == "Bearer sat-1"
        return httpx.Response(200, json={"data": []})

    http = httpx.Client(transport=httpx.MockTransport(handler))
    cred = ServiceAccountCredential(**config(http_client=http))
    f = Forward(credential=cred, http_client=http)
    Managed(credential=cred, http_client=http).agents.list()
    f.with_options(timeout=5).templates.list()
    assert sum(r.url.host == "openapi.qoder.sh" for r in requests) == 1
    assert "secret-key" not in repr(cred)
    with pytest.raises(ValueError):
        Forward(credential=cred, pat="static")
    with pytest.raises(ValueError):
        Forward(credential=cred, base_url="https://api.qoder.com.cn/api/v1/forward/")
    with pytest.raises(TypeError):
        AsyncForward(credential=cred)
    cred.close()
    assert not http.is_closed
    http.close()
    # Snapshot an ambient PAT without converting it to explicit configuration on copy.
    http = httpx.Client(transport=httpx.MockTransport(lambda r: httpx.Response(200, json={"data": []})))
    parent = Forward(http_client=http)
    monkeypatch.setenv("QODER_PAT", "different-pat")
    derived = parent.with_options(timeout=5)
    assert derived.pat == "ambient-pat"
    assert derived._auth_options["pat"] is None
    http.close()


def test_ttl_refresh_cooldown_and_safe_boundary(monkeypatch):
    now = 0.0
    monkeypatch.setattr(sa, "time", SimpleNamespace(monotonic=lambda: now, time=time.time))
    status = 200
    calls = 0

    def handler(r):
        nonlocal calls
        calls += 1
        return (
            token_response(f"sat-{calls}", "100")
            if status == 200
            else httpx.Response(
                status, json={"error": {"code": "temporary", "message": "secret-key"}, "request_id": "req-1"}
            )
        )

    http = httpx.Client(transport=httpx.MockTransport(handler))
    cred = ServiceAccountCredential(**config(http_client=http))
    assert cred.get_token() == "sat-1"
    now = 89
    assert cred.get_token() == "sat-1" and calls == 1
    now = 90
    status = 503
    assert cred.get_token() == "sat-1"
    assert cred.get_token() == "sat-1" and calls == 2
    now = 95
    with pytest.raises(InternalServerError):
        cred.get_token()
    now = 100
    status = 200
    assert cred.get_token() == "sat-4"
    now = 190
    status = 403
    with pytest.raises(PermissionDeniedError) as exc:
        cred.get_token()
    assert exc.value.request_id == "req-1"
    assert "secret-key" not in str(exc.value)
    assert "authorization" not in exc.value.request.headers
    with pytest.raises(PermissionDeniedError):
        cred.get_token()
    assert calls == 5
    http.close()


@pytest.mark.parametrize("ttl", [0, -1, 1.5, "1.5", True, 43201, None])
def test_invalid_ttl(ttl):
    with httpx.Client(transport=httpx.MockTransport(lambda _: token_response("sensitive-token", ttl))) as http:
        credential = ServiceAccountCredential(**config(http_client=http))
        with pytest.raises(APIResponseValidationError) as exc:
            credential.get_token()
        assert "sensitive-token" not in str(exc.value)
        assert "sensitive-token" not in str(exc.value.body)


def test_sync_concurrency_and_failure_cooldown():
    calls = 0
    started = threading.Event()
    release = threading.Event()

    def handler(_):
        nonlocal calls
        calls += 1
        started.set()
        release.wait(2)
        return token_response()

    with httpx.Client(transport=httpx.MockTransport(handler)) as http:
        cred = ServiceAccountCredential(**config(http_client=http))
        with ThreadPoolExecutor(max_workers=12) as executor:
            futures = [executor.submit(cred.get_token) for _ in range(12)]
            assert started.wait(2)
            release.set()
            assert [f.result() for f in futures] == ["sat-1"] * 12
        assert calls == 1
    calls = 0

    def fail(_):
        nonlocal calls
        calls += 1
        return httpx.Response(429, json={}, headers={"retry-after": "120"})

    with httpx.Client(transport=httpx.MockTransport(fail)) as http:
        cred = ServiceAccountCredential(**config(http_client=http))
        with ThreadPoolExecutor(max_workers=12) as executor:
            futures = [executor.submit(cred.get_token) for _ in range(12)]
            for future in futures:
                with pytest.raises(RateLimitError):
                    future.result()
        assert calls == 1


@pytest.mark.parametrize("cls,resource", [(AsyncForward, "templates"), (AsyncManaged, "agents")])
async def test_async_modes_shared_cache_and_headers(monkeypatch, cls, resource):
    monkeypatch.setenv("QODER_PAT", "ambient-pat")
    calls = 0
    tokens = []

    async def handler(r):
        nonlocal calls
        if r.url.host == "openapi.qoder.sh":
            calls += 1
            return token_response()
        tokens.append(r.headers["authorization"])
        return httpx.Response(200, json={"data": []})

    async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as http:
        async with AsyncServiceAccountCredential(**config(http_client=http)) as cred:
            client = cls(credential=cred, http_client=http)
            await getattr(client.with_options(timeout=5), resource).list()
            await getattr(client._raw_response_view(), resource).list()
            await getattr(client.with_options(auth_mode="pat"), resource).list()
            assert tokens == ["Bearer sat-1", "Bearer sat-1", "Bearer ambient-pat"] and calls == 1
            with pytest.raises(TypeError):
                Forward(credential=cred)
        assert not http.is_closed


async def test_async_owner_and_waiter_cancellation():
    started = asyncio.Event()
    release = asyncio.Event()
    calls = 0

    async def handler(_):
        nonlocal calls
        calls += 1
        started.set()
        if calls == 1:
            await release.wait()
        return token_response()

    async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as http:
        cred = AsyncServiceAccountCredential(**config(http_client=http))
        owner = asyncio.create_task(cred.get_token())
        await started.wait()
        waiter = asyncio.create_task(cred.get_token())
        waiter.cancel()
        with pytest.raises(asyncio.CancelledError):
            await waiter
        owner.cancel()
        with pytest.raises(asyncio.CancelledError):
            await owner
        assert await cred.get_token() == "sat-1" and calls == 2
        await cred.aclose()
        assert not http.is_closed


async def test_async_concurrent_failure_and_cooldown():
    calls = 0

    async def handler(_):
        nonlocal calls
        calls += 1
        await asyncio.sleep(0)
        return httpx.Response(503, json={})

    async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as http:
        cred = AsyncServiceAccountCredential(**config(http_client=http))
        results = await asyncio.gather(*(cred.get_token() for _ in range(12)), return_exceptions=True)
        assert all(isinstance(result, InternalServerError) for result in results)
        assert calls == 1


@pytest.mark.parametrize(
    "body",
    [
        None,
        [],
        {},
        {"access_token": "token", "token_type": "Basic", "expires_in": 100},
        *[
            {"access_token": "token", "token_type": "Bearer", "expires_in": 100, "expires_at": value}
            for value in [None, "", "2026-10-12"]
        ],
    ],
)
def test_invalid_response_fields(body):
    with httpx.Client(transport=httpx.MockTransport(lambda _: httpx.Response(200, json=body))) as http:
        credential = ServiceAccountCredential(**config(http_client=http))
        with pytest.raises(APIResponseValidationError):
            credential.get_token()


def test_short_lifetime_and_transport_error_redaction(monkeypatch):
    now = 0
    monkeypatch.setattr(sa, "time", SimpleNamespace(monotonic=lambda: now, time=time.time))

    def delayed(_):
        nonlocal now
        now = 1
        return token_response("sensitive-token", 1)

    with httpx.Client(transport=httpx.MockTransport(delayed)) as http:
        credential = ServiceAccountCredential(**config(http_client=http))
        with pytest.raises(APIResponseValidationError):
            credential.get_token()

    def fail(request):
        raise httpx.ConnectError("secret-key sensitive-token", request=request)

    with httpx.Client(transport=httpx.MockTransport(fail)) as http:
        credential = ServiceAccountCredential(**config(http_client=http))
        with pytest.raises(sa.APIConnectionError) as exc:
            credential.get_token()
        assert "secret-key" not in "".join(traceback.format_exception(exc.value))
        assert "authorization" not in exc.value.request.headers


async def test_async_exchange_timeout():
    async def stalled(_):
        await asyncio.sleep(5)
        return token_response()

    async with httpx.AsyncClient(transport=httpx.MockTransport(stalled)) as http:
        credential = AsyncServiceAccountCredential(**config(http_client=http, timeout=0.01))
        with pytest.raises(sa.APITimeoutError):
            await credential.get_token()
        await credential.aclose()
