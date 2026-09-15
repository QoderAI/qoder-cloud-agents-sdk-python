from __future__ import annotations

import asyncio
import io
import json
import platform
from datetime import datetime, timezone
from email.parser import BytesParser
from email.policy import default

import httpx
import pytest

from qca import (
    NOT_GIVEN,
    APIConnectionError,
    APIResponseValidationError,
    APIStatusError,
    APITimeoutError,
    AsyncForward,
    AsyncManaged,
    AuthenticationError,
    BadRequestError,
    ConflictError,
    Forward,
    InternalServerError,
    Managed,
    NotFoundError,
    PermissionDeniedError,
    RateLimitError,
    UnprocessableEntityError,
    __version__,
)


def make_client(handler, cls=Forward, **kwargs):
    return cls(
        pat="test-token",
        base_url="https://api.test/prefix/",
        http_client=httpx.Client(transport=httpx.MockTransport(handler)),
        **kwargs,
    )


@pytest.mark.parametrize(
    "cls,env,suffix", [(Forward, "QODER_FORWARD_BASE_URL", "forward"), (Managed, "QODER_MANAGED_BASE_URL", "cloud")]
)
def test_environment_defaults_and_explicit_precedence(monkeypatch, cls, env, suffix):
    monkeypatch.setenv("QODER_PAT", "from-env")
    monkeypatch.setenv(env, f"https://configured.test/api/v1/{suffix}")
    with cls() as client:
        assert client.pat == "from-env"
        assert str(client.base_url) == f"https://configured.test/api/v1/{suffix}/"
    with cls(pat="explicit", base_url="https://explicit.test/root") as client:
        assert client.pat == "explicit"
        assert str(client.base_url) == "https://explicit.test/root/"


def test_omission_null_false_zero_and_request_overrides():
    requests = []
    with make_client(
        lambda request: requests.append(request) or httpx.Response(200, json={}), default_headers={"X-Test": "default"}
    ) as client:
        client.identities.update(
            "identity",
            name=None,
            enabled=False,
            metadata={},
            extra_body={"count": 0},
            extra_headers={"x-test": "override"},
            timeout=7,
        )
        client.identities.update("identity", name=NOT_GIVEN)
    assert json.loads(requests[0].content) == {"name": None, "enabled": False, "metadata": {}, "count": 0}
    assert requests[0].headers["x-test"] == "override"
    assert requests[0].extensions["timeout"]["read"] == 7
    assert json.loads(requests[1].content) == {}


def test_path_segments_are_escaped_and_empty_ids_rejected():
    requests = []
    with make_client(lambda request: requests.append(request) or httpx.Response(200, json={})) as client:
        client.sessions.retrieve("a/b ?#中文")
        with pytest.raises(ValueError):
            client.sessions.retrieve("")
        with pytest.raises(ValueError):
            client.sessions.retrieve("..")
    assert requests[0].url.raw_path == b"/prefix/sessions/a%2Fb%20%3F%23%E4%B8%AD%E6%96%87"


def test_query_arrays_and_special_headers():
    requests = []
    with make_client(lambda request: requests.append(request) or httpx.Response(200, json={"data": []})) as client:
        client.sessions.events.list(
            "sess", types=["agent.message", "session.status_idle"], include_thinking=False, extra_query={"limit": 0}
        )
        client.sessions.events.send("sess", events=[], idempotency_key="send-key")
    assert requests[0].url.params.get_list("types[]") == ["agent.message", "session.status_idle"]
    assert requests[0].url.params["include_thinking"] == "false"
    assert requests[0].url.params["limit"] == "0"
    assert requests[1].headers["idempotency-key"] == "send-key"
    assert json.loads(requests[1].content) == {"events": []}


def test_client_fingerprint_reports_language_version_platform_and_deadline():
    requests = []
    with make_client(lambda request: requests.append(request) or httpx.Response(200, json={"data": []})) as client:
        client.models.list()
        client.models.list(timeout=7)
    headers = requests[0].headers
    assert headers["user-agent"] == f"qca-python/{__version__}"
    assert headers["x-qoder-lang"] == "python"
    assert headers["x-qoder-package-version"] == __version__
    assert headers["x-qoder-runtime"] == platform.python_implementation()
    assert headers["x-qoder-runtime-version"] == platform.python_version()
    # Normalized rather than platform.system()/machine() raw, so that the same
    # machine lands in the same server-side bucket as the Go and TS SDKs.
    assert headers["x-qoder-os"] in {"MacOS", "Windows", "Linux", "iOS", "Android", "FreeBSD", "OpenBSD"}
    assert headers["x-qoder-arch"] in {"x32", "x64", "arm", "arm64"}
    assert headers["x-qoder-retry-count"] == "0"
    assert headers["x-qoder-timeout"] == "60"
    assert requests[1].headers["x-qoder-timeout"] == "7"


def test_client_fingerprint_yields_to_caller_and_omits_absent_deadline():
    requests = []

    def handle(request):
        requests.append(request)
        return httpx.Response(200, json={"data": []})

    with make_client(handle, default_headers={"X-Qoder-Lang": "cli", "X-Qoder-Timeout": "5"}) as client:
        client.models.list(extra_headers={"User-Agent": "caller/1.0"})
    with make_client(handle) as client:
        client.models.list(timeout=None)
    assert requests[0].headers["x-qoder-lang"] == "cli"
    assert requests[0].headers["x-qoder-timeout"] == "5"
    assert requests[0].headers["user-agent"] == "caller/1.0"
    assert "x-qoder-timeout" not in requests[1].headers


def test_datetime_and_nested_query_serialization():
    requests = []
    with make_client(lambda request: requests.append(request) or httpx.Response(200, json={"data": []})) as client:
        client.sessions.list(
            created_at_gt=datetime(2026, 1, 2, 3, 4, 5, tzinfo=timezone.utc),
            updated_at_lte=datetime(2026, 3, 4),
            extra_query={"filter": {"status": "idle", "tags": ["a", "b"]}},
        )
    params = requests[0].url.params
    assert params["created_at[gt]"] == "2026-01-02T03:04:05+00:00"
    assert params["updated_at[lte]"] == "2026-03-04T00:00:00"
    assert params["filter[status]"] == "idle"
    assert params.get_list("filter[tags]") == ["a", "b"]


def test_managed_nested_identifiers_and_header_parameters():
    requests = []
    with make_client(lambda request: requests.append(request) or httpx.Response(200, json={}), cls=Managed) as client:
        client.environments.work.heartbeat(
            "work",
            environment_id="env",
            desired_ttl_seconds=0,
            expected_last_heartbeat=12,
            betas=["feature-a", "feature-b"],
        )
        client.vaults.credentials.retrieve("cred", vault_id="vault", workspace_id="workspace")
        client.environments.work.poll("env", worker_id="worker")
    assert requests[0].url.path == "/prefix/environments/env/work/work/heartbeat"
    assert requests[0].url.params["desired_ttl_seconds"] == "0"
    assert requests[0].headers["x-qoder-beta"] == "feature-a,feature-b"
    assert requests[1].headers["qoder-workspace-id"] == "workspace"
    assert requests[2].headers["Worker-ID"] == "worker"


@pytest.mark.parametrize(
    "status,expected",
    [
        (400, BadRequestError),
        (401, AuthenticationError),
        (403, PermissionDeniedError),
        (404, NotFoundError),
        (409, ConflictError),
        (422, UnprocessableEntityError),
        (429, RateLimitError),
        (500, InternalServerError),
        (503, InternalServerError),
        (418, APIStatusError),
    ],
)
def test_status_codes_map_to_typed_exceptions(monkeypatch, status, expected):
    monkeypatch.setattr("qca.common._base_client.time.sleep", lambda _: None)
    body = {"error": {"type": "invalid_request_error", "code": "bad_field", "message": "rejected"}}
    with make_client(
        lambda _: httpx.Response(status, json=body, headers={"x-request-id": "req-1"}), max_retries=0
    ) as client:
        with pytest.raises(expected) as caught:
            client.identities.retrieve("identity")
    assert type(caught.value) is expected
    assert (caught.value.status_code, caught.value.request_id) == (status, "req-1")
    assert (caught.value.type, caught.value.code, caught.value.body) == ("invalid_request_error", "bad_field", body)


@pytest.mark.parametrize(
    "verb,status,key,count",
    [
        ("GET", 408, False, 3),
        ("GET", 409, False, 1),
        ("GET", 429, False, 3),
        ("GET", 500, False, 3),
        ("POST", 500, False, 1),
        ("POST", 429, False, 3),
        ("POST", 500, True, 3),
        ("POST", 409, True, 1),
    ],
)
def test_retry_policy_by_verb_and_status(monkeypatch, verb, status, key, count):
    monkeypatch.setattr("qca.common._base_client.time.sleep", lambda _: None)
    calls = []
    with make_client(
        lambda request: calls.append(request) or httpx.Response(status, json={"error": {"message": "retry"}})
    ) as client:
        with pytest.raises(APIStatusError):
            if verb == "GET":
                client.models.list()
            else:
                client.identities.create(external_id="test", idempotency_key="key" if key else NOT_GIVEN)
    assert len(calls) == count


def test_retry_after_and_server_retry_directive(monkeypatch):
    sleeps = []
    monkeypatch.setattr("qca.common._base_client.time.sleep", sleeps.append)
    calls = []

    def handle(request):
        calls.append(request)
        return httpx.Response(429 if len(calls) == 1 else 200, headers={"retry-after-ms": "125"}, json={"data": []})

    with make_client(handle) as client:
        client.models.list()
    assert sleeps == [0.125]
    calls.clear()
    with make_client(
        lambda request: calls.append(request) or httpx.Response(500, headers={"x-should-retry": "false"}, json={})
    ) as client:
        with pytest.raises(APIStatusError):
            client.models.list()
    assert len(calls) == 1


def test_retry_count_header_reports_the_attempt_number(monkeypatch):
    monkeypatch.setattr("qca.common._base_client.time.sleep", lambda _: None)
    counts = []

    # Read inside the handler: the request object is reused across attempts, so
    # inspecting it afterwards would only show the last value.
    def handle(request):
        counts.append(request.headers["x-qoder-retry-count"])
        return httpx.Response(500, json={})

    with make_client(handle) as client:
        with pytest.raises(APIStatusError):
            client.models.list()
    assert counts == ["0", "1", "2"]


def test_connection_timeout_and_non_json_error(monkeypatch):
    monkeypatch.setattr("qca.common._base_client.time.sleep", lambda _: None)
    for exc_type, expected in [(httpx.ConnectError, APIConnectionError), (httpx.ReadTimeout, APITimeoutError)]:

        def handle(request):
            raise exc_type("failed", request=request)

        with make_client(handle, max_retries=0) as client, pytest.raises(expected):
            client.models.list()
    with make_client(lambda _: httpx.Response(502, text="gateway unavailable"), max_retries=0) as client:
        with pytest.raises(APIStatusError) as caught:
            client.models.list()
    assert caught.value.body == "gateway unavailable"


def test_dynamic_credentials_refresh_and_explicit_headers(monkeypatch):
    monkeypatch.delenv("QODER_PAT", raising=False)
    monkeypatch.setattr("qca.common._base_client.time.sleep", lambda _: None)

    class Rotating:
        count = 0

        def get_token(self):
            self.count += 1
            return f"token-{self.count}"

    credential = Rotating()
    headers = []

    def handle(request):
        headers.append(request.headers["authorization"])
        return httpx.Response(500 if len(headers) == 1 else 200, json={"data": []})

    with Forward(credential=credential, http_client=httpx.Client(transport=httpx.MockTransport(handle))) as client:
        client.models.list()
        client.models.list(extra_headers={"Authorization": "Bearer explicit"})
    assert headers == ["Bearer token-1", "Bearer token-2", "Bearer explicit"]


def test_response_models_unknown_fields_presence_and_raw_response():
    with make_client(
        lambda _: httpx.Response(
            200, json={"id": "one", "name": None, "future": {"value": 1}}, headers={"x-request-id": "req"}
        )
    ) as client:
        identity = client.identities.retrieve("one")
        assert identity.future == {"value": 1}
        assert "name" in identity.model_fields_set
        assert "external_id" not in identity.model_fields_set
        assert identity._request_id == "req"
        assert identity.to_dict() == {"id": "one", "name": None, "future": {"value": 1}}
        raw = client.identities.with_raw_response.retrieve("one")
        assert raw.status_code == 200
        assert raw.headers["x-request-id"] == "req"
        assert raw.parse().id == "one"
        assert client.identities.retrieve("one").id == "one"
    with make_client(lambda _: httpx.Response(200, text="not JSON")) as client:
        with pytest.raises(APIResponseValidationError):
            client.models.list()


def test_with_options_is_independent_and_preserves_custom_transport():
    headers = []
    with make_client(
        lambda request: headers.append(request.headers["x-test"]) or httpx.Response(200, json={"data": []}),
        default_headers={"x-test": "original"},
    ) as client:
        view = client.with_options(default_headers={"x-test": "changed"}, max_retries=0)
        view.models.list()
        client.models.list()
        assert view.max_retries == 0 and client.max_retries == 2
    assert headers == ["changed", "original"]


def test_multipart_metadata_filenames_and_retry_replay(monkeypatch, tmp_path):
    monkeypatch.setattr("qca.common._base_client.time.sleep", lambda _: None)
    requests = []

    def handle(request):
        requests.append(request)
        return httpx.Response(429 if len(requests) == 1 else 200, json={})

    local = tmp_path / "asset.txt"
    local.write_bytes(b"asset")
    supplied = io.BytesIO(b"skill content")
    with make_client(handle) as client:
        client.skills.create(
            files=[("skill/SKILL.md", supplied, "text/markdown"), ("skill/asset.txt", local)],
            metadata={"source": "test"},
            idempotency_key="upload-key",
        )
    assert requests[0].content == requests[1].content
    assert not supplied.closed
    message = BytesParser(policy=default).parsebytes(
        b"Content-Type: " + requests[0].headers["content-type"].encode() + b"\r\n\r\n" + requests[0].content
    )
    parts = list(message.iter_parts())
    assert [p.get_filename() for p in parts[:2]] == ["skill/SKILL.md", "skill/asset.txt"]
    assert parts[0].get_payload(decode=True) == b"skill content"
    assert json.loads(parts[2].get_payload(decode=True)) == {"source": "test"}


def test_download_does_not_forward_api_headers_cookies_or_auth(tmp_path):
    requests = []

    def handle(request):
        requests.append(request)
        if request.url.host == "api.test":
            return httpx.Response(200, json={"url": "https://storage.test/asset?signed=true"})
        assert not any(
            k in request.headers
            for k in ("authorization", "cookie", "x-sensitive", "qoder-workspace-id", "x-qoder-lang")
        )
        return httpx.Response(200, content=b"content")

    http = httpx.Client(
        transport=httpx.MockTransport(handle), headers={"x-sensitive": "secret"}, cookies={"session": "cookie"}
    )
    with Managed(pat="api-token", base_url="https://api.test/cloud", http_client=http) as client:
        response = client.files.download("file", workspace_id="workspace")
        response.write_to_file(tmp_path / "download.txt")
        assert response.http_response.is_closed
    assert (tmp_path / "download.txt").read_bytes() == b"content"
    assert len(requests) == 2


@pytest.mark.parametrize(
    "url", ["file:///etc/passwd", "ftp://storage.test/file", "https://user:secret@storage.test/file"]
)
def test_invalid_download_url_is_rejected(url):
    with make_client(lambda _: httpx.Response(200, json={"url": url})) as client:
        with pytest.raises(APIResponseValidationError):
            client.files.download("file")


async def test_native_async_concurrency_cancellation_and_raw_response():
    started = asyncio.Event()
    both = asyncio.Event()
    count = 0

    async def handle(request):
        nonlocal count
        if request.url.path.endswith("/cancel"):
            started.set()
            await asyncio.Event().wait()
        count += 1
        if count == 2:
            both.set()
        await asyncio.wait_for(both.wait(), timeout=1)
        return httpx.Response(200, json={"id": "identity", "data": []})

    async with AsyncForward(http_client=httpx.AsyncClient(transport=httpx.MockTransport(handle))) as client:
        first, second = await asyncio.gather(client.identities.retrieve("first"), client.identities.retrieve("second"))
        assert first.id == second.id == "identity"
        raw = await client.identities.with_raw_response.retrieve("third")
        assert (await raw.parse()).id == "identity"
        task = asyncio.create_task(client.identities.retrieve("cancel"))
        await started.wait()
        task.cancel()
        with pytest.raises(asyncio.CancelledError):
            await task


async def test_async_upload_and_download(tmp_path):
    async def handle(request):
        if request.method == "POST":
            assert b'filename="file.txt"' in request.content
            return httpx.Response(200, json={"id": "file"})
        if request.url.host == "storage.test":
            assert "authorization" not in request.headers
            return httpx.Response(200, content=b"async data")
        return httpx.Response(200, json={"url": "https://storage.test/asset"})

    async with AsyncManaged(
        pat="secret", http_client=httpx.AsyncClient(transport=httpx.MockTransport(handle))
    ) as client:
        item = await client.files.upload(file=("file.txt", b"hello"))
        result = await client.files.download(item.id)
        await result.write_to_file(tmp_path / "async.txt")
    assert (tmp_path / "async.txt").read_bytes() == b"async data"


def test_streaming_response_defers_body_read_and_closes():
    class Body(httpx.SyncByteStream):
        read = False
        closed = False

        def __iter__(self):
            self.read = True
            yield b'{"data":[]}'

        def close(self):
            self.closed = True

    body = Body()
    with make_client(lambda _: httpx.Response(200, stream=body, headers={"x-test": "header"})) as client:
        with client.models.with_streaming_response.list() as response:
            assert response.headers["x-test"] == "header"
            assert not body.read
            assert response.parse().data == []
            assert body.read
    assert body.closed


async def test_async_streaming_response_defers_body_read_and_closes():
    class Body(httpx.AsyncByteStream):
        read = False
        closed = False

        async def __aiter__(self):
            self.read = True
            yield b'{"data":[]}'

        async def aclose(self):
            self.closed = True

    body = Body()
    async with AsyncForward(
        http_client=httpx.AsyncClient(transport=httpx.MockTransport(lambda _: httpx.Response(200, stream=body)))
    ) as client:
        async with client.models.with_streaming_response.list() as response:
            assert not body.read
            assert (await response.parse()).data == []
    assert body.closed


def test_response_body_timeout_uses_sdk_exception_and_closes():
    class Body(httpx.SyncByteStream):
        closed = False

        def __iter__(self):
            raise httpx.ReadTimeout("body timed out")
            yield b""

        def close(self):
            self.closed = True

    body = Body()
    with make_client(lambda _: httpx.Response(200, stream=body)) as client:
        with pytest.raises(APITimeoutError):
            client.models.list()
    assert body.closed


@pytest.mark.parametrize("cls", [AsyncForward, AsyncManaged])
@pytest.mark.parametrize(
    "verb,status,key,count",
    [
        ("GET", 500, False, 3),
        ("GET", 429, False, 3),
        ("GET", 409, False, 1),
        ("POST", 500, False, 1),
        ("POST", 429, False, 3),
        ("POST", 500, True, 3),
    ],
)
async def test_async_retry_policy_through_public_resources(monkeypatch, cls, verb, status, key, count):
    calls, sleeps = [], []

    async def pause(delay):
        sleeps.append(delay)

    monkeypatch.setattr("qca.common._base_client.anyio.sleep", pause)

    def handle(request):
        calls.append(request)
        return httpx.Response(status, json={"error": {"message": "retry"}}, headers={"retry-after-ms": "25"})

    async with cls(pat="test", http_client=httpx.AsyncClient(transport=httpx.MockTransport(handle))) as client:
        with pytest.raises(APIStatusError):
            if verb == "GET":
                await client.models.list()
            else:
                await client.sessions.events.send(
                    "session", events=[], extra_headers={"Idempotency-Key": "key"} if key else {}
                )
    assert len(calls) == count
    assert sleeps == [0.025] * (count - 1)
    assert len({request.content for request in calls}) == 1


async def test_async_retry_count_header_reports_the_attempt_number(monkeypatch):
    async def pause(delay):
        return None

    monkeypatch.setattr("qca.common._base_client.anyio.sleep", pause)
    counts = []

    def handle(request):
        counts.append(request.headers["x-qoder-retry-count"])
        return httpx.Response(500, json={})

    transport = httpx.MockTransport(handle)
    async with AsyncForward(pat="test", http_client=httpx.AsyncClient(transport=transport)) as client:
        with pytest.raises(APIStatusError):
            await client.models.list()
    assert counts == ["0", "1", "2"]
