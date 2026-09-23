# Qoder Cloud Agents Python SDK

[Changelog](CHANGELOG.md) · [Releases](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/releases)

[![PyPI version](https://img.shields.io/pypi/v/qca-sdk.svg)](https://pypi.org/project/qca-sdk/)

The Qoder Cloud Agents Python SDK provides access to the Qoder Cloud Agents API from Python 3.10+. It ships synchronous and natively asynchronous clients, typed request parameters and response models, automatic pagination, SSE streaming, and file transfer.

The API is exposed in two modes, and each has its own client, resources, and types. Forward is multi-tenant: sessions are created from an Identity and a Template, and it adds Schedule, Batch, and Channel. Managed is single-tenant: sessions are created from an Agent and an Environment, and it adds Deployment, Dream, and the Work API for self-hosted environments.

## Installation

```bash
python -m pip install qca-sdk
```

The distribution is named `qca-sdk`; the import package is `qca`. The package is pre-1.0, so the command above resolves to the latest `0.1.x` release. To work from a checkout of this repository instead:

```bash
python -m pip install .
python -m pip install -e '.[dev]'   # development environment
```

## Requirements

Python 3.10 or newer. The runtime dependencies are `httpx`, `pydantic` v2, `anyio`, and `typing-extensions`; the package is typed and ships `py.typed`.

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
| Token | `QODER_PAT` | `QODER_PAT` |
| Base URL | `QODER_FORWARD_BASE_URL` | `QODER_MANAGED_BASE_URL` |
| Default base URL | `https://api.qoder.com/api/v1/forward/` | `https://api.qoder.com/api/v1/cloud/` |

Explicit arguments take precedence over environment variables. The clients never read `.env` files; only the examples load `.env.live`. Other regions, including China, have to be configured explicitly:

```python
client = Forward(
    pat="your-access-token",
    base_url="https://api.qoder.com.cn/api/v1/forward",
    timeout=30.0,
    max_retries=2,
)
```

A client owns an HTTP connection pool, so it should be closed when you are done with it — either through the context manager above or with `client.close()`.

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

`APIConnectionError` is raised when the request never reached the API; `APITimeoutError` is its timeout subclass. A non-2xx status raises an `APIStatusError` subclass, and a response that cannot be decoded into its declared type raises `APIResponseValidationError`. All of them derive from `qca.APIError`.

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
| 422 | `UnprocessableEntityError` |
| 429 | `RateLimitError` |
| 5xx | `InternalServerError` |
| other | `APIStatusError` |

`code` and `type` are read from the error body and are `None` when the server omits them, so log `message` and `request_id` as well. A non-JSON error body is kept verbatim in `.body`.

## Request IDs

Every response model carries the `x-request-id` of the call that produced it, and errors expose the same value. Include it when reporting a problem.

```python
identity = client.identities.retrieve("identity-id")
print(identity._request_id)
```

## Retries

Certain errors are retried twice by default with exponential backoff. GET and HEAD requests, and any request carrying an idempotency key, are retried on connection errors, 408, 429, and 5xx; other requests are retried on 429 only. A 409 is never retried automatically, and an SSE stream that has already been established is never retried. Within those rules the SDK honors `x-should-retry` and a valid `Retry-After-Ms` or `Retry-After`.

```python
client = Forward(max_retries=0)  # disable for all requests
client.with_options(max_retries=5).sessions.list()  # or override per call site
```

`with_options` returns a separately configured client that shares the original connection pool, so closing either one closes that pool.

## Timeouts

The default timeout is 10 seconds to connect and 60 seconds for each subsequent phase. Pass a float of seconds, an `httpx.Timeout`, or `None` to disable.

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

This project follows [Semantic Versioning](https://semver.org). It is pre-1.0 and currently published as `0.1.0`, so the public surface may still change between releases. Anything prefixed with an underscore is internal and may change at any time.

```python
import qca

print(qca.__version__)
```

## Resources

Runnable scenarios live in `examples/`, organized by mode, with one file per scenario and its run command at the top of the file. Bug reports and feature requests belong in [GitHub Issues](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/issues).

## License

Released under the [MIT License](LICENSE).
