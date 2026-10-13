from __future__ import annotations

import inspect
import os
from contextlib import AsyncExitStack
from datetime import datetime, timezone

import httpx
import pytest

from qca import APIError, APIStatusError, AsyncForward, Forward
from tests.sa.test_auth_live import region_config
from tests.support.harness import name

pytestmark = pytest.mark.integration


def response_log(response):
    print(
        f"http method={response.request.method} path={response.request.url.path} "
        f"status={response.status_code} request_id={response.headers.get('x-request-id', '')}",
        flush=True,
    )


async def async_response_log(response):
    response_log(response)


def failure(error):
    if isinstance(error, APIStatusError):
        return f"HTTP {error.status_code} code={error.code} request_id={error.request_id}"
    return type(error).__name__


async def invoke(method, *args, **kwargs):
    try:
        value = method(*args, **kwargs)
        return await value if inspect.isawaitable(value) else value
    except APIError as error:
        raise AssertionError(failure(error)) from None


async def denied(method, *args, statuses, **kwargs):
    try:
        value = method(*args, **kwargs)
        if inspect.isawaitable(value):
            await value
    except APIStatusError as error:
        if error.status_code in statuses:
            return
        raise AssertionError("Unexpected access refusal: " + failure(error)) from None
    except APIError as error:
        raise AssertionError(failure(error)) from None
    raise AssertionError("Expected access refusal, but the request succeeded")


def verify_token(token, subject, identity_id):
    if (
        not token.access_token
        or token.type != "service_account_token"
        or token.token_type != "Bearer"
        or not token.auth_token_id
        or not token.credential_id
        or not token.service_account_id
        or token.subject_type != subject
        or token.identity_id != identity_id
        or not 0 < token.expires_in <= 600
        or token.expires_at <= datetime.now(timezone.utc)
    ):
        raise AssertionError("Issued SAT metadata did not match the requested subject and lifetime")
    print(
        f"issued subject={subject} auth_token_id={token.auth_token_id} credential_id={token.credential_id} "
        f"identity_id={token.identity_id} expires_at={token.expires_at.isoformat()}",
        flush=True,
    )


@pytest.mark.parametrize("region", ["cn", "global"])
@pytest.mark.parametrize("async_mode", [False, True], ids=["sync", "async"])
async def test_forward_sa_tokens(region, async_mode):
    assert os.environ.get("QODER_SA_LIVE_ALLOW_WRITE") == "true", "QODER_SA_LIVE_ALLOW_WRITE=true is required"
    key, host = region_config(region)
    Client = AsyncForward if async_mode else Forward
    cleanups = []
    async with AsyncExitStack() as stack:

        async def client(access_token=None):
            transport = (
                httpx.AsyncClient(event_hooks={"response": [async_response_log]})
                if async_mode
                else httpx.Client(event_hooks={"response": [response_log]})
            )
            value = Client(
                base_url=f"{host}/api/v1/forward/",
                auth_mode="sa",
                access_token=access_token,
                max_retries=0,
                timeout=30,
                http_client=transport,
                _strict_response_validation=True,
            )
            if async_mode:
                return await stack.enter_async_context(value)
            return stack.enter_context(value)

        issuer = await client()
        params = dict(sa_key=key, ttl_seconds=600, metadata={"purpose": "sdk verification", "sdk": "python"})

        async def revoke(token, runtime, identity_id=None):
            result = await invoke(
                issuer.service_account_tokens.revoke,
                token.auth_token_id,
                sa_key=key,
                target_credential_id=token.credential_id,
                target_expires_at=token.expires_at,
                reason="sdk verification complete",
            )
            assert result.revoked, "Revoke did not acknowledge success"
            if identity_id:
                await denied(runtime.identities.configs.list, identity_id, limit=1, statuses=(401, 403))
            else:
                await denied(runtime.templates.list, limit=1, statuses=(401, 403))

        try:
            admin_token = await invoke(issuer.service_account_tokens.create, **params)
            admin = await client(admin_token.access_token)
            cleanups.append(("admin SAT " + admin_token.auth_token_id, lambda: revoke(admin_token, admin)))
            verify_token(admin_token, "admin", None)
            assert isinstance((await invoke(admin.templates.list, limit=1)).data, list)
            identities = []
            for _ in range(2):
                identity = await invoke(admin.identities.create, external_id=name("sat-identity"))
                identity_id = identity.id
                cleanups.append(
                    ("identity " + identity_id, lambda identity_id=identity_id: admin.identities.delete(identity_id))
                )
                assert identity_id, "Created Identity must have an ID"
                identities.append(identity_id)
            identity_token = await invoke(issuer.identities.service_account_tokens.create, identities[0], **params)
            runtime = await client(identity_token.access_token)
            cleanups.append(
                ("identity SAT " + identity_token.auth_token_id, lambda: revoke(identity_token, runtime, identities[0]))
            )
            verify_token(identity_token, "identity", identities[0])
            assert isinstance((await invoke(runtime.identities.configs.list, identities[0], limit=1)).data, list)
            await denied(runtime.identities.configs.list, identities[1], limit=1, statuses=(403,))
            print(
                f"verified {region}/{'async' if async_mode else 'sync'} business access and Identity isolation",
                flush=True,
            )
        finally:
            failures = []
            for label, action in reversed(cleanups):
                try:
                    await invoke(action)
                    print(f"cleanup {label}: completed", flush=True)
                except Exception as error:
                    failures.append(label + ": " + failure(error))
            assert not failures, "Cleanup failed: " + "; ".join(failures)
