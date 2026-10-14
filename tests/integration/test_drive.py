"""Opt-in Drive lifecycle on isolated Identities; never clears an existing Drive."""

from __future__ import annotations

import inspect
import os
from contextlib import AsyncExitStack
from uuid import uuid4

import httpx
import pytest

from qca import APIStatusError, AsyncForward, Forward
from tests.support.harness import read_env

pytestmark = pytest.mark.integration


async def call(method, *args, **kwargs):
    result = method(*args, **kwargs)
    return await result if inspect.isawaitable(result) else result


async def refused(action, status):
    try:
        await action()
    except APIStatusError as error:
        assert error.status_code == status
    else:
        raise AssertionError(f"Expected HTTP {status}")


def safe_error(error):
    if isinstance(error, APIStatusError):
        return f"HTTP {error.status_code} code={error.code} request_id={error.request_id}"
    # Never include storage URLs or token responses in failures.
    return type(error).__name__


@pytest.mark.parametrize("region", ["cn", "global"])
@pytest.mark.parametrize("auth", ["pat", "admin_sat", "identity_sat"])
@pytest.mark.parametrize("async_mode", [False, True], ids=["sync", "async"])
async def test_drive_lifecycle(region, auth, async_mode):
    values = {**read_env(os.environ.get("QODER_LIVE_ENV_FILE", ".env.live")), **os.environ}
    if values.get("QODER_DRIVE_RUN_LIVE") != "1":
        pytest.skip("Set QODER_DRIVE_RUN_LIVE=1 to run Drive tests")
    assert values.get("QODER_DRIVE_LIVE_ALLOW_WRITE") == "true"
    host = "https://api.qoder.com.cn" if region == "cn" else "https://api.qoder.com"
    Client = AsyncForward if async_mode else Forward
    options = dict(base_url=f"{host}/api/v1/forward/", max_retries=0, timeout=30, _strict_response_validation=True)
    cleanups = []
    stage = "setup"
    async with AsyncExitStack() as stack:

        async def client(**authentication):
            instance = Client(**options, **authentication)
            return await stack.enter_async_context(instance) if async_mode else stack.enter_context(instance)

        try:
            issuer = await client(auth_mode="sa")
            key = values.get(f"QODER_SA_{region.upper()}_KEY", "")

            async def issue(identity_id=None):
                assert key, f"QODER_SA_{region.upper()}_KEY is required"
                params = dict(sa_key=key, ttl_seconds=600)
                token = (
                    await call(issuer.identities.service_account_tokens.create, identity_id, **params)
                    if identity_id
                    else await call(issuer.service_account_tokens.create, **params)
                )
                cleanups.append(
                    lambda: call(
                        issuer.service_account_tokens.revoke,
                        token.auth_token_id,
                        sa_key=key,
                        target_credential_id=token.credential_id,
                        target_expires_at=token.expires_at,
                    )
                )
                return await client(auth_mode="sa", access_token=token.access_token)

            if auth == "pat":
                pat = values.get(f"QODER_FORWARD_{region.upper()}_PAT")
                assert pat, f"QODER_FORWARD_{region.upper()}_PAT is required"
                admin = await client(auth_mode="pat", pat=pat)
            else:
                admin = await issue()
            identity = await call(admin.identities.create, external_id=f"sdk-drive-{uuid4().hex}")
            cleanups.append(lambda: call(admin.identities.delete, identity.id))
            # This ID was created above and is never supplied by the operator.
            cleanups.append(lambda: call(admin.drives.clear, identity_id=identity.id))
            runtime = await issue(identity.id) if auth == "identity_sat" else admin
            args = dict(identity_id=identity.id)
            print(f"Drive {region}/{auth}/{'async' if async_mode else 'sync'} identity_id={identity.id}", flush=True)
            assert (await call(runtime.drives.list_entries, **args)).entries == []

            stage = "upload"
            async with httpx.AsyncClient(timeout=30, follow_redirects=False) as storage:
                paths = ["sdk 目录/a+b.txt", "sdk 目录/zero.txt", "sdk 目录/nested/child.txt"]
                content = b"SDK Drive verification"
                for path in paths:
                    signed = await call(runtime.drives.create_upload_url, **args, path=path, content_type="text/plain")
                    assert signed.method == "PUT"
                    assert not any(key.lower() == "authorization" for key in signed.headers)
                    response = await storage.request(
                        signed.method, signed.url, headers=signed.headers, content=b"" if "zero" in path else content
                    )
                    assert 200 <= response.status_code < 300, f"Storage PUT HTTP {response.status_code}"
                stage = "pagination"
                entries, seen = [], set()
                cursor = None
                while True:
                    page = await call(
                        runtime.drives.list_entries,
                        **args,
                        path="sdk 目录",
                        limit=1,
                        **({"page_token": cursor} if cursor else {}),
                    )
                    entries.extend(page.entries)
                    cursor = page.next_page_token
                    if not cursor:
                        break
                    assert cursor not in seen, "Repeated cursor"
                    seen.add(cursor)
                    assert len(seen) < 10, "Pagination did not finish"
                assert {entry.path for entry in entries} == {paths[0], paths[1], "sdk 目录/nested"}
                assert next(entry for entry in entries if entry.path == paths[1]).size == 0
                assert next(entry for entry in entries if entry.type == "directory").size is None
                stage = "download"
                signed = await call(runtime.drives.create_download_url, **args, path=paths[0])
                assert signed.method == "GET"
                assert not any(key.lower() == "authorization" for key in signed.headers)
                response = await storage.request(signed.method, signed.url, headers=signed.headers)
                assert response.status_code == 200 and response.content == content, "Storage download differs"
            stage = "deletion"
            await refused(lambda: call(runtime.drives.delete_entry, **args, path="sdk 目录"), 409)
            assert (await call(runtime.drives.delete_entry, **args, path=paths[0])).deleted_count == 1
            assert (await call(runtime.drives.delete_entry, **args, path=paths[0])).deleted_count == 0
            assert (
                await call(runtime.drives.delete_entry, **args, path="sdk 目录/nested", recursive=True)
            ).deleted_count == 1
            assert (await call(runtime.drives.clear, **args)).deleted_count == 1
            assert (await call(runtime.drives.clear, **args)).deleted_count == 0
            if auth == "identity_sat":
                stage = "Identity isolation"
                other = await call(admin.identities.create, external_id=f"sdk-drive-other-{uuid4().hex}")
                cleanups.append(lambda: call(admin.identities.delete, other.id))
                await refused(lambda: call(runtime.drives.list_entries, identity_id=other.id), 403)
            else:
                stage = "Template managed tools"
                env = await call(
                    admin.environments.create, name=f"sdk-drive-{uuid4().hex[:12]}", config={"type": "cloud"}
                )
                cleanups.append(lambda: call(admin.environments.archive, env.id))
                template = await call(
                    admin.templates.create,
                    name=f"sdk-drive-{uuid4().hex[:12]}",
                    model="auto",
                    environment_id=env.id,
                    managed_tool_config={"enabled_tools": ["drive"]},
                )
                cleanups.append(lambda: call(admin.templates.archive, template.id))
                current = await call(admin.templates.retrieve, template.id)
                assert current.managed_tool_config.enabled_tools == ["drive"]
                current = await call(admin.templates.update, template.id, managed_tool_config={"enabled_tools": []})
                assert current.managed_tool_config is None or current.managed_tool_config.enabled_tools == []
        except Exception as error:
            # Suppress exception chains that can contain signed URLs / credentials.
            pytest.fail(f"{stage}: {safe_error(error)}", pytrace=False)
        finally:
            errors = []
            for action in reversed(cleanups):
                try:
                    await action()
                except Exception as error:
                    errors.append(safe_error(error))
            assert not errors, f"Drive cleanup failed: {errors}"
