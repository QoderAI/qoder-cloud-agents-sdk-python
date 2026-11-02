# Usage guide

Resource-specific behavior and examples for the Qoder Cloud Agents SDK. See the [README](../README.md) for installation, authentication and shared client configuration. Run shell commands from the repository root; code fragments use the clients and imports shown in the README unless stated otherwise.

- [API modes](#api-modes)
- [SDK-created Session metadata](#sdk-created-session-metadata)
- [Forward Realtime (Beta)](#forward-realtime-beta)
- [Forward SAT management](#forward-sat-management)
- [Authentication examples](#authentication-examples)
- [Usage and cancellation](#usage-and-cancellation)
- [Sessions](#sessions)
- [Streaming](#streaming)
- [Resuming a stream](#resuming-a-stream)
- [Long-running sessions](#long-running-sessions)
- [Forward Decisions (Beta)](#forward-decisions-beta)
- [Forward Drive (Beta)](#forward-drive-beta)
- [File uploads and downloads](#file-uploads-and-downloads)
- [Forward Webhooks](#forward-webhooks)
- [Resource search](#resource-search)
- [Official contract alignment](#official-contract-alignment)

## API modes

The API is exposed in two modes, and each has its own client, resources, and types. Forward is multi-tenant: sessions are created from an Identity and a Template, and it adds Schedule, Batch, Channel, and Usage. Managed is single-tenant: sessions are created from an Agent and an Environment, and it adds Deployment, Dream, and the Work API for self-hosted environments.

## SDK-created Session metadata

Direct Forward and Managed Session creation automatically adds these string-valued
metadata fields (Python includes both sync and async clients):

| Field | Value |
| --- | --- |
| `__qca_sdk_created` | `"true"` |
| `__qca_sdk_language` | `"python"` |
| `__qca_sdk_version` | The installed SDK's version |

Reserve the `__qca_sdk_` prefix for SDK provenance. Business metadata is preserved,
and the caller's metadata object is not mutated. Omitted or null metadata becomes
an object containing the markers. Passing an existing marker with the exact same
string value is accepted; a different value or type (including null) fails locally
before any HTTP request. This also applies after `extra_body` overrides are merged.

Session updates, reads and event operations do not inject or repair these fields.
Sessions created indirectly through Schedules, Batches or Realtime are outside this
behavior. These markers describe the creating SDK; they are client-supplied metadata,
not an authentication or authorization mechanism.

Migration: rename any business fields that already use these three keys before
upgrading. Automatic markers count toward API metadata limits; the SDK never drops
business fields to make room. No additional parameters or opt-in are required.

## Forward Realtime (Beta)

Forward exposes Conversation creation, WebSocket connections, and independent
history pages. The Template must already have Realtime enabled. No Realtime
Template configuration methods or extra beta header are added. See the
[creation](https://docs.qoder.com/cloud-agents/api/forward/realtime/create-conversation)
and [connection](https://docs.qoder.com/cloud-agents/api/forward/realtime/connect)
contracts.

```python
from uuid import uuid4
from qca import Forward

with Forward() as client:
    conversation = client.realtime.conversations.create(
        identity_id="idn_your_test_identity",
        template_id="tmpl_realtime_enabled",
        idempotency_key=uuid4().hex,
        config={"audio": {"output": {"voice": "longanqian"}}},
    )
    with client.realtime.connect(conversation_id=conversation.id) as connection:
        # connect returns only after voice.ready; earlier events remain iterable.
        connection.ping()
        for event in connection:
            if event.type == "pong":
                break
        outcome = connection.close_gracefully()
    page = client.realtime.conversations.history(conversation.id, limit=10)
    while page.has_next_page():
        page = page.get_next_page()  # next_before moves toward older history
```

For `AsyncForward`, await creation, history, and connection methods; use
`async with await client.realtime.connect(...)` and `async for event in connection`.
An async history page has `await page.get_next_page()`. History uses
`conversation / events / page.next_before / page.has_more`, not `data / next_page`;
`types="message"`, `"work"`, or `"message,work"` filters it. Repeated cursors fail
rather than looping. History event IDs (`vevt_*`) differ from WebSocket delivery
IDs and connection-local sequence numbers. Original timestamp strings preserve
nanosecond precision; unknown event types, payload fields, and history fields are
retained.

Connections expose `conversation_id`, typed `ready`, and optional handshake
`request_id`. They provide `send_text`, `append_audio`, `send_event`, `interrupt`,
`ping`, `playback_started`, `playback_ended`, and `playback_cancelled` (await them
on async connections). Pass the corresponding audio event's `work_id` and
`announcement_id` to playback receipts. Input is raw **16 kHz mono little-endian
PCM16**; output is **24 kHz mono PCM16**, available through `event.audio_bytes()`.
The SDK sends Base64 inside JSON text frames; it doesn't open audio devices,
resample, decode WAV, or send an `audio.commit` event. Text is trimmed and limited
to 16 KiB UTF-8. The complete outgoing JSON, including Base64, is limited to 256
KiB.

`audio.done` describes generation, not completed playback. Applications stop their
player on `playback.interrupt`, clear queued audio, and acknowledge actual
playback/cancellation; the SDK never invents receipts. `work.failed` and
nonterminal `error` events remain available without closing a healthy connection.
`voice.replaced` ends the old connection and stops sending.

`close_gracefully()` sends a request ID, waits for the matching
`connection.closed`, returns the successful outcome, and closes the transport.
A missing/mismatched acknowledgement, persistence failure, or timeout raises an
error. A server that advertises `graceful_close=false` rejects this operation.
`close()`/context exit release transport only; they don't confirm persistence,
stop background Work, or delete the Conversation. No public Conversation delete
API is assumed. Keep track of test Conversations and use dedicated resources.

Handshake/credential resolution defaults to 30 seconds, ready to 60, sending to
30, and graceful close to 10; the ordinary HTTP timeout isn't the WebSocket
lifetime. The server limits a connection to 60 minutes. The receive queue is
bounded to 256 events and 4 MiB, and incoming messages to 1 MiB; slow consumers
raise `RealtimeQueueOverflowError` and close instead of dropping events. These
limits and timeouts are keyword options on `connect`. Transport/protocol errors
are exported from `qca.forward` and belong to the existing API error hierarchy.

HTTP and each new handshake share PAT, direct SAT, and Credential header
construction. Credentials appear only in headers. Every new connection resolves
a current token; an established connection doesn't rotate its Authorization.
There are no redirects, automatic reconnects, or input replay. Custom `httpx`
clients/middleware aren't WebSocket transports: configure `ssl_context` and
`proxy` on `connect` (system proxy by default, `None` to disable). Synchronous
Credential providers can't be forcibly stopped; if a deadline/cancellation wins,
their background call may finish later without opening a WebSocket.

The Realtime service currently requires a **Forward-issued, bound SAT** in SA
mode. Pass that token as `Forward(auth_mode="sa", access_token=forward_sat)`
(or use a custom provider that returns such a token). A platform SAT obtained
from `ServiceAccountCredential` does not create this Forward token binding.
The SDK does not automatically issue or bind a Forward SAT.

Runnable text, PCM, and history examples reuse the existing PAT/SA configuration:

```bash
python -m examples.forward.realtime --identity-id ID --template-id ID --text "Hello"
python -m examples.forward.realtime --identity-id ID --template-id ID --pcm input.pcm --async
python -m examples.forward.realtime --conversation-id ID --history-only
```

For SA examples, set `QODER_AUTH_MODE=sa` and `QODER_ACCESS_TOKEN` to the
Forward-issued SAT; leave `QODER_SA_KEY` empty.

The PCM example sends 20 ms chunks and validates output without playing it.
Use `--help` for a no-network check. CN/Global integration is separate from daily
business tests: configure the dedicated `QODER_REALTIME_*` fields in
`.env.live.example` and run `uv run make test-live-realtime`. It preflights both
regions, requires explicit write/model flags, creates persistent Conversations,
and covers ready, ping, short text response (or explicit PCM input), graceful close,
history, and temporary Identity cleanup in both PAT/SA and sync/async modes.
It records persistent Conversation IDs. Background Work and actual speaker
playback still require dedicated acceptance scenarios.
Use `QODER_REALTIME_CN_SAT` and `QODER_REALTIME_GLOBAL_SAT` for SA acceptance;
these take priority over the platform Credential path retained for diagnostics.

## Forward SAT management

Forward exposes explicit admin/Identity SAT issuance and revocation in addition
to automatic platform exchange. These three endpoints authenticate with an
**SA Key**, supplied per method call; ordinary business requests still use PAT
or SAT. The Key overrides client/request Authorization only for that call, is
never included in the JSON body, and is not saved on the client.

`ttl_seconds` is optional (1-43200); omission uses the issuer's default. Issuance
and revocation are not automatically retried, even when the client or request
allows retries. Do not blindly repeat an issuance after an uncertain network
failure: it may already have issued a token. Metadata is for audit information,
not secrets. Keep the issuance response's Token ID, Credential ID and expiry for
precise revocation. A returned static SAT does not renew automatically, and
revocation affects its Forward binding; it does not cancel an already-running
Session or revoke unrelated Managed/platform access. Never log the SA Key, SAT,
serialized token response or Authorization headers.

Run `uv run make test-live-sa-tokens` with `QODER_SA_CN_KEY`,
`QODER_SA_GLOBAL_KEY` and `QODER_SA_LIVE_ALLOW_WRITE=true` to verify both regions.
This separate suite issues admin and Identity SATs, checks business access and
cross-Identity refusal, then revokes the tokens, verifies access is refused and
deletes its temporary Identities. It does not execute a model or require
`QODER_SA_LIVE_ALLOW_EXECUTION=true`.

```python
with Forward(base_url=forward_base_url) as issuer:
    # Admin: issuer.service_account_tokens.create(sa_key=sa_key, ...).
    token = issuer.identities.service_account_tokens.create(
        identity_id, sa_key=sa_key, ttl_seconds=600,
    )
    try:
        with Forward(base_url=forward_base_url, auth_mode="sa",
                     access_token=token.access_token) as runtime:
            page = runtime.sessions.list(identity_i_ds=[identity_id], limit=1)
    finally:
        issuer.service_account_tokens.revoke(
            token.auth_token_id, sa_key=sa_key,
            target_credential_id=token.credential_id,
            target_expires_at=token.expires_at, reason="runtime complete",
        )
```

`AsyncForward` exposes the same methods with `await`, including raw/streaming
response views. Runnable example: `uv run python -m examples.auth.forward_tokens`.
It revokes its token even if the business call fails. Set `QODER_SA_KEY` and
`QODER_SA_REGION=cn|global`; set `QODER_IDENTITY_ID` for Identity mode, or leave it
unset for admin mode.

See the official [admin issuance](https://docs.qoder.com/cloud-agents/api/forward/service-account-tokens/create),
[Identity issuance](https://docs.qoder.com/cloud-agents/api/forward/service-account-tokens/create-identity)
and [revocation](https://docs.qoder.com/cloud-agents/api/forward/service-account-tokens/revoke) contracts.

## Authentication examples

The two read-only examples under `examples/auth/` show client construction directly:
SA Key exchange with automatic caching/renewal, and direct SAT access with renewal
managed by the caller. Each lists Forward templates and Managed agents; no model
execution or resources are created. The SA needs both API scopes/permissions and
its Managed workspace binding in the selected region.

```sh
# These standalone demos read process environment variables (not .env.live).
# Configure QODER_SA_REGION=cn|global and only the credential needed by the demo.
uv run python -m examples.auth.sa_key       # QODER_SA_KEY; unset QODER_ACCESS_TOKEN
uv run python -m examples.auth.sa_key --async
uv run python -m examples.auth.sa_token     # QODER_ACCESS_TOKEN; unset QODER_SA_KEY
```

The existing business examples keep PAT as the default and read `.env.live`.
Set `QODER_AUTH_MODE=sa` to select SA explicitly, then configure exactly one of
`QODER_SA_KEY` and `QODER_ACCESS_TOKEN`. `QODER_SA_REGION=cn|global` selects both the
business and exchange hosts; `--region` overrides it (`international` remains an
alias for `global`). Leave the unused credential empty. Ambient PATs are ignored
in SA mode; missing SA credentials and conflicting Key/SAT inputs fail before a
request is sent. The async Session examples use the same configuration and manage
an `AsyncServiceAccountCredential` for SA Key access. This selection is example
configuration, not implicit SDK behavior.

```sh
# With the SA credential configured in .env.live, reuse any business example.
QODER_AUTH_MODE=sa QODER_SA_REGION=cn uv run python -m examples.forward.models
QODER_AUTH_MODE=sa QODER_SA_REGION=global uv run python -m examples.managed.session
# Continue an existing session with native async I/O.
QODER_AUTH_MODE=sa QODER_SESSION_ID=sess_... uv run python -m examples.managed.async_session
```

For a centralized SAT service, supply `Forward(auth_mode="sa", credential=my_token_provider)`.
The provider's `get_token()` returns the current SAT and manages its renewal;
async clients also support an async `get_token()`.

## Usage and cancellation

Forward Usage requires PAT or Admin SAT.

```python
with Forward() as client:
    for row in client.usage.list_identities(
        start_at="2026-09-14T09:00:00", end_at="2026-09-14T12:00:00",
        identity_ids=["idn_one", "idn_two"],
    ):
        print(row.identity_id, row.active_seconds, row.credits)

with Managed() as client:
    acknowledgement = client.sessions.cancel("sess_one")
    for run in client.deployments.runs.list("dep_one", limit=20):
        print(run.id)
    run = client.deployments.runs.retrieve("drun_one", deployment_id="dep_one")
```

`usage.list_templates` accepts the same filters. Bounds are whole hours in
Asia/Shanghai for CN and Global, with an inclusive start, exclusive end, and a
maximum 744-hour span. Multi-ID filters accept lists or comma-separated strings.
`active_seconds` preserves fractions. Legacy timestamp parameters and
`duration_seconds` are not exposed.

`client.vaults.credentials.update("cred_one", vault_id="vault_one", auth={...})`
rotates write-only secrets; only auth and metadata are patched, and omitted fields
are preserved. `metadata=None` clears metadata; `metadata={"key": None}` deletes a
key. This operation never retries automatically, even if client retries are enabled.

Session cancellation returns the lightweight `canceling` acknowledgement for
active (HTTP 202) and idle (HTTP 200) sessions. The global `deployment_runs` resource
remains available. All new methods also exist on `AsyncForward` / `AsyncManaged`;
await requests or iterate pages with `async for`.

## Sessions

A session is the unit of agent execution. Forward materializes one from an Identity and a Template:

```python
from qca import Forward

with Forward() as client:
    environment = client.environments.create(name="demo", config={"type": "cloud"})
    identity = client.identities.create(external_id="example-user", name="Example User")
    template = client.templates.create(
        name="assistant",
        environment_id=environment.id,
        model="ultimate",  # use a model enabled for the current account
        system="Answer questions from the material you can read.",
        tools=[{"type": "agent_toolset_20260401"}],
    )
    session = client.sessions.create(identity_id=identity.id, template_id=template.id)
    print(session.id)
```

Managed creates one from an Agent and an Environment:

```python
from qca import Managed

with Managed() as client:
    environment = client.environments.create(name="demo", config={"type": "cloud"})
    agent = client.agents.create(
        name="assistant",
        model={"id": "ultimate"},
        system="Answer questions from the material you can read.",
        tools=[{"type": "agent_toolset_20260401"}],
    )
    session = client.sessions.create(environment_id=environment.id, agent=agent.id)
    print(session.id)
```

Both snippets create billable resources on the server. Template names are unique within an account, and templates and sessions cannot be deleted — only archived — so give them distinct names rather than reusing one. Runnable scenarios with assertions and cleanup live in the `examples/` directory.

## Streaming

Send events to a session, then read the server's response as an SSE stream. The code below works with either client.

```python
from uuid import uuid4

sent = client.sessions.events.send(
    session_id,
    events=[{"type": "user.message", "content": [{"type": "text", "text": "Hello"}]}],
    idempotency_key=uuid4().hex,
)

with client.sessions.events.stream(
    session_id,
    last_event_id=sent.data[0].id,
    event_deltas=["agent.message"],
) as stream:
    for event in stream:
        if event.type == "agent.message":
            print(event.to_json())
        elif event.type == "session.status_idle":
            print(event.stop_reason)
            break
        elif event.type in ("session.error", "session.status_terminated"):
            raise RuntimeError(f"Session stopped: {event.type}")
```

Reuse one `session_id` for the whole conversation, and reuse one idempotency key across HTTP retries of the same logical message. `event_deltas` opts into incremental events for the listed types; those previews are not deduplicated, and the final event repeats the complete content, so render deltas but treat the final event as the source of truth. An idle status does not by itself mean success — the session may be waiting for a confirmation or have reached its budget, so check `stop_reason` and the final reply.


### Thread event resumption

Forward and Managed also support automatic resumption for a single Thread. Use the
same retry and cancellation behavior as Session streams, with a thread-scoped
`Last-Event-ID` cursor:

```python
# Forward and Managed use the same call shape.
with client.sessions.threads.events.resumable_stream(
    thread_id, session_id=session_id, last_event_id=after_id,
) as stream:
    for event in stream:
        print(event.type)

# AsyncForward / AsyncManaged
async with async_client.sessions.threads.events.resumable_stream(
    thread_id, session_id=session_id, last_event_id=after_id,
) as stream:
    async for event in stream:
        print(event.type)
```

`session.thread_status_idle` ends only the current turn, so the subscription stays
open. `session.thread_status_terminated`, `session.status_terminated`, or
`session.deleted` ends it normally. A non-retryable error (including an invalid
cursor or missing thread) is returned to the caller; the SDK never clears the
cursor to silently start over. The existing one-shot Thread stream remains
available. See the [Forward Thread stream](https://docs.qoder.com/cloud-agents/api/forward/sessions/stream-thread-events)
and [Managed Thread stream](https://docs.qoder.com/cloud-agents/api/sessions/threads/events/stream)
contracts for cursor validity.

## Resuming a stream

The low-level `stream()` method exposes `stream.last_event_id` but does not reconnect. Use the handwritten `resumable_stream()` helper to reconnect automatically after EOF, timeouts, transient transport failures, and retryable HTTP statuses. It checkpoints only complete events and sends the latest checkpoint as `Last-Event-ID`; close it with a context manager when finished.

```python
with client.sessions.events.resumable_stream(
    session_id,
    last_event_id=saved_event_id,
    event_deltas=["agent.message"],
) as stream:
    for event in stream:
        saved_event_id = stream.last_event_id
        print(event.type)
```

The async form is a native async iterator and context manager; unlike `stream()`, constructing it does not require `await`:

```python
async with client.sessions.events.resumable_stream(session_id) as stream:
    async for event in stream:
        print(event.type)
```

The helper retries until closed, cancelled, or it receives `session.status_terminated` / `session.deleted`. It uses jittered exponential backoff and the same HTTP retry classification as the client (in particular, `409` is not retried). It does not query event history, discard an invalid cursor, or deduplicate event IDs because multiple preview deltas may share one ID.

With the default synchronous HTTP/1.x transport, `close()` also wakes a body read
blocked in another thread, including over HTTPS. HTTP/2 connections are shared,
so their sockets are not interrupted; HTTP/2 and custom transports without an
exposed socket retain their transport's close behavior. Async callers can cancel
the consuming task or await `close()` to interrupt an active read.

Events are also readable after the fact through `client.sessions.events.list(session_id)`, which paginates like any other list method.

## Long-running sessions

An agent run can take minutes, and the read timeout applies to each read from the stream, not to the stream as a whole. A session that stays silent longer than the read timeout raises `APITimeoutError` even though it is still running, so raise the timeout when you open a long stream and resume with `last_event_id` if the connection drops anyway.

```python
with client.sessions.events.stream(session_id, timeout=None) as stream:
    ...
```

## Forward Decisions (Beta)

The Decision API is in Beta. Its behavior may change in future updates.

Evaluate a nonempty `state` object or an accessible `session_id` (exactly one)
with 1–32 choice or score questions. Choice values are strings or booleans;
score questions select from your numeric levels. Creation waits for the result.
The service selects the model; no `model` parameter is accepted. Normal PAT or
SAT authentication determines the caller's access.

```python
from uuid import uuid4
from qca import Forward

with Forward() as client:  # Or use the PAT/SA configuration above.
    decision = client.decisions.create(
        state={"message": "My issue is resolved."},
        questions=[{
            "type": "choice", "name": "resolved",
            "instructions": "Has the user confirmed resolution?",
            "choices": [{"value": True}, {"value": False}],
        }],
        idempotency_key=str(uuid4()),
    )
    stored = client.decisions.retrieve(decision.id)
    print(stored.answers)
    page = client.decisions.list(limit=20)
    print(page.data)  # Iterate over page directly to follow all pages.
```

For Session input, replace `state=...` with `session_id=session_id`.
For scores, use `{"type": "score", "instructions": "Rate risk", "levels":
[{"label": "low", "score": 0}, {"label": "high", "score": 10}]}`.
`AsyncForward` offers the same methods with `await` and asynchronous pagination.

Session context is selected by the server. `context.mode` identifies the input
mode; Session results may include event IDs and counts describing the selected
history. Answers have type `choice` or `score`. Oversized input returns HTTP 422.

Reuse an idempotency key only for identical request bytes. A changed request or
a still-running request with that key returns HTTP 409; the SDK does not retry
that conflict automatically. Creation errors can contain `decision_id` in the
standard API error body. Retrieve and list can return running or failed records.
Lists preserve server order and support `after_id` / `before_id` cursors (one at
a time), optional `session_id`, and a limit of 1–100. There is no delete endpoint;
Decision records expire according to server retention.

See the [runnable example](../examples/forward/decisions.py) and the
[opt-in live test instructions](../CONTRIBUTING.md#decision-live-tests).

## Forward Drive (Beta)

Drive is a Beta API. It uses `entries` / `next_page_token`, not the ordinary
resource paginator. Pass `identity_id` even with an Identity SAT, preserve the
server order, and reuse a cursor only within the same Identity, directory and
authentication scope. Paths are relative; the SDK preserves slashes when encoding
the list query and leaves path validation to the service.

Upload/download methods return a signed URL, method, headers and expiry. Send the
storage request with a separate HTTP client using only those returned headers;
do not attach QCA credentials or log signed URLs. Replaying an `Idempotency-Key`
does not renew the URL: use a new key or omit it when requesting a fresh URL.

Deleting a nonempty directory requires `recursive=true`; `clear` deletes the
entire selected Identity Drive. Partial failures retain `drive_delete_partial`
and `deleted_count` in the standard API error body. Direct Drive APIs do not
require Template tool configuration.

```python
page = client.drives.list_entries(identity_id=identity_id, path="reports", limit=20)
for entry in page.entries:
    print(entry.path)
if page.next_page_token:
    page = client.drives.list_entries(
        identity_id=identity_id, path="reports", page_token=page.next_page_token,
    )
# Replace the complete managed-tool list, retaining any other tools you need.
client.templates.update(template_id, managed_tool_config={"enabled_tools": ["drive"]})
```

`AsyncForward` exposes the same methods with `await`. Run the
[file lifecycle example](../examples/forward/drive.py) with
`python -m examples.forward.drive --region cn` (or `global`); it uses the shared
PAT/SA configuration and creates a fresh Identity. A directory has `size=None`;
a zero-byte file has `size=0`.
For maintainers, `uv run make test-live-drive` tests CN/Global × PAT/admin
SAT/Identity SAT with both sync and async clients.

To enable Agent-managed Drive tools, use Template `managed_tool_config.enabled_tools`.
It is separate from `tools[].enabled_tools` and replaces the entire list; an empty
list disables managed tools, omission preserves the setting, and `null` clears it.
Full Agent Drive usage also requires the DeliverArtifacts tool. Internal
`/forward-mcp` routes are invoked by the runtime and are not public SDK methods.

The Drive live suite requires `QODER_DRIVE_LIVE_ALLOW_WRITE=true`,
`QODER_FORWARD_CN_PAT`, `QODER_FORWARD_GLOBAL_PAT`, `QODER_SA_CN_KEY`, and
`QODER_SA_GLOBAL_KEY` in `.env.live` (or `LIVE_ENV_FILE`). It creates isolated
Identities, verifies storage transfers, pagination, deletion, Identity isolation,
and Template configuration, then clears only those new Identities. It does not
run Agent/model tool execution.

## File uploads and downloads

Uploads accept `bytes`, a binary file object, a `Path`, or a `(filename, content[, content type])` tuple. Content is buffered so it can be replayed on retry; a file object you open stays yours to close.

```python
from pathlib import Path

file = client.files.upload(file=Path("report.txt"))

skill = client.skills.create(files=[("example/SKILL.md", b"---\nname: example\n---\nExample skill")])

with client.files.download(file.id) as content:
    content.write_to_file("downloaded.txt")
```

Relative paths are preserved in the multipart filename, which is how a Skill keeps its directory layout. A file download first requests a temporary link and then streams from object storage; API credentials, default headers, and cookies are not sent to the storage host. Async downloads are awaited: `response = await client.files.download(...)`, then `await response.write_to_file(...)`.

## Forward Webhooks

Manage webhook endpoints and verify signed event deliveries. See [Webhook usage and receiver examples](../docs/webhooks.md).

## Resource search

Search uses `POST /<resource>/search` with typed filters in the JSON body.
The SDK automatically includes `x-qoder-beta: search-2026-08-31`, preserving
other effective beta flags. Calling Search with no filters sends `{}`.

- Forward: Environments, Skills, Vaults, and Files.
- Managed: Agents, Sessions, Deployments, Environments, Skills, Vaults, Files,
  and Memory Stores.

Metadata filters are exact string matches combined with AND. Each resource also
supports its documented filters, such as name, creation time, Session status,
or Skill source/display title. See the official
[Forward search](https://docs.qoder.com/cloud-agents/api/forward/environments/search)
and [Managed Session search](https://docs.qoder.com/cloud-agents/api/sessions/search)
contracts. This searches QCA resources; it does not perform a web search.

Forward's `identity_id` selector is sent only in the URL query. Set it when a PAT
should search an Identity's resources; omit it with all SATs, whose scope comes
from the token. Search cursors are opaque: automatic pagination puts `next_page`
back into the JSON body's `page` while preserving filters, ownership, and request
options. Existing List methods retain their GET/query pagination behavior.

```python
# client is a Forward client.
for environment in client.environments.search(
    metadata={"team": "core"},
    name="dev",
    identity_id="idn_example",  # PAT only; omit for SAT.
    limit=20,
):
    print(environment.id)

# managed_client is a Managed client. Time filters accept datetime or RFC 3339 strings.
page = managed_client.sessions.search(
    metadata={"ticket": "A-123"},
    statuses=["idle", "running"],
    created_at_gte="2026-01-01T00:00:00Z",
)

# async_client is an AsyncForward client.
async for environment in async_client.environments.search(metadata={"team": "core"}):
    print(environment.id)
```

Synchronous searches return `SyncPage`; asynchronous searches can be awaited for
an `AsyncPage` or directly iterated with `async for`. Use `get_next_page()` for
manual pagination (await it on an async page). `*SearchParams` TypedDicts are
exported from `qca.forward.types` and `qca.managed.types`.

## Official contract alignment

The next release aligns these public types with the official API documentation
retrieved on 2026-10-27. It introduces source changes relative to 0.12.0:
Outcome `rubric` is an object; Managed Agent `effort` is a string; Managed Agent
and Dream model objects do not accept `speed`. Managed Dream `model` is optional
and defaults to `auto`. Discover model IDs and supported efforts/context windows
with List models. These Managed model changes do not remove Forward model features.

```python
from qca import Forward, Managed

client = Forward(pat="...")
rubric = {"type": "text", "content": "report exists"}
model = {"id": "ultimate", "effort": "high"}
dream = client.dreams.create(inputs=[{
    "type": "identity_template", "identity_id": "idn_...", "template_id": "tmpl_...",
}])  # model defaults to auto

for mount in client.identities.memory_stores.list(
    "tmpl_...", identity_id="idn_...", limit=20,
):
    print(mount.memory_store_id)
```

The async mount list returns an `AsyncPaginator`: use `async for` directly, or
`await` it to obtain the first `AsyncPage`. Sync lists return `SyncPage`.
Identity `tools=[]` replaces all tools with no tools; `tools=None` clears that
override. Pass `managed_tool_config={"schedule": {"enabled": False}, "drive": None}`
to disable Schedule tools and restore inherited Drive settings. Omitted values
remain unchanged. Multiagent `agents` accepts Template ID strings and
`{"type": "advisor", "model": "ultimate"}` objects.

New Forward Dream calls require a PAT or an admin SAT; an Identity SAT is not
supported. Inputs contain exactly one primary Memory Store or Identity/Template
source, optionally plus Session sources. Pairing `update` changes an active
binding; supply at least one nonempty Identity or Template ID. Use pairing
`create` to complete a pending pairing. Pending records preserve empty
`identity_id`, `template_id`, and `paired_at` strings.

Identity `auto_memory_store=false` disables automatic default-store creation.
Independent mounts now accept `access="read_write"`; omit access for a new
read-only mount, or to preserve an existing mount's permission. Schedule
`resources` accepts file entries and `[]` clears them; Run retrieval supports
`include_initial_events=true` to return the saved input snapshot.

Managed cloud Environment `config.storage.buckets` supports up to eight OSS
mounts. When the resulting configuration has buckets, explicitly include beta
`oss-bucket-2026-09-23` (`Betas` in Go, `betas` in Python/TS). Send credentials
only when creating or replacing them; omit `credential` on an existing named
bucket to keep it. Responses expose a read view without role ARN or AccessKey
secret. `storage: {buckets: []}` clears mounts.

Managed `OAuth.Start` (Go) / `oauth.start` (Python/TS) returns `authorization_url`,
`state`, and `callback_origin`; the user completes authorization in a browser.
Client secrets go in the POST body, never in a URL. This method does not open a
browser or complete consent automatically.

See the official [Outcome contract](https://docs.qoder.com/cloud-agents/api/forward/sessions/send-events),
[Identity overrides](https://docs.qoder.com/cloud-agents/api/forward/identities/upsert-config),
[Dream inputs](https://docs.qoder.com/cloud-agents/api/forward/dreams/create),
[OSS storage](https://docs.qoder.com/cloud-agents/api/environments/storage-buckets),
and [OAuth flow](https://docs.qoder.com/cloud-agents/api/vaults/start-oauth).
