"""Official docs.qoder.com model/Outcome contracts retrieved 2026-10-27."""

import inspect
import json

import httpx
import pytest

from qca import AsyncForward, AsyncManaged, Forward, Managed


async def resolve(value):
    return await value if inspect.isawaitable(value) else value


@pytest.mark.parametrize("async_", [False, True])
@pytest.mark.parametrize(
    "model", ["omitted", None, "", "auto", {"id": "auto", "effort": "none", "context_window": 400000}]
)
async def test_dream_model_default_and_tuning(async_, model):
    body = {"inputs": [{"type": "memory_store", "memory_store_id": "memstore_test"}]}
    if model != "omitted":
        body["model"] = model

    def handle(req):
        assert req.url.path.endswith("/dreams")
        assert json.loads(req.content) == body
        return httpx.Response(
            200, json={"id": "dream_test", "model": model if isinstance(model, dict) else {"id": "auto"}}
        )

    http = (httpx.AsyncClient if async_ else httpx.Client)(transport=httpx.MockTransport(handle))
    client = (AsyncManaged if async_ else Managed)(pat="test", http_client=http, _strict_response_validation=True)
    try:
        dream = await resolve(client.dreams.create(**body))
        if isinstance(model, dict):
            assert dream.model.effort == "none"
            assert dream.model.context_window == 400000
        else:
            assert dream.model.id == "auto"
    finally:
        await resolve(client.close())


@pytest.mark.parametrize("async_", [False, True])
@pytest.mark.parametrize(
    "rubric", [{"type": "text", "content": "report exists"}, {"type": "file", "file_id": "file_test"}]
)
async def test_forward_outcome_rubric_roundtrip(async_, rubric):
    event = {"id": "evt_test", "type": "user.define_outcome", "rubric": rubric}

    def handle(req):
        if req.method == "POST":
            assert json.loads(req.content)["events"][0]["rubric"] == rubric
        return httpx.Response(200, json={"data": [event], "has_more": False})

    http = (httpx.AsyncClient if async_ else httpx.Client)(transport=httpx.MockTransport(handle))
    client = (AsyncForward if async_ else Forward)(pat="test", http_client=http, _strict_response_validation=True)
    try:
        await resolve(
            client.sessions.events.send(
                "sess_test", events=[{"type": "user.define_outcome", "description": "write report", "rubric": rubric}]
            )
        )
        page = await resolve(client.sessions.events.list("sess_test"))
        assert page.data[0].rubric.to_dict() == rubric
    finally:
        await resolve(client.close())


@pytest.fixture
async def mock_sdk():
    clients = []

    def create(mode, async_, handler, strict=True):
        cls = {
            ("forward", False): Forward,
            ("forward", True): AsyncForward,
            ("managed", False): Managed,
            ("managed", True): AsyncManaged,
        }[mode, async_]
        http = (httpx.AsyncClient if async_ else httpx.Client)(transport=httpx.MockTransport(handler))
        client = cls(pat="test", http_client=http, _strict_response_validation=strict, max_retries=0)
        clients.append(client)
        return client

    yield create
    for client in clients:
        await resolve(client.close())


@pytest.mark.parametrize("async_", [False, True])
async def test_identity_config_and_schedule_fields(mock_sdk, async_):
    responses = {
        "/identities/idn": {"id": "idn", "auto_memory_store": False},
        "/identities/idn/templates/tmpl/config": {},
        "/identities/idn/templates/tmpl/memory_stores": {"memory_store_id": "mem", "access": "read_write"},
        "/schedules/sched": {"resources": [{"type": "file", "file_id": "file_test", "mount_path": "/data/test.txt"}]},
        "/schedule_runs/run": {
            "initial_events": [{"type": "user.message", "content": [{"type": "text", "text": "input"}]}]
        },
    }
    expected = []

    def handle(req):
        path, body = expected.pop(0)
        assert req.url.path.endswith(path)
        if body is None:
            assert req.url.params["include_initial_events"] == "true"
            assert not req.content
        else:
            assert json.loads(req.content) == body
        return httpx.Response(200, json=responses[path])

    client = mock_sdk("forward", async_, handle)
    expected.append(("/identities/idn", {"auto_memory_store": False}))
    identity = await resolve(client.identities.update("idn", auto_memory_store=False))
    assert identity.auto_memory_store is False
    for spec in [
        {"tools": [], "managed_tool_config": {"schedule": {"enabled": False}, "drive": None}},
        {"tools": {"Bash": {"enabled": False}}},
        {"tools": None, "managed_tool_config": None, "system": None, "model": None},
    ]:
        expected.append(("/identities/idn/templates/tmpl/config", {"identity_config": spec}))
        responses["/identities/idn/templates/tmpl/config"] = {"identity_config": spec}
        result = await resolve(client.identities.configs.upsert("tmpl", identity_id="idn", identity_config=spec))
        assert result.identity_config.to_dict() == spec
    expected.append(
        ("/identities/idn/templates/tmpl/memory_stores", {"memory_store_id": "mem", "access": "read_write"})
    )
    mount = await resolve(
        client.identities.memory_stores.mount("tmpl", identity_id="idn", memory_store_id="mem", access="read_write")
    )
    assert mount.access == "read_write"
    resources = responses["/schedules/sched"]["resources"]
    expected.append(("/schedules/sched", {"resources": resources}))
    schedule = await resolve(client.schedules.update("sched", resources=resources))
    assert schedule.resources[0].file_id == "file_test"
    expected.append(("/schedule_runs/run", None))
    run = await resolve(client.schedule_runs.retrieve("run", include_initial_events=True))
    assert run.initial_events[0].type == "user.message"
    assert not expected


@pytest.mark.parametrize("async_", [False, True])
@pytest.mark.parametrize("direction", ["after_id", "before_id"])
async def test_mount_pagination_retains_scope(mock_sdk, async_, direction):
    calls = []

    def handle(req):
        assert req.url.path.endswith("/identities/idn/templates/tmpl/memory_stores")
        assert req.url.params["limit"] == "1"
        cursor = "start" if not calls else "mem_one"
        assert req.url.params[direction] == cursor
        assert ("before_id" if direction == "after_id" else "after_id") not in req.url.params
        calls.append(req)
        id_ = "mem_one" if len(calls) == 1 else "mem_two"
        return httpx.Response(
            200,
            json={
                "data": [{"memory_store_id": id_, "access": "read_write"}],
                "first_id": id_,
                "last_id": id_,
                "has_more": len(calls) == 1,
            },
        )

    client = mock_sdk("forward", async_, handle)
    page = client.identities.memory_stores.list("tmpl", identity_id="idn", limit=1, **{direction: "start"})
    ids = [item.memory_store_id async for item in page] if async_ else [item.memory_store_id for item in page]
    assert ids == ["mem_one", "mem_two"]
    assert len(calls) == 2


@pytest.mark.parametrize("async_", [False, True])
async def test_forward_dream_and_pairing_lifecycle(mock_sdk, async_):
    from pathlib import Path

    fixtures = json.loads((Path(__file__).parent / "fixtures/official-contract-responses.json").read_text())
    expected = []

    def handle(req):
        method, path, body, result = expected.pop(0)
        assert req.method == method and req.url.path.endswith(path)
        if body is None:
            assert not req.content
        else:
            assert json.loads(req.content) == body
        return httpx.Response(200, json=result)

    client = mock_sdk("forward", async_, handle)
    dream = fixtures["dream"]
    inputs = [
        {"type": "identity_template", "identity_id": "idn", "template_id": "tmpl"},
        {"type": "sessions", "session_ids": ["sess"]},
    ]
    for model in ["omitted", None, "", "auto", {"id": "auto", "effort": "none", "context_window": 400000}]:
        body = {"inputs": inputs}
        if model != "omitted":
            body["model"] = model
        expected.append(("POST", "/dreams", body, dream))
        result = await resolve(client.dreams.create(**body))
        assert result.model.effort == "none" and result.outputs[0].files_touched == ["MEMORY.md"]
        assert result.usage.input_tokens == 5 and result.error is None
    for method in ["retrieve", "cancel", "archive"]:
        expected.append(
            (
                "GET" if method == "retrieve" else "POST",
                "/dreams/drm" + ("" if method == "retrieve" else "/" + method),
                None,
                dream,
            )
        )
        assert (await resolve(getattr(client.dreams, method)("drm"))).id == "drm_contract"
    pending = {**fixtures["pairing"], "status": "pairing", "identity_id": "", "template_id": "", "paired_at": ""}
    expected.append(("GET", "/channel_pairings/pair", None, pending))
    result = await resolve(client.channel_pairings.retrieve("pair"))
    assert result.paired_at == "" and result.identity_id == "" and result.status == "pairing"
    expected.append(("POST", "/channel_pairings/pair", {"template_id": "tmpl_new"}, fixtures["pairing"]))
    await resolve(client.channel_pairings.update("pair", template_id="tmpl_new"))
    assert not expected


@pytest.mark.parametrize("async_", [False, True])
async def test_oauth_and_managed_memory_cursor(mock_sdk, async_):
    from pathlib import Path

    fixture = json.loads((Path(__file__).parent / "fixtures/official-contract-responses.json").read_text())["oauth"]
    body = {
        "vault_id": "vault",
        "mcp_server_url": "https://mcp.example.com",
        "client_id": "client",
        "client_secret": "test-secret",
    }
    calls = []

    def handle(req):
        calls.append(req)
        if req.url.path.endswith("/oauth/start"):
            assert req.method == "POST" and json.loads(req.content) == body
            assert not req.url.query and req.headers["qoder-workspace-id"] == "workspace"
            return httpx.Response(200, json=fixture)
        assert req.url.path.endswith("/memory_stores")
        assert req.url.params["before_id"] == "mem_before"
        assert req.url.params["include_archived"] == "false" and not req.content
        return httpx.Response(200, json={"data": [], "has_more": False})

    client = mock_sdk("managed", async_, handle)
    result = await resolve(client.oauth.start(**body, workspace_id="workspace"))
    assert result.to_dict() == fixture
    await resolve(client.memory_stores.list(before_id="mem_before", include_archived=False))
    assert len(calls) == 2


@pytest.mark.parametrize("async_", [False, True])
async def test_oss_storage_write_read_and_clear(mock_sdk, async_):
    bucket = {
        "name": "assets",
        "provider": "aliyun-oss",
        "region": "cn-hangzhou",
        "bucket": "example",
        "access": "read_only",
        "credential": {"type": "access_key", "access_key_id": "test-ak", "access_key_secret": "test-secret"},
    }
    read_bucket = {**bucket, "credential": {"type": "access_key", "access_key_id": "test****"}}
    expected = []

    def handle(req):
        body = expected.pop(0)
        assert req.method == "POST" and req.url.path.endswith("/environments/env")
        assert json.loads(req.content) == body
        assert req.headers.get("x-qoder-beta") == "oss-bucket-2026-09-23"
        assert not req.url.query
        return httpx.Response(200, json={"config": {"type": "cloud", "storage": {"buckets": [read_bucket]}}})

    client = mock_sdk("managed", async_, handle)
    for buckets in [[bucket], [{k: v for k, v in read_bucket.items() if k != "credential"}], []]:
        config = {"type": "cloud", "storage": {"buckets": buckets}}
        expected.append({"config": config})
        env = await resolve(client.environments.update("env", config=config, betas=["oss-bucket-2026-09-23"]))
        credential = env.config.storage.buckets[0].credential
        assert credential.to_dict() == {"type": "access_key", "access_key_id": "test****"}
        assert not hasattr(credential, "access_key_secret")
    assert not expected
