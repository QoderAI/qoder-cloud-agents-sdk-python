"""Offline contracts from cached Forward/CAS handlers and official API docs.

Forward: session/create.go:968, handler/session/handler.go:128,
templatea2a/config.go:15-122, handler/a2a/handler_test.go:288-315.
CAS: agent/helpers.go:59-327, agent/service.go:598,621-648,
mcp/rules.go:232-279 and mcp/validate.go:129-166. OSS read/write shapes:
official-docs/api/forward/environments/schemas.txt:101-116.
MCP mocks verify serialization and snapshots, not actual tool execution.
"""

from __future__ import annotations

import inspect
import json
from contextlib import asynccontextmanager
from typing import get_type_hints

import httpx
import pytest
from pydantic import TypeAdapter, ValidationError

from qca import APIResponseValidationError, AsyncForward, AsyncManaged, BadRequestError, Forward, Managed, __version__
from qca.common._types import NOT_GIVEN
from qca.forward import types as ft
from qca.managed import types as mt

SEGMENT = "id /?%# +"
ESCAPED = "id%20%2F%3F%25%23%20%2B"
SKILL = {"id": "summary", "name": "Summarize", "description": "Summarize text", "tags": [], "examples": []}
PUBLICATION = {"enabled": True, "description": "Public summary", "skills": [SKILL]}
ROSTER = {
    "type": "coordinator",
    "agents": [
        "tmpl_child",
        {"type": "agent", "template_id": "tmpl_second"},
        {"type": "agent", "id": "agent_child"},
        {"type": "self"},
        {"type": "advisor", "model": "ultimate"},
    ],
}
MEDIA = [
    ("ImageGen", "image_gen", mt.ImageGenToolConfigParams, mt.ImageGenToolConfig),
    ("ImageSearch", "image_search", mt.ImageSearchToolConfigParams, mt.ImageSearchToolConfig),
    ("VideoGen", "video_gen", mt.VideoGenToolConfigParams, mt.VideoGenToolConfig),
    ("DeliverArtifacts", "deliver_artifacts", mt.DeliverArtifactsToolConfigParams, mt.DeliverArtifactsToolConfig),
]
POLICY_PARAMS = [
    mt.BashToolConfigParams,
    mt.EditToolConfigParams,
    mt.ReadToolConfigParams,
    mt.WriteToolConfigParams,
    mt.GlobToolConfigParams,
    mt.GrepToolConfigParams,
    mt.WebFetchToolConfigParams,
    mt.WebSearchToolConfigParams,
    mt.AgentToolsetDefaultConfigParams,
    mt.MCPToolsetDefaultConfigParams,
    mt.MCPToolConfigParams,
]


@pytest.fixture(params=[False, True], ids=["sync", "async"])
def async_(request):
    return request.param


async def resolve(value):
    return await value if inspect.isawaitable(value) else value


@asynccontextmanager
async def client_for(async_, surface, handle, *, sat=False, strict=True):
    def transport(request):
        assert request.url.host == "api.test"
        assert request.headers["authorization"] == "Bearer " + ("test-sat" if sat else "test-pat")
        return handle(request)

    http = (httpx.AsyncClient if async_ else httpx.Client)(transport=httpx.MockTransport(transport))
    cls = {
        (False, "forward"): Forward,
        (True, "forward"): AsyncForward,
        (False, "managed"): Managed,
        (True, "managed"): AsyncManaged,
    }[async_, surface]
    auth = {"auth_mode": "sa", "access_token": "test-sat"} if sat else {"pat": "test-pat"}
    client = cls(
        **auth,
        http_client=http,
        base_url="https://api.test/api/v1/" + surface,
        _strict_response_validation=strict,
        max_retries=0,
    )
    try:
        yield client
    finally:
        await resolve(client.close())
        await resolve(http.aclose() if async_ else http.close())


def reply(payload, status=200):
    return httpx.Response(status, json=payload, headers={"x-request-id": "req-parity"})


def adapter(cls, namespace):
    value = TypeAdapter(cls)
    value.rebuild(force=True, _types_namespace=vars(namespace))
    return value


def card_payload(version):
    payload = {
        "name": "Summary",
        "description": "Public summary",
        "version": "2026.11",
        "skills": [SKILL],
        "defaultInputModes": ["text/plain", "application/json"],
        "defaultOutputModes": ["text/plain"],
        "capabilities": {"streaming": True},
        "futureField": {"kept": True},
    }
    if version == "0.3":
        payload["url"] = "https://do-not-follow.test/a2a?identity_id=identity"
        payload["additionalInterfaces"] = [{"url": payload["url"], "transport": "JSONRPC"}]
    else:
        payload["supportedInterfaces"] = [
            {
                "url": "https://do-not-follow.test/a2a",
                "protocolBinding": "JSONRPC",
                "protocolVersion": "1.0",
                "futureInterfaceField": 7,
            }
        ]
    return payload


@pytest.mark.parametrize("auto_title,title", [(NOT_GIVEN, NOT_GIVEN), (False, "Manual"), (True, NOT_GIVEN)])
async def test_session_auto_title_creation(async_, auto_title, title):
    def handle(req):
        assert req.method == "POST" and req.url.path == "/api/v1/forward/sessions"
        body = json.loads(req.content)
        expected = {"identity_id": "idn_one", "template_id": "tmpl_one", "config": {"model": "auto"}}
        if auto_title is not NOT_GIVEN:
            expected["auto_title"] = auto_title
        if title is not NOT_GIVEN:
            expected["title"] = title
        metadata = body.pop("metadata")
        assert metadata == {
            "__qca_sdk_created": "true",
            "__qca_sdk_language": "python",
            "__qca_sdk_version": __version__,
        }
        assert body == expected
        return reply({"id": "sess_one", "type": "session", "config": expected["config"]})

    async with client_for(async_, "forward", handle) as client:
        session = await resolve(
            client.sessions.create(
                identity_id="idn_one",
                template_id="tmpl_one",
                auto_title=auto_title,
                title=title,
                config={"model": "auto"},
            )
        )
        assert session.config.model == "auto"
        assert "auto_title" not in ft.Session.model_fields
        assert "auto_title" not in inspect.signature(client.sessions.update).parameters


@pytest.mark.parametrize("title", [None, "", "Manual"])
async def test_auto_title_conflicts_are_left_to_service(async_, title):
    calls = []

    def handle(req):
        calls.append(req)
        body = json.loads(req.content)
        assert body["auto_title"] is True and body["title"] == title
        return reply({"error": {"type": "invalid_request", "message": "title must not be supplied"}}, 400)

    async with client_for(async_, "forward", handle) as client:
        with pytest.raises(BadRequestError):
            await resolve(
                client.sessions.create(
                    identity_id="idn_one",
                    template_id="tmpl_one",
                    auto_title=True,
                    title=title,
                )
            )
    assert len(calls) == 1


@pytest.mark.parametrize(
    "config",
    [
        NOT_GIVEN,
        {},
        {"multiagent": None},
        {"multiagent": ROSTER},
    ],
)
async def test_session_roster_update(async_, config):
    expected = {} if config is NOT_GIVEN else {"config": config}

    def handle(req):
        assert req.method == "POST"
        assert req.url.raw_path == f"/api/v1/forward/sessions/{ESCAPED}".encode()
        assert json.loads(req.content) == expected
        return reply({"id": "sess_one", **expected})

    async with client_for(async_, "forward", handle) as client:
        session = await resolve(client.sessions.update(SEGMENT, config=config))
        assert session.to_dict() == {"id": "sess_one", **expected}
        if config is not NOT_GIVEN and config.get("multiagent") is not None:
            assert isinstance(session.config.multiagent, ft.MultiagentConfig)
            assert session.config.multiagent.to_dict()["agents"] == config["multiagent"]["agents"]
            assert session.config.multiagent.agents[2].id == "agent_child"


async def test_session_empty_roster_is_rejected(async_):
    config = {"multiagent": {"type": "coordinator", "agents": []}}

    def handle(req):
        assert json.loads(req.content) == {"config": config}
        return reply(
            {"error": {"type": "invalid_request", "message": "multiagent.agents must be a non-empty array"}}, 400
        )

    async with client_for(async_, "forward", handle) as client:
        with pytest.raises(BadRequestError):
            await resolve(client.sessions.update(SEGMENT, config=config))


@pytest.mark.parametrize("method", ["create", "update"])
@pytest.mark.parametrize("publication", [NOT_GIVEN, None, {}, PUBLICATION, {"skills": []}, {"enabled": False}])
async def test_template_a2a_patch(async_, method, publication):
    expected = {"name": "summary", "model": "auto", "environment_id": "env_one"} if method == "create" else {}
    if publication is not NOT_GIVEN:
        expected["a2a"] = publication

    def handle(req):
        assert req.method == "POST"
        suffix = "/templates" + ("/" + ESCAPED if method == "update" else "")
        assert req.url.raw_path == ("/api/v1/forward" + suffix).encode()
        assert json.loads(req.content) == expected
        return reply({"id": "tmpl_one", **expected})

    async with client_for(async_, "forward", handle) as client:
        kwargs = {"a2a": publication}
        if method == "create":
            template = await resolve(client.templates.create(**expected, **({} if "a2a" in expected else kwargs)))
        else:
            template = await resolve(client.templates.update(SEGMENT, **kwargs))
        assert template.to_dict() == {"id": "tmpl_one", **expected}
        if isinstance(publication, dict):
            assert isinstance(template.a2a, ft.A2AConfig)
            if publication.get("skills"):
                assert isinstance(template.a2a.skills[0], ft.A2ASkill)
                assert template.a2a.skills[0].tags == []


@pytest.mark.parametrize("version", [NOT_GIVEN, "0.3", "1.0"])
@pytest.mark.parametrize("sat", [False, True], ids=["PAT", "SAT"])
async def test_agent_card_protocol_and_options(async_, version, sat):
    calls = []
    payload = card_payload("0.3" if version is NOT_GIVEN else version)

    def handle(req):
        calls.append(req)
        assert req.method == "GET" and req.content == b""
        assert req.url.raw_path.split(b"?")[0] == f"/api/v1/forward/templates/{ESCAPED}/a2a/agent-card.json".encode()
        assert req.url.params["custom"] == "a +/=&"
        if sat:
            assert "identity_id" not in req.url.params
        else:
            assert req.url.params["identity_id"] == SEGMENT
            assert "%23" in str(req.url) and "%2B" in str(req.url)
        if version is NOT_GIVEN:
            assert "a2a-version" not in req.headers
        else:
            assert req.headers["a2a-version"] == version
        assert "a2a_version" not in req.url.params and "A2A-Version" not in req.url.params
        assert req.headers["x-test"] == "forwarded"
        assert req.extensions["timeout"]["read"] == 12.5
        return reply(payload)

    async with client_for(async_, "forward", handle, sat=sat) as client:
        raw = await resolve(
            client.templates.with_raw_response.retrieve_agent_card(
                SEGMENT,
                identity_id=NOT_GIVEN if sat else SEGMENT,
                a2a_version=version,
                extra_headers={"X-Test": "forwarded"},
                extra_query={"custom": "a +/=&"},
                timeout=12.5,
            )
        )
        card = await resolve(raw.parse())
        assert isinstance(card, ft.AgentCard)
        assert card._request_id == "req-parity"
        assert (card.name, card.description, card.version) == ("Summary", "Public summary", "2026.11")
        assert card.default_input_modes == ["text/plain", "application/json"]
        assert card.default_output_modes == ["text/plain"]
        assert card.skills[0].id == "summary"
        assert card.futureField == {"kept": True}
        if version == "1.0":
            interface = card.supported_interfaces[0]
            assert isinstance(interface, ft.AgentCardInterface)
            assert interface.protocol_binding == "JSONRPC" and interface.protocol_version == "1.0"
            assert interface.futureInterfaceField == 7
            assert card.url is None
        else:
            assert card.url.startswith("https://do-not-follow.test/")
            assert card.supported_interfaces is None
        assert card.to_dict() == payload
    assert len(calls) == 1  # Never follow invocation URLs.


@pytest.mark.parametrize("version", ["0.3", "1.0"])
async def test_agent_card_extra_options_override(async_, version):
    def handle(req):
        assert req.headers["a2a-version"] == version
        assert req.url.params["identity_id"] == SEGMENT
        return reply(card_payload(version))

    async with client_for(async_, "forward", handle) as client:
        card = await resolve(
            client.templates.retrieve_agent_card(
                "tmpl_one",
                a2a_version="0.3",
                identity_id="original",
                extra_headers={"A2A-Version": version},
                extra_query={"identity_id": SEGMENT},
                extra_body={},
            )
        )
        assert card.version == "2026.11"


@pytest.mark.parametrize("method", ["create", "update"])
@pytest.mark.parametrize("credential", ["ram_role", "access_key", "omitted", "empty_buckets"])
async def test_forward_oss_request_and_safe_response(async_, method, credential):
    bucket = {
        "name": "datasets",
        "provider": "aliyun-oss",
        "region": "cn-hangzhou",
        "bucket": "test-bucket",
        "prefix": "team/data/",
        "access": "read_write",
        "accelerator_endpoint": "test.oss-data-acc.aliyuncs.com",
    }
    if credential == "ram_role":
        bucket["credential"] = {"type": "ram_role", "role_arn": "test-role-arn"}
    elif credential == "access_key":
        bucket["credential"] = {
            "type": "access_key",
            "access_key_id": "test-key-id",
            "access_key_secret": "test-key-secret",
        }
    buckets = [] if credential == "empty_buckets" else [bucket]
    config = {"type": "cloud", "packages": {"apt": []}, "startup_script": "true", "storage": {"buckets": buckets}}
    expected = {"config": config, **({"name": "datasets"} if method == "create" else {})}
    safe_bucket = {**bucket, "credential": {"type": "access_key", "access_key_id": "test****id"}}
    if credential == "ram_role":
        safe_bucket["credential"] = {"type": "ram_role"}
    safe = {
        "id": "env_one",
        "config": {
            **config,
            "storage": {
                "buckets": [] if credential == "empty_buckets" else [safe_bucket],
            },
        },
    }

    def handle(req):
        assert req.method == "POST"
        assert req.url.params["identity_id"] == SEGMENT
        assert req.headers["x-qoder-beta"] == "oss-bucket-2026-09-23"
        assert json.loads(req.content) == expected
        if method == "create" and credential == "omitted":
            return reply({"error": {"type": "invalid_request", "message": "credential required"}}, 400)
        return reply(safe)

    async with client_for(async_, "forward", handle) as client:
        kwargs = {**expected, "identity_id": SEGMENT, "extra_headers": {"X-Qoder-Beta": "oss-bucket-2026-09-23"}}
        if method == "create" and credential == "omitted":
            with pytest.raises(BadRequestError):
                await resolve(client.environments.create(**kwargs))
            return
        env = await resolve(
            client.environments.create(**kwargs)
            if method == "create"
            else client.environments.update(SEGMENT, **kwargs)
        )
        assert isinstance(env.config, ft.EnvironmentConfig)
        assert isinstance(env.config.storage, ft.BucketStorage)
        assert env.to_dict() == safe
        if credential != "empty_buckets":
            result = env.config.storage.buckets[0].credential
            assert isinstance(result, ft.OSSBucketCredential)
            assert not hasattr(result, "role_arn") and not hasattr(result, "access_key_secret")
            assert "test-key-secret" not in env.to_json() and "test-role-arn" not in env.to_json()
            assert result.access_key_id is None if credential == "ram_role" else result.access_key_id == "test****id"
    assert "role_arn" not in ft.OSSBucketCredential.model_fields
    assert "access_key_secret" not in ft.OSSBucketCredential.model_fields


@pytest.mark.parametrize(
    "config",
    [
        NOT_GIVEN,
        {"type": "self_hosted", "startup_script": "true"},
        {"type": "cloud", "storage": {"buckets": []}},
        {"type": "cloud", "future_config": {"keep": True}},
    ],
)
async def test_environment_config_omission_and_dict_compatibility(async_, config):
    expected = {} if config is NOT_GIVEN else {"config": config}

    def handle(req):
        assert json.loads(req.content) == expected
        assert "x-qoder-beta" not in req.headers
        return reply({"id": "env_one", **expected})

    async with client_for(async_, "forward", handle) as client:
        env = await resolve(client.environments.update("env_one", config=config))
        assert env.to_dict() == {"id": "env_one", **expected}


def managed_tools(aliases=False):
    return [
        {
            "type": "agent_toolset_20260401",
            "default_config": {"permission_policy": {"type": "always_deny"}},
            "configs": [
                {"name": alias if aliases else name, "permission_policy": {"type": "always_deny"}}
                for name, alias, _, _ in MEDIA
            ]
            + [{"name": "bash", "enabled": False, "permission_policy": {"type": "always_deny"}}],
        },
        {
            "type": "mcp_toolset",
            "mcp_server_name": "weather",
            "permission_policy": {"type": "always_deny"},
            "configs": [{"name": "forecast", "enabled": False, "permission_policy": {"type": "always_deny"}}],
        },
        {"type": "browser_toolset_20260714"},
    ]


@pytest.mark.parametrize("method", ["create", "update"])
@pytest.mark.parametrize("aliases", [False, True])
async def test_managed_media_browser_and_deny_roundtrip(async_, method, aliases):
    tools = managed_tools(aliases)
    response_tools = managed_tools(False)
    response_tools[-1]["futureBrowserField"] = {"keep": True}
    expected = {"tools": tools, **({"model": "auto", "name": "media"} if method == "create" else {})}

    def handle(req):
        assert req.method == "POST"
        assert json.loads(req.content) == expected
        assert req.headers["x-qoder-beta"] == "browser-use-2026-07-14"
        assert "version" not in json.loads(req.content)
        return reply({"id": "agent_one", "version": 2, "tools": response_tools})

    async with client_for(async_, "managed", handle) as client:
        kwargs = {**expected, "betas": ["browser-use-2026-07-14"]}
        agent = await resolve(
            client.agents.create(**kwargs) if method == "create" else client.agents.update(SEGMENT, **kwargs)
        )
        assert agent.version == 2
        for config, (name, _, _, response_type) in zip(agent.tools[0].configs, MEDIA):
            assert isinstance(config, response_type)
            assert config.name == name and config.permission_policy.type == "always_deny"
        assert agent.tools[0].configs[-1].name == "bash"  # Existing name is unchanged by SDK.
        assert agent.tools[0].default_config.permission_policy.type == "always_deny"
        assert agent.tools[1].configs[0].permission_policy.type == "always_deny"
        assert agent.tools[1].permission_policy.type == "always_deny"
        assert isinstance(agent.tools[2], mt.BrowserToolset20260714)
        assert agent.tools[2].futureBrowserField == {"keep": True}
        assert agent.to_dict()["tools"] == response_tools


@pytest.mark.parametrize("method", ["create", "update"])
async def test_managed_session_snapshot_tools(async_, method):
    tools = managed_tools()
    tools[-1]["futureBrowserField"] = True
    snapshot = {"id": "agent_one", "type": "agent", "version": 3, "tools": tools}

    def handle(req):
        body = json.loads(req.content)
        if method == "create":
            assert body["agent"]["type"] == "agent_with_overrides"
            assert body["agent"]["tools"] == managed_tools()
        else:
            assert body == {"agent": {"tools": managed_tools()}}
        assert req.headers["x-qoder-beta"] == "browser-use-2026-07-14"
        return reply({"id": "sess_one", "type": "session", "agent": snapshot})

    async with client_for(async_, "managed", handle) as client:
        if method == "create":
            session = await resolve(
                client.sessions.create(
                    agent={"type": "agent_with_overrides", "id": "agent_one", "tools": managed_tools()},
                    environment_id="env_one",
                    betas=["browser-use-2026-07-14"],
                )
            )
        else:
            session = await resolve(
                client.sessions.update(
                    "sess_one",
                    agent={"tools": managed_tools()},
                    betas=["browser-use-2026-07-14"],
                )
            )
        assert session.agent.version == 3
        assert isinstance(session.agent.tools[2], mt.BrowserToolset20260714)
        assert session.agent.tools[2].futureBrowserField is True
        assert isinstance(session.agent.tools[0].configs[0], mt.ImageGenToolConfig)
        assert session.agent.tools[1].permission_policy.type == "always_deny"
        assert session.to_dict()["agent"] == snapshot


@pytest.mark.parametrize("model", [mt.SessionThreadAgentUnion, mt.SessionMultiagentCoordinatorAgentUnion])
def test_other_managed_agent_snapshots(model):
    payload = {"id": "agent_one", "version": 5, "tools": managed_tools()}
    snapshot = model.model_validate(payload)
    assert snapshot.version == 5
    assert isinstance(snapshot.tools[2], mt.BrowserToolset20260714)
    assert isinstance(snapshot.tools[0].configs[3], mt.DeliverArtifactsToolConfig)
    assert snapshot.tools[1].permission_policy.type == "always_deny"
    assert snapshot.to_dict() == payload


@pytest.mark.parametrize("params", POLICY_PARAMS, ids=lambda cls: cls.__name__)
def test_all_existing_policy_request_unions(params):
    payload = {"permission_policy": {"type": "always_deny"}}
    if params is mt.MCPToolConfigParams:
        payload["name"] = "forecast"
    assert adapter(params, mt).validate_python(payload) == payload


@pytest.mark.parametrize("name,alias,params,response", MEDIA)
def test_new_media_required_names_and_sparse_response(name, alias, params, response):
    request_type = adapter(params, mt)
    assert request_type.validate_python({"name": name}) == {"name": name}
    assert request_type.validate_python({"name": alias}) == {"name": alias}
    for payload in [{}, {"name": "wrong"}, {"name": None}]:
        with pytest.raises(ValidationError):
            request_type.validate_python(payload)
        with pytest.raises(ValidationError):
            response.model_validate(payload)
    parsed = response.model_validate({"name": name, "unknown": "preserved"})
    assert parsed.enabled is None and parsed.permission_policy is None
    assert parsed.unknown == "preserved"
    assert set(response.model_fields) == {"name", "enabled", "permission_policy"}
    assert set(get_type_hints(params, vars(mt), vars(mt))) == {"name", "enabled", "permission_policy"}
    toolset = {"type": "agent_toolset_20260401", "configs": [{"name": name}]}
    assert adapter(mt.AgentToolset20260401Params, mt).validate_python(toolset) == toolset


def test_public_request_boundaries():
    assert "multiagent" not in get_type_hints(ft.SessionCreateParamsConfigParam, vars(ft))
    assert "auto_title" not in get_type_hints(ft.SessionUpdateParams, vars(ft), vars(ft))
    assert adapter(ft.SessionUpdateParamsConfigParam, ft).validate_python({"multiagent": None}) == {"multiagent": None}
    assert set(get_type_hints(mt.BrowserToolset20260714Params, vars(mt))) == {"type"}
    with pytest.raises(ValidationError):
        adapter(mt.BrowserToolset20260714Params, mt).validate_python({})
    assert mt.AlwaysDenyPolicy.model_validate({"type": "always_deny"}).type == "always_deny"
    assert adapter(mt.AlwaysDenyPolicyParam, mt).validate_python({"type": "always_deny"}) == {"type": "always_deny"}
    for cls in [mt.AgentCreateParams, mt.AgentUpdateParams, mt.AgentWithOverridesParams, mt.SessionAgentUpdateParam]:
        args = {"tools": [{"type": "browser_toolset_20260714"}]}
        if cls is mt.AgentCreateParams:
            args.update(name="browser", model="auto")
        elif cls is mt.AgentWithOverridesParams:
            args.update(id="agent_one", type="agent_with_overrides")
        assert adapter(cls, mt).validate_python(args) == args


@pytest.mark.parametrize("member", ["enabled", "description", "skills"])
def test_a2a_members_cannot_be_null(member):
    with pytest.raises(ValidationError):
        adapter(ft.A2AConfigParam, ft).validate_python({member: None})
    for cls in [ft.TemplateCreateParams, ft.TemplateUpdateParams]:
        args = {"a2a": None}
        if cls is ft.TemplateCreateParams:
            args.update(name="summary", model="auto", environment_id="env_one")
        assert adapter(cls, ft).validate_python(args) == args
    assert adapter(ft.A2AConfigParam, ft).validate_python({}) == {}
    assert adapter(ft.A2AConfigParam, ft).validate_python({"skills": []}) == {"skills": []}
    for key in ["id", "name", "description", "tags", "examples"]:
        with pytest.raises(ValidationError):
            adapter(ft.A2ASkillParam, ft).validate_python({**SKILL, key: None})


def test_forward_environment_public_types():
    config = {
        "type": "cloud",
        "storage": {
            "buckets": [
                {
                    "name": "data",
                    "provider": "aliyun-oss",
                    "region": "cn-hangzhou",
                    "bucket": "test-bucket",
                }
            ]
        },
    }
    assert adapter(ft.EnvironmentConfigParam, ft).validate_python(config) == config
    assert adapter(ft.EnvironmentCreateParams, ft).validate_python({"name": "data", "config": config}) == {
        "name": "data",
        "config": config,
    }
    assert adapter(ft.EnvironmentUpdateParams, ft).validate_python({"config": config}) == {"config": config}
    for cls, credential in [
        (ft.OSSRAMRoleCredentialParam, {"type": "ram_role", "role_arn": "test-role"}),
        (
            ft.OSSAccessKeyCredentialParam,
            {"type": "access_key", "access_key_id": "test-id", "access_key_secret": "test-secret"},
        ),
    ]:
        assert adapter(cls, ft).validate_python(credential) == credential


@pytest.mark.parametrize(
    "surface,entry,payload",
    [
        ("forward", "card", {**card_payload("1.0"), "defaultInputModes": 1}),
        ("forward", "card", {**card_payload("0.3"), "skills": [{"id": "summary"}]}),
        ("forward", "card", {**card_payload("1.0"), "supportedInterfaces": [{"url": 17}]}),
        ("forward", "environment", {"config": {"type": "cloud", "storage": {"buckets": [{"name": "data"}]}}}),
        (
            "forward",
            "environment",
            {
                "config": {
                    "storage": {
                        "buckets": [
                            {
                                "name": "data",
                                "provider": "aliyun-oss",
                                "region": "cn-hangzhou",
                                "bucket": "test-bucket",
                                "credential": {"type": "access_key", "access_key_id": []},
                            }
                        ]
                    }
                }
            },
        ),
        ("forward", "template", {"a2a": {"skills": [{"id": "summary", "name": "Summarize"}]}}),
        ("forward", "session", {"config": {"multiagent": {"agents": 1}}}),
        (
            "managed",
            "agent",
            {
                "tools": [
                    {
                        "type": "agent_toolset_20260401",
                        "configs": [
                            {
                                "name": "ImageGen",
                                "permission_policy": {"type": []},
                            }
                        ],
                    }
                ]
            },
        ),
    ],
)
async def test_strict_http_response_failures(async_, surface, entry, payload):
    async with client_for(async_, surface, lambda req: reply(payload)) as client:
        with pytest.raises(APIResponseValidationError):
            if entry == "card":
                await resolve(client.templates.retrieve_agent_card("tmpl_one"))
            else:
                resource = {
                    "environment": "environments",
                    "template": "templates",
                    "session": "sessions",
                    "agent": "agents",
                }[entry]
                await resolve(getattr(client, resource).retrieve("id_one"))


async def test_browser_snapshot_migration_branches_before_reading_configs(async_):
    payload = {
        "id": "agent_one",
        "tools": [
            {"type": "browser_toolset_20260714"},
            {"type": "agent_toolset_20260401", "configs": [{"name": "Bash"}]},
        ],
    }
    async with client_for(async_, "managed", lambda req: reply(payload)) as client:
        agent = await resolve(client.agents.retrieve("agent_one"))
        names = []
        for tool in agent.tools or []:
            if isinstance(tool, mt.BrowserToolset20260714):
                continue
            for config in tool.configs or []:
                names.append(config.name)
        assert names == ["Bash"]


async def test_managed_lenient_unknown_tool_compatibility(async_):
    payload = {
        "id": "agent_one",
        "tools": [{"type": "future_toolset", "future": True}, {"type": "browser_toolset_20260714", "future": True}],
    }
    async with client_for(async_, "managed", lambda req: reply(payload), strict=False) as client:
        agent = await resolve(client.agents.retrieve("agent_one"))
        assert type(agent.tools[0]) is mt.AgentToolUnion
        assert agent.tools[0].future is True
        assert isinstance(agent.tools[1], mt.BrowserToolset20260714)
        assert agent.tools[1].future is True
        assert agent.to_dict() == payload


@pytest.mark.parametrize(
    "entry,tool_model",
    [("agent", mt.AgentToolUnion), ("session", mt.SessionAgentToolUnion), ("thread", mt.SessionThreadAgentToolUnion)],
)
@pytest.mark.parametrize("strict", [False, True], ids=["lenient", "strict"])
async def test_managed_historical_policy_snapshots(async_, entry, tool_model, strict):
    tools = [
        {
            "type": "agent_toolset_20260401",
            "configs": [{"name": "Bash", "permission_policy": "always_ask"}]
            + [{"name": name, "permission_policy": {"type": "always_deny"}} for name, _, _, _ in MEDIA],
        },
        {
            "type": "future_toolset",
            "configs": [{"name": "FutureTool", "permission_policy": "future_policy"}],
            "future": {"keep": True},
        },
        {"type": "browser_toolset_20260714", "futureBrowserField": True},
    ]
    snapshot = {"id": "agent_one", "type": "agent", "tools": tools}
    payload = snapshot if entry == "agent" else {"id": "snapshot_one", "agent": snapshot}
    paths = {
        "agent": "/agents/agent_one",
        "session": "/sessions/sess_one",
        "thread": "/sessions/sess_one/threads/thread_one",
    }

    def handle(req):
        assert req.method == "GET" and req.url.path == "/api/v1/managed" + paths[entry]
        return reply(payload)

    async with client_for(async_, "managed", handle, strict=strict) as client:
        resource, resource_id, kwargs = {
            "agent": (client.agents, "agent_one", {}),
            "session": (client.sessions, "sess_one", {}),
            "thread": (client.sessions.threads, "thread_one", {"session_id": "sess_one"}),
        }[entry]
        if strict:
            with pytest.raises(APIResponseValidationError) as caught:
                await resolve(resource.retrieve(resource_id, **kwargs))
            assert caught.value.body == payload
            return
        result = await resolve(resource.retrieve(resource_id, **kwargs))
        agent = result if entry == "agent" else result.agent
        toolset = agent.tools[0]
        assert type(toolset) is tool_model
        assert not isinstance(toolset, mt.BrowserToolset20260714)
        assert type(toolset.configs[0]) is mt.AgentToolConfigUnion
        assert not isinstance(toolset.configs[0], dict)
        assert toolset.configs[0].name == "Bash"
        assert toolset.configs[0].permission_policy == "always_ask"
        for config, (_, _, _, model) in zip(toolset.configs[1:], MEDIA):
            assert isinstance(config, model)
            assert config.permission_policy.type == "always_deny"
        assert type(agent.tools[1]) is tool_model
        assert type(agent.tools[1].configs[0]) is mt.AgentToolConfigUnion
        assert agent.tools[1].configs[0].name == "FutureTool"
        assert agent.tools[1].configs[0].permission_policy == "future_policy"
        assert agent.tools[1].future == {"keep": True}
        assert isinstance(agent.tools[2], mt.BrowserToolset20260714)
        assert agent.tools[2].futureBrowserField is True
        assert result.to_dict() == payload


@pytest.mark.parametrize("method", ["create", "update"])
@pytest.mark.parametrize("legacy_default", [False, True])
async def test_mcp_top_level_deny_without_configs_roundtrip(async_, method, legacy_default):
    tool = {"type": "mcp_toolset", "mcp_server_name": "weather", "permission_policy": {"type": "always_deny"}}
    if legacy_default:
        tool["default_config"] = {"permission_policy": {"type": "always_allow"}}
    tools = [tool]
    expected = {"tools": tools, **({"name": "weather", "model": "auto"} if method == "create" else {})}

    def handle(req):
        assert req.method == "POST"
        assert req.url.path == "/api/v1/managed/agents" + ("/agent_one" if method == "update" else "")
        assert json.loads(req.content) == expected
        assert "configs" not in json.loads(req.content)["tools"][0]
        return reply({"id": "agent_one", "tools": tools})

    async with client_for(async_, "managed", handle) as client:
        agent = await resolve(
            client.agents.create(**expected) if method == "create" else client.agents.update("agent_one", **expected)
        )
        toolset = agent.tools[0]
        assert "permission_policy" in mt.AgentToolUnion.model_fields
        assert isinstance(toolset.permission_policy, mt.AgentToolConfigUnionPermissionPolicy)
        assert toolset.permission_policy.type == "always_deny"
        assert toolset.configs is None
        if legacy_default:
            assert toolset.default_config.permission_policy.type == "always_allow"
        else:
            assert toolset.default_config is None
        assert agent.to_dict()["tools"] == tools


@pytest.mark.parametrize("policy", ["always_allow", "always_ask", "always_deny"])
def test_mcp_top_level_policy_request_and_response_types(policy):
    tool = {"type": "mcp_toolset", "mcp_server_name": "weather", "permission_policy": {"type": policy}}
    assert adapter(mt.MCPToolsetParams, mt).validate_python(tool) == tool
    for cls in [mt.AgentCreateParams, mt.AgentUpdateParams, mt.AgentWithOverridesParams, mt.SessionAgentUpdateParam]:
        payload = {"tools": [tool]}
        if cls is mt.AgentCreateParams:
            payload.update(name="weather", model="auto")
        elif cls is mt.AgentWithOverridesParams:
            payload.update(id="agent_one", type="agent_with_overrides")
        assert adapter(cls, mt).validate_python(payload) == payload
    for model in [mt.AgentToolUnion, mt.SessionAgentToolUnion, mt.SessionThreadAgentToolUnion]:
        assert "permission_policy" in model.model_fields
        snapshot = model.model_validate(tool)
        assert isinstance(snapshot.permission_policy, mt.AgentToolConfigUnionPermissionPolicy)
        assert snapshot.permission_policy.type == policy
        assert snapshot.to_dict() == tool
    with pytest.raises(ValidationError):
        adapter(mt.MCPToolsetParams, mt).validate_python({**tool, "permission_policy": {"type": "deny"}})
