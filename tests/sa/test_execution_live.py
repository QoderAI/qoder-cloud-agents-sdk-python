from __future__ import annotations

import inspect
import os
import time
from contextlib import AsyncExitStack

import anyio
import pytest

from qca import (
    APIError,
    AsyncForward,
    AsyncManaged,
    AsyncServiceAccountCredential,
    Forward,
    Managed,
    ServiceAccountCredential,
)
from tests.sa.test_auth_live import region_config
from tests.support.assertions import TurnResult
from tests.support.harness import marker, name, safe_error

pytestmark = pytest.mark.integration


async def call(method, *args, **kwargs):
    try:
        result = method(*args, **kwargs)
        return await result if inspect.isawaitable(result) else result
    except APIError as error:
        raise AssertionError(safe_error(error)) from None


async def finish_session(client, session_id, mode):
    deadline = time.monotonic() + 60
    session = await call(client.sessions.retrieve, session_id)
    if session.status not in ("idle", "terminated"):
        if mode == "forward":
            await call(client.sessions.cancel, session_id)
        else:
            await call(client.sessions.events.send, session_id, events=[{"type": "user.interrupt"}])
        while session.status not in ("idle", "terminated"):
            assert time.monotonic() < deadline, f"Cleanup session {session_id} did not become idle"
            await anyio.sleep(1)
            session = await call(client.sessions.retrieve, session_id)
    method = client.sessions.archive if mode == "forward" else client.sessions.delete
    await call(method, session_id)


@pytest.mark.parametrize("region", ["cn", "global"])
@pytest.mark.parametrize("mode", ["forward", "managed"])
@pytest.mark.parametrize("async_mode", [False, True], ids=["sync", "async"])
async def test_sa_execution(region, mode, async_mode):
    for flag in ("QODER_SA_LIVE_ALLOW_WRITE", "QODER_SA_LIVE_ALLOW_EXECUTION"):
        assert os.environ.get(flag) == "true", f"{flag}=true is required"
    key, host = region_config(region)
    model = os.environ.get("QODER_SA_MODEL", "auto")
    credential_type = AsyncServiceAccountCredential if async_mode else ServiceAccountCredential
    client_type = (
        (AsyncForward if mode == "forward" else AsyncManaged)
        if async_mode
        else (Forward if mode == "forward" else Managed)
    )
    path = "forward" if mode == "forward" else "cloud"
    cleanups = []

    def track(kind, resource, action):
        assert resource.id, f"Created {kind} must have an ID"
        cleanups.append((kind, resource.id, action))
        print(f"{region}/{mode}/{'async' if async_mode else 'sync'} {kind}_id={resource.id}", flush=True)
        return resource.id

    async with AsyncExitStack() as stack:
        credential = credential_type(sa_key=key, region=region, scopes=["qca.access", "forward.access"])
        client = client_type(credential=credential, base_url=f"{host}/api/v1/{path}/", max_retries=0, timeout=30)
        if async_mode:
            await stack.enter_async_context(credential)
            await stack.enter_async_context(client)
        else:
            stack.enter_context(credential)
            stack.enter_context(client)
        try:
            with anyio.fail_after(180):
                environment = await call(client.environments.create, name=name("sa-env"), config={"type": "cloud"})
                environment_id = track("environment", environment, lambda: client.environments.archive(environment.id))
                assert (await call(client.environments.retrieve, environment_id)).id == environment_id
                system = "Follow the current user message. Echo the supplied text directly without using tools."
                if mode == "forward":
                    identity = await call(client.identities.create, external_id=name("sa-identity"))
                    identity_id = track("identity", identity, lambda: client.identities.delete(identity.id))
                    template = await call(
                        client.templates.create,
                        name=name("sa-template"),
                        environment_id=environment_id,
                        model=model,
                        system=system,
                    )
                    template_id = track("template", template, lambda: client.templates.archive(template.id))
                    assert (await call(client.templates.retrieve, template_id)).id == template_id
                    session = await call(client.sessions.create, identity_id=identity_id, template_id=template_id)
                else:
                    agent = await call(client.agents.create, name=name("sa-agent"), model={"id": model}, system=system)
                    agent_id = track("agent", agent, lambda: client.agents.archive(agent.id))
                    assert (await call(client.agents.retrieve, agent_id)).id == agent_id
                    session = await call(client.sessions.create, agent=agent_id, environment_id=environment_id)
                session_id = track("session", session, lambda: finish_session(client, session.id, mode))
                assert (await call(client.sessions.retrieve, session_id)).id == session_id
                expected = marker()
                sent = await call(
                    client.sessions.events.send,
                    session_id,
                    events=[
                        {
                            "type": "user.message",
                            "content": [{"type": "text", "text": "Reply with exactly " + expected}],
                        }
                    ],
                    extra_headers={"Idempotency-Key": name("sa-event")},
                )
                assert len(sent.data) == 1 and sent.data[0].id, "Send must return one user event ID"
                reply = TurnResult(last_id=sent.data[0].id)
                stream = await call(
                    client.sessions.events.stream, session_id, last_event_id=sent.data[0].id, timeout=180
                )
                deadline = time.monotonic() + 180
                if async_mode:
                    async with stream:
                        async for event in stream:
                            assert time.monotonic() < deadline, "SSE deadline exceeded"
                            reply.observe(event)
                            if reply.complete:
                                break
                else:
                    with stream:
                        for event in stream:
                            assert time.monotonic() < deadline, "SSE deadline exceeded"
                            reply.observe(event)
                            if reply.complete:
                                break
                reply.verify([expected])
                print(f"verified session={session_id} last_event_id={reply.last_id} via SSE model={model}", flush=True)
        finally:
            failures = []
            for kind, resource_id, action in reversed(cleanups):
                try:
                    with anyio.fail_after(60):
                        await call(action)
                    print(f"cleanup {kind} {resource_id}: completed", flush=True)
                except Exception as error:
                    failures.append(f"{kind} {resource_id}: {safe_error(error)}")
            assert not failures, "Cleanup failed: " + "; ".join(failures)
