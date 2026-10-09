"""Account-backed scenarios for the newly added, non-beta API operations."""

import json
from datetime import datetime, timedelta, timezone

from qca import Forward, Managed
from tests.support.cleanup import finish_session_managed
from tests.support.harness import Run, marker, name


def usage(client: Forward, context: Run) -> None:
    end = datetime.now(timezone(timedelta(hours=8))).replace(minute=0, second=0, microsecond=0)
    bounds = {
        "start_at": (end - timedelta(hours=24)).strftime("%Y-%m-%dT%H:00:00"),
        "end_at": end.strftime("%Y-%m-%dT%H:00:00"),
    }
    for method, kind, id_field in [
        (client.usage.list_identities, "identity", "identity_id"),
        (client.usage.list_templates, "template", "template_id"),
    ]:
        page = method(**bounds, limit=2)
        if page.type != f"{kind}_usage.list" or page.start_at != bounds["start_at"] or page.end_at != bounds["end_at"]:
            raise AssertionError("Usage collection type or hourly window changed")
        if len(page.data) > 2:
            raise AssertionError("Usage exceeded the requested limit")
        for row in page.data:
            if row.type != f"{kind}_usage" or not getattr(row, id_field):
                raise AssertionError("Usage item has the wrong type or no identity")
            if row.active_seconds < 0 or row.credits < 0 or row.session_count < 0:
                raise AssertionError("Usage counters must be nonnegative")
            if kind == "template" and row.active_identities < 0:
                raise AssertionError("Active identity count must be nonnegative")
        if page.has_next_page():
            following = page.get_next_page()
            if following.start_at != page.start_at or following.end_at != page.end_at:
                raise AssertionError("Usage pagination lost the hourly window")
        ids = [getattr(row, id_field) for row in page.data]
        if ids:
            for value in [ids, ",".join(ids)]:
                filtered = method(**bounds, limit=2, **{id_field + "s": value})
                if any(getattr(row, id_field) not in ids for row in filtered.data):
                    raise AssertionError("Usage ignored the multi-ID filter")
        context.output(f"{kind}_usage_rows", len(page.data))


def credentials(client: Forward, context: Run) -> None:
    vault = client.vaults.create(display_name=name("vault"))
    context.track("vault", vault.id, lambda: client.vaults.delete(vault.id))
    original, rotated = marker(), marker()
    url = "https://example.com/" + name("mcp")
    credential = client.vaults.credentials.create(
        vault.id,
        auth={"type": "static_bearer", "mcp_server_url": url, "token": original},
        metadata={"keep": "original", "remove": "old"},
    )
    context.track(
        "credential", credential.id, lambda: client.vaults.credentials.delete(credential.id, vault_id=vault.id)
    )
    updated = client.vaults.credentials.update(
        credential.id,
        vault_id=vault.id,
        auth={"type": "static_bearer", "token": rotated},
        metadata={"remove": None, "added": "new"},
    )
    saved = client.vaults.credentials.retrieve(credential.id, vault_id=vault.id)
    patched_saved = saved
    for response in [updated, saved]:
        if (
            response.id != credential.id
            or response.auth.type != "static_bearer"
            or response.auth.mcp_server_url != url
            or response.metadata.get("keep") != "original"
            or response.metadata.get("added") != "new"
            or "remove" in response.metadata
        ):
            raise AssertionError("Credential merge patch did not preserve immutable or omitted fields")
    cleared = client.vaults.credentials.update(credential.id, vault_id=vault.id, metadata=None)
    saved = client.vaults.credentials.retrieve(credential.id, vault_id=vault.id)
    if cleared.metadata or saved.metadata:
        raise AssertionError("Null metadata did not clear the credential metadata")
    encoded = json.dumps([r.to_dict(mode="json") for r in [credential, updated, patched_saved, cleared, saved]])
    if original in encoded or rotated in encoded:
        raise AssertionError("Credential response disclosed a write-only secret")


def session_cancel(client: Managed, context: Run) -> None:
    environment = client.environments.create(name=name("env"), config={"type": "cloud"})
    context.track("environment", environment.id, lambda: client.environments.archive(environment.id))
    agent = client.agents.create(
        name=name("agent"), model={"id": context.config.model or "auto"}, tools=[{"type": "agent_toolset_20260401"}]
    )
    context.track("agent", agent.id, lambda: client.agents.archive(agent.id))
    session = client.sessions.create(agent=agent.id, environment_id=environment.id)
    context.track("session", session.id, lambda: finish_session_managed(client, context, session.id))
    for active in [False, True]:
        if active:
            client.sessions.events.send(
                session.id,
                events=[
                    {
                        "type": "user.message",
                        "content": [
                            {
                                "type": "text",
                                "text": "Use a shell command to sleep 30 seconds, then reply with SDK-LIVE.",
                            }
                        ],
                    }
                ],
            )
        raw = client.sessions.with_raw_response.cancel(session.id)
        result = raw.parse()
        if raw.status_code not in ([200, 202] if active else [200]) or (result.id, result.type, result.status) != (
            session.id,
            "session",
            "canceling",
        ):
            raise AssertionError("Session cancellation did not return the lightweight acknowledgement")
        context.output("active_cancel_http_status" if active else "idle_cancel_http_status", raw.status_code)
        while client.sessions.retrieve(session.id).status not in ("idle", "terminated"):
            context.pause()


SCENARIOS = {
    "usage": ("forward", usage),
    "credential_update": ("forward", credentials),
    "session_cancel": ("managed", session_cancel),
}
