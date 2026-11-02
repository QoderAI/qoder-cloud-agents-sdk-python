# Qoder Cloud Agents Python SDK

[Changelog](CHANGELOG.md) · [Releases](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/releases)

[![PyPI version](https://img.shields.io/pypi/v/qca-sdk.svg)](https://pypi.org/project/qca-sdk/)

The Qoder Cloud Agents Python SDK provides access to the Qoder Cloud Agents API from Python 3.10+. It ships synchronous and natively asynchronous clients, typed request parameters and response models, automatic pagination and SSE streaming.

The SDK provides separate Forward and Managed clients. Both modes share authentication, transport, retries, error handling and pagination.

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

## Streaming

Streaming responses are consumed incrementally. Close the stream when finished and handle interruption explicitly; closing a local stream does not cancel server-side work.

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

## Documentation and examples

- [API reference](docs/api/reference.md)
- [Runnable examples](examples/)
- [Contribution guide](CONTRIBUTING.md)

Bug reports and feature requests belong in [GitHub Issues](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/issues).

## License

Released under the [MIT License](LICENSE).
