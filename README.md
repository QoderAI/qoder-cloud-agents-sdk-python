# Qoder Cloud Agents Python SDK

Synchronous and natively asynchronous clients for Python 3.10+, with typed responses, automatic pagination, SSE streaming, and file transfer.

## Installation and configuration

```bash
python -m pip install qca
```

The package is still in pre-release, so the command above resolves to the latest `0.0.1.devN` build. To work from a checkout of this repository instead:

```bash
python -m pip install .
# Development environment
python -m pip install -e '.[dev]'
```

```python
from qca import Forward, Managed

with Forward() as client:
    for model in client.models.list().data:
        if model.is_enabled:
            print(model.id)

with Managed() as client:
    for agent in client.agents.list(limit=20):
        print(agent.id, agent.name)
```

`from qca.forward import Client` and `from qca.managed import Client` are equivalent entry points. The two modes are instantiated independently and use their own resources and types.

| Setting | Forward | Managed |
|---|---|---|
| Token | `QODER_ACCESS_TOKEN` | `QODER_ACCESS_TOKEN` |
| API base URL | `QODER_FORWARD_BASE_URL` | `QODER_BASE_URL` |
| Default base URL | `https://api.qoder.com/api/v1/forward/` | `https://api.qoder.com/api/v1/cloud/` |

Explicit arguments take precedence over environment variables. The clients never read `.env`; only the examples load `.env.live`. The China endpoints have to be configured explicitly:

```python
client = Forward(
    access_token="your-access-token",
    base_url="https://api.qoder.com.cn/api/v1/forward",
    timeout=30.0,
    max_retries=2,
)
```

## Sessions

Forward creates a Session from an Identity and a Template; Managed creates one from an Agent and an Environment:

```python
from qca import Forward

with Forward() as client:
    environment = client.environments.create(name="demo", config={"type": "cloud"})
    identity = client.identities.create(external_id="example-user", name="Example User")
    template = client.templates.create(
        name="assistant", environment_id=environment.id,
        model="ultimate",  # use a model enabled for the current account
        system="Answer questions from the material you can read.",
        tools=[{"type": "agent_toolset_20260401"}],
    )
    session = client.sessions.create(identity_id=identity.id, template_id=template.id)
    print(session.id)
```

```python
from qca import Managed

with Managed() as client:
    environment = client.environments.create(name="demo", config={"type": "cloud"})
    agent = client.agents.create(
        name="assistant", model={"id": "ultimate"},
        system="Answer questions from the material you can read.",
        tools=[{"type": "agent_toolset_20260401"}],
    )
    session = client.sessions.create(environment_id=environment.id, agent=agent.id)
    print(session.id)
```

These snippets create real resources. For complete scenarios with execution assertions and cleanup, see [examples](examples/README.md). Forward additionally offers Schedule, Batch, and Channel; Managed offers Deployment, Dream, and the Work API for self-hosted environments.

## Messages and SSE

The code below works with either client. Reuse `session_id` throughout a conversation, and reuse one idempotency key across HTTP retries of the same logical message.

```python
from uuid import uuid4

sent = client.sessions.events.send(
    session_id,
    events=[{"type": "user.message", "content": [{"type": "text", "text": "Hello"}]}],
    extra_headers={"Idempotency-Key": uuid4().hex},
)

with client.sessions.events.stream(
    session_id,
    extra_headers={"Last-Event-ID": sent.data[0].id},
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

The SDK does not reconnect a stream on its own. Persist `stream.last_event_id` and resume through the `Last-Event-ID` header rather than resending messages the server already accepted. `event_start` and `event_delta` are previews: the final event carries the complete content again, and delta events sharing an ID are not deduplicated. An idle status can also mean the session is waiting for a confirmation or has reached its budget, so check `stop_reason` and the final reply before treating a run as successful.

## Async

The async clients are built on `httpx.AsyncClient`; requests, retry backoff, and SSE reads are all native async I/O.

```python
import asyncio
from qca import AsyncManaged

async def main():
    async with AsyncManaged() as client:
        async for agent in client.agents.list(limit=20):
            print(agent.id)
        first_page = await client.sessions.list(limit=10)
        print(first_page.data)

asyncio.run(main())
```

Async streams use `async with await client.sessions.events.stream(...)`. Complete snippets are in the [Forward async example](examples/forward/async_session.py) and the [Managed async example](examples/managed/async_session.py). Local files are read in a worker thread; network requests go directly through the async HTTP client.

## Parameters and responses

Methods use snake_case names, keyword arguments, and type annotations. The target ID of a nested resource may be positional, while ancestor IDs must be named:

```python
credential = client.vaults.credentials.retrieve("credential-id", vault_id="vault-id")
memory = client.memory_stores.memories.retrieve("memory-id", memory_store_id="store-id")
```

Requests are described by `TypedDict`s in each mode's `types/*_params.py`. Pass plain dicts for nested parameters, and pass the matching string, dict, or list for unions. Responses are Pydantic models: fields are accessed directly, and unknown fields are preserved.

```python
from qca import NOT_GIVEN

client.identities.update("identity-id", name=NOT_GIVEN)  # omits name from the request
client.identities.update("identity-id", name=None)       # sends null
client.identities.update("identity-id", enabled=False)   # keeps false

identity = client.identities.retrieve("identity-id")
print(identity.to_dict())
print(identity.to_json())
print(identity._request_id)
print("name" in identity.model_fields_set)  # tells a missing field from null
```

Whether a field can be cleared is decided by the server. Every method accepts `extra_headers`, `extra_query`, `extra_body`, and `timeout`; extra values take precedence over method arguments. Empty arrays, empty objects, `0`, and `false` are all preserved.

## Pagination

```python
page = client.sessions.list(limit=20)
print(page.data)                  # current page
for session in page:              # fetches subsequent pages automatically
    print(session.id)
for page in client.sessions.list().iter_pages():
    print(len(page.data))
```

Following the API, the SDK distinguishes `after_id` / `before_id` cursors from `next_page` pagination and carries filters into subsequent requests. It raises if a cursor stops advancing or starts looping. Non-paginated list responses, such as Models, are read through `.data`.

## Errors, timeouts, and retries

```python
from qca import APIConnectionError, APIStatusError, APITimeoutError

try:
    session = client.sessions.retrieve("sess-id", timeout=10)
except APITimeoutError:
    print("The request timed out")
except APIConnectionError:
    print("The connection failed")
except APIStatusError as exc:
    print(exc.status_code, exc.code, exc.type, exc.request_id)
```

HTTP statuses map to `BadRequestError`, `AuthenticationError`, `PermissionDeniedError`, `NotFoundError`, `ConflictError`, `UnprocessableEntityError`, `RateLimitError`, and `InternalServerError`. Non-JSON error bodies are kept in `.body`. When a response cannot be decoded into its declared type, `APIResponseValidationError` is raised.

The default connect timeout is 10 seconds, and 60 seconds for the remaining HTTP phases. You can pass a float of seconds, an `httpx.Timeout`, or `None`; timeouts are measured per HTTP phase and per attempt. End-to-end deadlines are the caller's responsibility — async code can use `asyncio.wait_for`.

Up to 2 retries by default: GET/HEAD requests and requests carrying an `Idempotency-Key` are retried on connection errors, 408, 429, and 5xx; other requests without an idempotency key are retried on 429 only; 409 is never retried automatically. Within those constraints the SDK honors `x-should-retry` and a valid `Retry-After-Ms` / `Retry-After`, and otherwise backs off exponentially. An SSE stream that has already been established is not retried.

`client.with_options(max_retries=0, timeout=20)` returns a separately configured client that shares the same HTTP connection pool; closing either client closes that pool.

## Files and custom HTTP

```python
from pathlib import Path

file = client.files.upload(file=Path("report.txt"))
skill = client.skills.create(files=[("example/SKILL.md", b"---\nname: example\n---\nExample skill")])
with client.files.download(file.id) as content:
    content.write_to_file("downloaded.txt")
```

Uploads accept bytes, binary file objects, `Path`, and `(filename, content[, MIME type])`. File objects you provide stay yours to close; upload content is buffered so it can be replayed on retry. Metadata is JSON-encoded, and Skill relative paths are preserved in the multipart filename.

A file download first obtains a temporary link and then streams from the storage endpoint; API credentials, default headers, and cookies are not sent to the storage host. A Skill version download returns the API's binary response directly. Async downloads use `await client.files.download(...)` and `await response.write_to_file(...)`.

```python
import httpx
from qca import Forward

with Forward(http_client=httpx.Client(proxy="http://localhost:8080")) as client:
    raw = client.models.with_raw_response.list()
    print(raw.status_code, raw.headers)
    models = raw.parse()
```

Async clients accept an `httpx.AsyncClient`, and async raw responses are parsed with `await raw.parse()`. A dynamic token provider is passed as `credential=` and its `get_token()` is called on every HTTP attempt; async clients also accept an async `get_token()`. A static `access_token` takes precedence over a provider, and an explicit `Authorization` header takes precedence over both.

Use `with_streaming_response` when the response headers have to be inspected before the body is read. The connection is closed when the context exits:

```python
with client.models.with_streaming_response.list() as response:
    print(response.headers)
    models = response.parse()
```

The async form is `async with client.models.with_streaming_response.list()`, with the body parsed through `await response.parse()`; the payload can also be iterated in chunks with `iter_bytes()` / `iter_lines()`.

## Project layout

```text
src/qca/
  __init__.py
  common/                 # HTTP, auth, errors, pagination, upload/download, SSE
  forward/
    _client.py
    resources/            # identities/configs, sessions/events, and so on
    types/                # request TypedDicts, response models
  managed/
    _client.py
    resources/            # agents, deployments, environments/work, and so on
    types/
tests/                    # resource surface, common layer, simulated execution
examples/                 # one file per scenario; each mode ships 6 sync scenarios, async snippets, and live tests
```

## License

Released under the [MIT License](LICENSE).
