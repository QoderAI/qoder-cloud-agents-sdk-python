# Qoder Cloud Agents Python SDK

[Changelog](CHANGELOG.md) · [Releases](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/releases)

[![PyPI version](https://img.shields.io/pypi/v/qca-sdk.svg)](https://pypi.org/project/qca-sdk/)

The Qoder Cloud Agents Python SDK provides access to the Qoder Cloud Agents API from Python 3.10+. It ships synchronous and natively asynchronous clients, typed request parameters and response models, automatic pagination, SSE streaming, and file transfer.

The API is exposed in two modes, and each has its own client, resources, and types. Forward is multi-tenant: sessions are created from an Identity and a Template, and it adds Schedule, Batch, Channel, and Usage. Managed is single-tenant: sessions are created from an Agent and an Environment, and it adds Deployment, Dream, and the Work API for self-hosted environments.

## Installation

```bash
python -m pip install qca-sdk
```

The distribution is named `qca-sdk`; the import package is `qca`. The package is pre-1.0, so pin the version your application uses. To work from a checkout of this repository instead:

```bash
python -m pip install .
python -m pip install -e '.[dev]'   # development environment
```

## Requirements

Python 3.10 or newer. The runtime dependencies are `httpx`, `pydantic` v2, `anyio`, `typing-extensions`, and `websockets` 16.x; the package is typed and ships `py.typed`.

## Generating documentation

The API reference under `docs/api/` is generated from the public source and
committed. Regenerate and verify it with:

```bash
make docs          # regenerate docs/api/ from src/qca
make docs-check    # regenerate + drift/link/snippet checks (offline)
```

Under the hood these run `pydoc-markdown` via `uv` on a pinned Python 3.12:

```bash
uv run --python 3.12 --extra dev --locked pydoc-markdown pydoc-markdown.yml
```

## Usage

```python
from qca import Forward

with Forward() as client:
    for model in client.models.list().data:
        if model.is_enabled:
            print(model.id)
```

```python
from qca import Managed

with Managed() as client:
    for agent in client.agents.list(limit=20):
        print(agent.id, agent.name)
```

Both clients read their token from the environment. `from qca.forward import Client` and `from qca.managed import Client` are equivalent entry points.

| Setting | Forward | Managed |
|---|---|---|
| Token | `QODER_ACCESS_TOKEN` (PAT mode falls back to `QODER_PAT`) | `QODER_ACCESS_TOKEN` (PAT mode falls back to `QODER_PAT`) |
| Base URL | `QODER_FORWARD_BASE_URL` | `QODER_MANAGED_BASE_URL` |
| Default base URL | `https://api.qoder.com/api/v1/forward/` | `https://api.qoder.com/api/v1/cloud/` |

Explicit arguments take precedence over environment variables. The clients never read `.env` files; examples and explicit live-test commands have their own config loaders. Other regions, including China, have to be configured explicitly:

```python
client = Forward(
    pat="your-access-token",
    base_url="https://api.qoder.com.cn/api/v1/forward",
    timeout=30.0,
    max_retries=2,
)
```

A client owns an HTTP connection pool, so it should be closed when you are done with it — either through the context manager above or with `client.close()`.

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

## PAT and Service Account authentication

PAT and SA are parallel modes. Existing `pat=` calls remain supported. For an
existing SAT use `Forward(auth_mode="sa", access_token=token)` (Managed and async
clients accept the same configuration). `QODER_ACCESS_TOKEN` supplies the selected
mode's token; only PAT mode falls back to `QODER_PAT`. Ordinary clients do not read
`QODER_SA_KEY` or implicitly exchange it.

```python
from qca import Forward, Managed, ServiceAccountCredential

with ServiceAccountCredential.from_env(
    region="global", scopes=["qca.access", "forward.access"]
) as credential:
    with Forward(credential=credential) as forward, Managed(credential=credential) as managed:
        templates = forward.templates.list(limit=1)
        agents = managed.agents.list(limit=1)
```

Use `AsyncServiceAccountCredential` with `AsyncForward`/`AsyncManaged` and `async
with`; native sync/async credentials must match the client. For CN, select
`region="cn"` and the matching `https://api.qoder.com.cn/api/v1/forward/` or
`https://api.qoder.com.cn/api/v1/cloud/` BaseURL. Managed-only access can request
`["qca.access"]`. Permissions and workspace bindings are configured server-side.

The instance-owned cache uses the server's actual TTL and a monotonic clock.
Concurrent calls share exchange results; failures enter a cooldown. Transient
failures may reuse a still-safe SAT; authentication and invalid-response failures
cannot. Expiry is handled before the next request, without background refresh,
PAT fallback, or replaying a 401 write. Existing streams are not closed by expiry.
Sync exchange uses httpx phase timeouts (default 30 seconds); async exchange also
has an independent total deadline. Cancelling an async owner releases the shared
state so another caller can exchange; cancelling a waiter does not cancel its owner.
Close the credential separately: business clients do not own it. Injected exchange
HTTP clients remain caller-owned.

Do not combine `access_token` with `pat` or `credential`, or an SA credential with
a static token. Explicit `pat` + legacy custom credential retains PAT precedence;
explicit credentials now override ambient PAT. Request Authorization overrides
remain supported. `with_options` retains mode/source and accepts `credential`,
`access_token`, and `auth_mode`; switching mode clears the prior credentials.

Run the separate read-only CN/Global suite with `uv run make test-live-sa`, setting
`QODER_SA_CN_KEY` and `QODER_SA_GLOBAL_KEY` in `.env.live` or the process environment.
Process variables take precedence; `LIVE_ENV_FILE` selects another file when using
Make. All selected regions' keys are checked before the first API call. For
write/read, Session SSE and cleanup verification, run
`uv run make test-live-sa-execution` with `QODER_SA_LIVE_ALLOW_WRITE=true` and
`QODER_SA_LIVE_ALLOW_EXECUTION=true`. `QODER_SA_MODEL` defaults to `auto`.
Existing PAT tests remain separate; `QODER_AUTH_MODE` switches examples, not the
PAT test suites. See the
[official authentication contract](https://docs.qoder.com/cloud-agents/api/conventions/authentication).

### Forward SAT management

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

### Authentication examples

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

## Async usage

`AsyncForward` and `AsyncManaged` are built on `httpx.AsyncClient`. Requests, retry backoff, and SSE reads are all native async I/O; only local file reads are delegated to a worker thread.

```python
import asyncio
from qca import AsyncManaged


async def main() -> None:
    async with AsyncManaged() as client:
        async for agent in client.agents.list(limit=20):
            print(agent.id)

        first_page = await client.sessions.list(limit=10)
        print(first_page.data)


asyncio.run(main())
```

Every method shown in this document has an async counterpart with the same name and signature. Async streams are opened with `async with await client.sessions.events.stream(...)`.

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

Events are also readable after the fact through `client.sessions.events.list(session_id)`, which paginates like any other list method.

## Handling errors

`APIConnectionError` is raised when the request never reached the API; `APITimeoutError` is its timeout subclass. A non-2xx status raises an `APIStatusError` subclass. Invalid JSON, invalid download URLs, and response schema mismatches when strict response validation is enabled raise `APIResponseValidationError`. All of them derive from `qca.APIError`.

```python
from qca import APIConnectionError, APIStatusError, APITimeoutError

try:
    session = client.sessions.retrieve("sess-id", timeout=10)
except APITimeoutError:
    print("The request timed out")
except APIConnectionError:
    print("The connection failed")
except APIStatusError as exc:
    print(exc.status_code, exc.message, exc.code, exc.type, exc.request_id)
```

| Status | Exception |
|---|---|
| 400 | `BadRequestError` |
| 401 | `AuthenticationError` |
| 403 | `PermissionDeniedError` |
| 404 | `NotFoundError` |
| 409 | `ConflictError` |
| 413 | `RequestTooLargeError` |
| 422 | `UnprocessableEntityError` |
| 429 | `RateLimitError` |
| 529 | `OverloadedError` |
| other 5xx | `InternalServerError` |
| other | `APIStatusError` |

`code` and `type` are read from the error body and are `None` when the server omits them, so log `message` and `request_id` as well. A non-JSON error body is kept verbatim in `.body`.

`RequestTooLargeError` and `OverloadedError` inherit directly from `APIStatusError`, matching Anthropic. Code that previously caught `InternalServerError` for status 529 should now catch `OverloadedError` as well, or catch `APIStatusError` for all HTTP errors.

## Response validation

By default, responses are constructed into models without requiring every field to match the declared schema, matching Anthropic's Python SDK. Nested objects are still converted to models and unknown fields are retained. Unexpected field values may keep their original type, so type annotations describe the expected API schema rather than guaranteeing the runtime value.

To require Pydantic response validation and raise `APIResponseValidationError` on a schema mismatch, enable the constructor option:

```python
client = Forward(_strict_response_validation=True)
```

The option is available on `Forward`, `Managed`, `AsyncForward`, and `AsyncManaged`, and is preserved by `with_options`, raw and streaming response views, pagination, and SSE parsing. Invalid JSON and invalid download URLs still raise `APIResponseValidationError` in either mode. Direct construction or validation of model classes continues to use Pydantic validation.

## Request IDs

Every response model carries the `x-request-id` of the call that produced it, and errors expose the same value. Include it when reporting a problem.

```python
identity = client.identities.retrieve("identity-id")
print(identity._request_id)
```

## Retries

Certain errors are retried twice by default with exponential backoff. GET and HEAD requests, and any request carrying an idempotency key, are retried on connection errors, 408, 429, and 5xx; other requests are retried on 429 only. A 409 is never retried automatically, and an SSE stream that has already been established is never retried. Within those rules the SDK honors `x-should-retry` and a valid `Retry-After-Ms` or `Retry-After`.

Positive server-requested delays, including values over 60 seconds, are honored up to 4,294,967 seconds, matching Anthropic's Python SDK. A numeric `Retry-After-Ms` takes precedence over `Retry-After`, which accepts seconds or an HTTP date. Zero, negative, or invalid delays fall back to exponential backoff. A server-requested wait can therefore exceed the timeout configured for an individual HTTP attempt.

```python
client = Forward(max_retries=0)  # disable for all requests
client.with_options(max_retries=5).sessions.list()  # or override per call site
```

`with_options` returns a separately configured client that shares the original connection pool, so closing either one closes that pool.

## Timeouts

The default timeout is 5 seconds to connect and 600 seconds each for reading data, writing data, and acquiring a connection from the pool, matching Anthropic's Python SDK. These are phase timeouts, not a total request deadline. Pass a float of seconds, an `httpx.Timeout`, or `None` to disable.

```python
client = Forward(timeout=30.0)
client.sessions.retrieve("sess-id", timeout=5.0)  # per request
```

Timeouts apply per HTTP phase and per attempt, not to the whole call including retries. End-to-end deadlines are the caller's responsibility; async code can wrap a call in `asyncio.wait_for`.

## Long-running sessions

An agent run can take minutes, and the read timeout applies to each read from the stream, not to the stream as a whole. A session that stays silent longer than the read timeout raises `APITimeoutError` even though it is still running, so raise the timeout when you open a long stream and resume with `last_event_id` if the connection drops anyway.

```python
with client.sessions.events.stream(session_id, timeout=None) as stream:
    ...
```

## Auto-pagination

List methods return a page that iterates across page boundaries for you.

```python
page = client.sessions.list(limit=20)
print(page.data)  # just this page
print(page.has_next_page())

for session in page:  # fetches subsequent pages as needed
    print(session.id)

for page in client.sessions.list().iter_pages():
    print(len(page.data))
```

Cursor pagination with `after_id` / `before_id` and page-token pagination with `next_page` are both handled, and filters are carried into subsequent requests. The SDK raises rather than looping forever if a cursor stops advancing. A few endpoints, such as Models, return an unpaginated list; read those through `.data`.

## Nested resources

For a nested resource the target ID may be passed positionally, while ancestor IDs are always keyword arguments.

```python
credential = client.vaults.credentials.retrieve("credential-id", vault_id="vault-id")
memory = client.memory_stores.memories.retrieve("memory-id", memory_store_id="store-id")
```

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
[file lifecycle example](examples/forward/drive.py) with
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

## Default headers and query parameters

Headers and query parameters can be set for every request on a client, or for one request.

```python
client = Forward(default_headers={"X-Trace-Id": "abc"}, default_query={"debug": "1"})

client.sessions.list(extra_headers={"X-Trace-Id": "override"}, extra_query={"debug": "0"})
```

Every method accepts `extra_headers`, `extra_query`, `extra_body`, and `timeout`. These values are applied last, so they override anything the method itself would send — including the `Authorization` header.

## Type system

Request parameters are `TypedDict`s, declared per mode in `types/*_params.py`. Pass plain dicts for nested parameters, and pass the matching string, dict, or list for a union. Responses are Pydantic models: read fields as attributes, and unknown fields the server adds are preserved rather than dropped.

```python
from qca import NOT_GIVEN

client.identities.update("identity-id", name=NOT_GIVEN)  # omit the field
client.identities.update("identity-id", name=None)  # send null
client.identities.update("identity-id", enabled=False)  # send false

identity = client.identities.retrieve("identity-id")
print(identity.to_dict(), identity.to_json())
print("name" in identity.model_fields_set)  # tells a missing field from an explicit null
```

An omitted argument is left out of the request body entirely, while `None` is serialized as `null`; empty strings, empty arrays, empty objects, `0`, and `false` are all sent as given. Whether a field can actually be cleared is decided by the server.

## Advanced usage

Prefix any method with `with_raw_response` to get the status code and headers alongside the parsed body.

```python
raw = client.models.with_raw_response.list()
print(raw.status_code, raw.headers)
models = raw.parse()
```

Use `with_streaming_response` when the headers have to be inspected before the body is read, or when the body should be consumed in chunks. The connection is released when the context exits.

```python
with client.models.with_streaming_response.list() as response:
    print(response.headers)
    models = response.parse()
```

The async forms are `await raw.parse()` and `async with client.models.with_streaming_response.list()`; a streaming body can also be iterated with `iter_bytes()` or `iter_lines()`.

## HTTP client

Pass your own `httpx.Client` (or `httpx.AsyncClient`) to control proxies, transports, TLS, and connection limits.

```python
import httpx
from qca import Forward

with Forward(http_client=httpx.Client(proxy="http://localhost:8080")) as client:
    print(client.models.list().data)
```

For tokens that expire, pass a credential provider instead of a static token. Its `get_token()` is called on every HTTP attempt, so a refreshed token takes effect without rebuilding the client; async clients also accept an async `get_token()`.

```python
client = Forward(credential=my_credential)
```

A static `pat` takes precedence over a provider, and an explicit `Authorization` header takes precedence over both.

## Versioning

This project follows [Semantic Versioning](https://semver.org). It is pre-1.0, so the public surface may still change between releases. Anything prefixed with an underscore is internal and may change at any time.

```python
import qca

print(qca.__version__)
```

## Resources

Runnable scenarios live in `examples/`, organized by mode, with one file per scenario and its run command at the top of the file. Bug reports and feature requests belong in [GitHub Issues](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/issues).

## License

Released under the [MIT License](LICENSE).
