from __future__ import annotations

import json
import sys
from email.parser import BytesParser
from email.policy import default

import httpx
import pytest

from examples.common.live import Config, ProjectMemory, Run, TurnResult, choose_model, read_env, run_cli, safe_error
from examples.forward import batch
from examples.forward.__main__ import SCENARIOS as FORWARD_SCENARIOS
from examples.managed.__main__ import SCENARIOS as MANAGED_SCENARIOS
from qca import Forward, Managed


class ExampleService:
    """A stateful HTTP stub: replies are derived from uploaded resources and memory."""

    def __init__(self, mode):
        self.mode = mode
        self.objects = {}
        self.contents = {}
        self.events = {}
        self.mounts = {}
        self.overrides = {}
        self.outputs = {}
        self.counter = 0
        self.deleted = []

    def create(self, kind, body):
        self.counter += 1
        item = {**body, "id": f"{kind}-{self.counter}"}
        self.objects[item["id"]] = item
        return item

    def session(self, body):
        session = self.create("session", {**body, "status": "idle"})
        self.events[session["id"]] = []
        for event in body.get("initial_events", []):
            self.send(session["id"], event)
        return session

    def send(self, session_id, event):
        session = self.objects[session_id]
        user_event = self.create("event", event)
        self.events[session_id].append(user_event)
        content = event.get("content", [])
        prompt = content if isinstance(content, str) else "".join(block.get("text", "") for block in content)
        text = prompt
        agent = self.objects[session.get("template_id") or session.get("agent")]
        if "SDK_EXAMPLE_VALUE" in prompt:
            resource = next(r for r in session["resources"] if r["type"] == "file")
            assert resource["mount_path"] == "/data/workspace/sdk-example.txt"
            text = self.contents[resource["file_id"]].decode()
            if self.mode == "forward":
                override = self.overrides[session["identity_id"], session["template_id"]]
                assert override["op"] == "set"
                text += " " + override["value"]
            else:
                text += " " + session["environment_variables"]["SDK_EXAMPLE_VALUE"]
        elif "EXAMPLE_SKILL_CODE" in prompt:
            skill = agent["skills"][0]
            text = self.contents[skill["skill_id"]].decode()
        elif "项目约定" in prompt:
            store_id = (
                self.mounts[session["identity_id"], session["template_id"]]
                if self.mode == "forward"
                else next(r["memory_store_id"] for r in session["resources"] if r["type"] == "memory_store")
            )
            text = "\n".join(item["content"] for item in self.objects.values() if item.get("store_id") == store_id)
            assert "MEMORY.md" in [
                item.get("path") for item in self.objects.values() if item.get("store_id") == store_id
            ]
        events = [
            {"type": "agent.tool_use", "name": "Read", "evaluated_permission": "allow"},
            {"type": "agent.message", "content": [{"type": "text", "text": text}]},
            {"type": "session.status_idle", "stop_reason": {"type": "end_turn"}},
        ]
        self.events[session_id].extend(self.create("event", item) for item in events)
        return user_event

    def __call__(self, request):
        path = request.url.path.split("/api/v1/", 1)[1].split("/", 1)[1]
        parts = path.split("/")
        verb = request.method
        body = {}
        if request.content:
            if request.headers.get("content-type", "").startswith("multipart/"):
                message = BytesParser(policy=default).parsebytes(
                    b"Content-Type: " + request.headers["content-type"].encode() + b"\r\n\r\n" + request.content
                )
                body = {
                    part.get_param("name", header="content-disposition"): part.get_payload(decode=True)
                    for part in message.iter_parts()
                }
            else:
                body = json.loads(request.content)

        def reply(data):
            if isinstance(data, dict) and isinstance(data.get("agent"), str):
                data = {**data, "agent": {"id": data["agent"]}}
            return httpx.Response(200, json=data)

        if path == "models":
            return reply({"data": [{"id": "ultimate", "is_enabled": True}]})
        if parts[0] == "sessions" and len(parts) >= 3:
            session_id = parts[1]
            if parts[2] == "events":
                if verb == "POST":
                    return reply({"data": [self.send(session_id, e) for e in body["events"]]})
                events = self.events[session_id]
                after = request.headers.get("Last-Event-ID") or request.url.params.get("after_id")
                if after:
                    events = events[next(i for i, e in enumerate(events) if e["id"] == after) + 1 :]
                if parts[-1] == "stream":
                    return httpx.Response(
                        200,
                        text="".join(f"id: {e['id']}\nevent: {e['type']}\ndata: {json.dumps(e)}\n\n" for e in events),
                        headers={"content-type": "text/event-stream"},
                    )
                return reply({"data": events, "has_more": False})
            if parts[2] == "resources":
                return reply({"data": self.objects[session_id]["resources"], "has_more": False})
        if parts[0] == "memory_stores" and len(parts) >= 3 and parts[2] == "memories":
            store_id = parts[1]
            if verb == "POST":
                return reply(self.create("memory", {**body, "store_id": store_id}))
            if len(parts) == 4:
                assert self.objects[parts[3]]["store_id"] == store_id
                return reply(self.objects[parts[3]])
            return reply(
                {
                    "data": [item for item in self.objects.values() if item.get("store_id") == store_id],
                    "has_more": False,
                }
            )
        if parts[0] == "identities" and len(parts) >= 5:
            identity, template = parts[1], parts[3]
            if parts[4] == "config":
                self.overrides[identity, template] = body["identity_config"]["environment_variables"][
                    "SDK_EXAMPLE_VALUE"
                ]
                return reply({})
            if parts[4] == "memory_stores":
                if verb == "POST":
                    self.mounts[identity, template] = body["memory_store_id"]
                    return reply({})
                if verb == "DELETE":
                    del self.mounts[identity, template]
                    return reply({})
                return reply({"data": [{"memory_store_id": self.mounts[identity, template]}]})
        if len(parts) == 1 and verb == "POST":
            kind = parts[0]
            if self.mode == "forward" and kind == "memory_stores":
                assert request.headers.get("Idempotency-Key"), "Idempotency-Key header is required"
            if kind in ("files", "skills"):
                item = self.create(kind, {"latest_version": "v1"} if kind == "skills" else {})
                self.contents[item["id"]] = body["file" if kind == "files" else "files"]
            elif kind in ("agents", "templates"):
                for skill in body.get("skills", []):
                    assert skill["version"] == self.objects[skill["skill_id"]]["latest_version"]
                item = self.create(kind, body)
            elif kind == "sessions":
                item = self.session(body)
            elif kind == "dreams":
                store_id = body["inputs"][0]["memory_store_id"]
                source = next(item["content"] for item in self.objects.values() if item.get("store_id") == store_id)
                output = self.create("memory_stores", {})
                self.create(
                    "memory", {"store_id": output["id"], "path": "sdk-example/consolidated.md", "content": source}
                )
                item = self.create(
                    "dream",
                    {"status": "completed", "outputs": [{"type": "memory_store", "memory_store_id": output["id"]}]},
                )
            elif kind == "batches":
                assert body["ignore_idle_window"] is True
                task = json.loads(self.contents[body["input_file_id"]])
                session = self.session(
                    {
                        "identity_id": task["identity_id"],
                        "template_id": task["template_id"],
                        "initial_events": [{"type": "user.message", "content": task["body"]["input"]}],
                    }
                )
                item = self.create(
                    "batch",
                    {
                        "status": "completed",
                        "output_file_id": "output",
                        "request_counts": {"total": 1, "completed": 1, "failed": 0},
                    },
                )
                self.outputs[item["id"]] = [
                    {
                        "custom_id": task["custom_id"],
                        "identity_id": task["identity_id"],
                        "template_id": task["template_id"],
                        "session_id": session["id"],
                        "status": "completed",
                        "response": task["body"]["input"],
                    }
                ]
            else:
                item = self.create(kind, body)
            return reply(item)
        if len(parts) == 3 and parts[-1] == "run":
            item = self.objects[parts[1]]
            session = self.session(item)
            execution = self.create("run", {"session_id": session["id"], "status": "completed"})
            return reply(execution)
        if len(parts) == 3 and parts[-1] == "tasks":
            return reply({"data": [{"custom_id": row["custom_id"]} for row in self.outputs[parts[1]]]})
        if len(parts) == 3 and parts[-1] == "clear":
            return reply({"status": "completed"})
        if verb == "DELETE" or (len(parts) == 3 and parts[-1] == "archive"):
            self.deleted.append(parts[1])
            return reply({})
        if len(parts) == 2 and verb == "GET":
            return reply(self.objects[parts[1]])
        raise AssertionError(f"Unexpected request: {verb} {path}")


@pytest.mark.parametrize(
    "mode,scenario", [("forward", s) for s in FORWARD_SCENARIOS] + [("managed", s) for s in MANAGED_SCENARIOS]
)
def test_go_example_scenarios_with_http_stub(mode, scenario, monkeypatch, capsys):
    config = Config(mode, "test-token", f"https://api.test/api/v1/{mode}", timeout=2, poll_interval=0)
    run = Run(config)
    service = ExampleService(mode)
    cls, scenarios = (Forward, FORWARD_SCENARIOS) if mode == "forward" else (Managed, MANAGED_SCENARIOS)
    with cls(**config.client_options(), http_client=httpx.Client(transport=httpx.MockTransport(service))) as client:
        if mode == "forward":
            monkeypatch.setattr(batch, "batch_rows", lambda client, batch_id: service.outputs[batch_id])
        try:
            scenarios[scenario](client, run)
        finally:
            run.cleanup()
    assert not run.cleanups
    assert not service.mounts
    created = [key for key in service.objects if not key.startswith(("event-", "memory-", "run-", "batch-"))]
    assert all(key in service.deleted for key in created)
    assert capsys.readouterr().out == ""
    outputs = {item["label"]: item["value"] for item in run.outputs}
    assert outputs["selected_model"] == "ultimate"
    if scenario == "models":
        assert outputs["models"] == [{"id": "ultimate", "is_enabled": True}]
    elif scenario == "dream":
        assert outputs["memory_path"] == "sdk-example/consolidated.md"
        assert outputs["memory_content"]
        assert outputs["output_memory_store_id"] in service.objects
    else:
        messages = [
            event["content"][0]["text"]
            for events in service.events.values()
            for event in events
            if event["type"] == "agent.message"
        ]
        assert [item["value"] for item in run.outputs if item["label"] == "assistant"] == messages
    if scenario != "models":
        assert outputs["cleanup"] == "completed"


def test_turn_assertions_require_final_assistant_output_and_successful_idle():
    result = TurnResult()
    for event in [
        {"type": "user.message", "content": [{"type": "text", "text": "expected"}]},
        {"type": "agent.tool_result", "content": [{"type": "text", "text": "expected"}]},
        {"type": "event_delta", "text": "expected"},
        {"type": "session.status_idle", "stop_reason": {"type": "end_turn"}},
    ]:
        result.observe(event)
    with pytest.raises(AssertionError, match="No idle state"):
        result.verify(["expected"])
    result.observe({"type": "agent.message", "content": [{"type": "text", "text": "expected"}]})
    result.observe({"type": "agent.message", "content": [{"type": "text", "text": "final answer"}]})
    result.observe({"type": "session.status_idle", "stop_reason": {"type": "end_turn"}})
    with pytest.raises(AssertionError, match="missing"):
        result.verify(["expected"])
    with pytest.raises(AssertionError, match="No actual tool"):
        result.verify(["final answer"], require_tool=True)
    result.observe({"type": "agent.tool_use"})
    result.verify(["final answer"], require_tool=True)


@pytest.mark.parametrize("reason", ["budget_exceeded", "tool_confirmation", "max_iterations"])
def test_turn_rejects_idle_that_needs_further_action(reason):
    with pytest.raises(AssertionError, match="stopped early"):
        TurnResult(text="answer").observe({"type": "session.status_idle", "stop_reason": {"type": reason}})


def test_memory_facts_are_absent_from_prompt_and_index():
    memory = ProjectMemory(release_time="21:34", contact="林岚", rollback_version="v2.456.789")
    for fact in memory.expected():
        assert fact in memory.content()
        assert fact not in memory.prompt()
        assert fact not in memory.index()


def test_cleanup_is_reverse_order_and_continues_after_failures():
    run = Run(Config("forward", "secret"))
    calls = []
    run.track("first", "first", lambda: calls.append("first"))

    def fail():
        calls.append("second")
        raise ValueError("secret https://signed.test/?token=sensitive")

    run.track("second", "second", fail)
    run.track("third", "third", lambda: calls.append("third"))
    with pytest.raises(RuntimeError) as caught:
        run.cleanup()
    assert calls == ["third", "second", "first"]
    assert "secret" not in str(caught.value)
    assert "sensitive" not in str(caught.value)
    assert not any(item["label"] == "cleanup" for item in run.outputs)


def test_config_file_is_data_and_environment_wins(tmp_path, monkeypatch):
    path = tmp_path / ".env"
    path.write_text(
        "QODER_FORWARD_PAT='file-token'\nVALUE=$(touch /tmp/never-execute)\nQODER_FORWARD_MODEL=ultimate # comment\n"
    )
    assert read_env(path)["VALUE"] == "$(touch /tmp/never-execute)"
    monkeypatch.setenv("QODER_FORWARD_PAT", "env-token")
    monkeypatch.delenv("QODER_FORWARD_BASE_URL", raising=False)
    config = Config.load("forward", env_file=str(path))
    assert config.access_token == "env-token"
    assert config.model == "ultimate"
    assert "env-token" not in repr(config)
    assert "env-token" not in safe_error(ValueError("env-token"), config.access_token)


def test_choose_model_rejects_disabled_preference():
    from types import SimpleNamespace

    models = SimpleNamespace(
        data=[SimpleNamespace(id="ultimate", is_enabled=True), SimpleNamespace(id="disabled", is_enabled=False)]
    )
    assert choose_model(models, "") == "ultimate"
    with pytest.raises(AssertionError):
        choose_model(models, "disabled")


@pytest.mark.parametrize("fails", [False, True])
def test_single_scenario_cli_defaults_to_that_scenario_and_cleans_up(fails, monkeypatch, capsys):
    config = Config("forward", "test-token")
    monkeypatch.setattr(Config, "load", lambda *args, **kwargs: config)
    monkeypatch.setattr(sys, "argv", ["examples.forward.memory", "--output", "json"])
    http_client = httpx.Client(transport=httpx.MockTransport(lambda request: httpx.Response(200)))
    client = Forward(access_token=config.access_token, http_client=http_client)
    calls = []

    def memory(client, context):
        def cleanup():
            assert not http_client.is_closed
            calls.append("cleanup")

        context.track("memory_store", "store-1", cleanup)
        calls.append("memory")
        if fails:
            raise RuntimeError("test-token failed")

    with pytest.raises(SystemExit) as caught:
        run_cli("forward", lambda **kwargs: client, {"memory": memory})

    assert caught.value.code == (1 if fails else 0)
    assert calls == ["memory", "cleanup"]
    assert http_client.is_closed
    output = capsys.readouterr().out
    result = json.loads(output)
    assert result[0]["scenario"] == "memory"
    assert result[0]["passed"] is not fails
    assert bool(result[0]["errors"]) is fails
    assert result[0]["outputs"] == [
        {"label": "memory_store_id", "value": "store-1"},
        {"label": "cleanup", "value": "completed"},
    ]
    assert "test-token" not in output


@pytest.mark.parametrize("mode", ["forward", "managed"])
@pytest.mark.parametrize("scenario", ["models", "session"])
@pytest.mark.parametrize("output_format", ["text", "json"])
def test_cli_displays_api_results(mode, scenario, output_format, monkeypatch, capsys):
    config = Config(mode, "test-token", f"https://api.test/api/v1/{mode}", timeout=2, poll_interval=0)
    monkeypatch.setattr(Config, "load", lambda *args, **kwargs: config)
    monkeypatch.setattr(sys, "argv", [f"examples.{mode}.{scenario}", "--output", output_format])
    service = ExampleService(mode)
    cls, scenarios = (Forward, FORWARD_SCENARIOS) if mode == "forward" else (Managed, MANAGED_SCENARIOS)

    def client_type(**options):
        return cls(**options, http_client=httpx.Client(transport=httpx.MockTransport(service)))

    with pytest.raises(SystemExit) as caught:
        run_cli(mode, client_type, {scenario: scenarios[scenario]})
    assert caught.value.code == 0
    captured = capsys.readouterr()
    assert captured.err == ""
    assert "test-token" not in captured.out
    if output_format == "json":
        result = json.loads(captured.out)
        assert len(result) == 1
        assert result[0]["scenario"] == scenario
        assert result[0]["passed"] is True
        values = {item["label"]: item["value"] for item in result[0]["outputs"]}
        assert values["selected_model"] == "ultimate"
        if scenario == "models":
            assert values["models"] == [{"id": "ultimate", "is_enabled": True}]
        else:
            session_id = next(iter(service.events))
            assert values["session_id"] == session_id
            assert values["assistant"] == service.events[session_id][-2]["content"][0]["text"]
            assert values["user"] == service.events[session_id][0]["content"][0]["text"]
            assert values["cleanup"] == "completed"
    else:
        assert captured.out.startswith(f"[{mode}.{scenario}]\n")
        assert captured.out.endswith(f"{scenario}: PASS\n")
        assert "selected_model: ultimate\n" in captured.out
        if scenario == "models":
            assert '"id": "ultimate"' in captured.out
            assert '"is_enabled": true' in captured.out
        else:
            session_id = next(iter(service.events))
            assistant = service.events[session_id][-2]["content"][0]["text"]
            prompt = service.events[session_id][0]["content"][0]["text"]
            assert f"session_id: {session_id}\n" in captured.out
            assert f"user: {prompt}\n" in captured.out
            assert f"assistant: {assistant}\n" in captured.out
            assert "cleanup: completed\n" in captured.out


@pytest.mark.parametrize("output_format", ["text", "json"])
def test_cli_validation_error_identifies_field_without_response_contents(output_format, monkeypatch, capsys):
    config = Config("forward", "test-token", "https://api.test/api/v1/forward")
    monkeypatch.setattr(Config, "load", lambda *args, **kwargs: config)
    monkeypatch.setattr(sys, "argv", ["examples.forward.models", "--output", output_format])

    def client_type(**options):
        return Forward(
            **options,
            http_client=httpx.Client(
                transport=httpx.MockTransport(
                    lambda _: httpx.Response(
                        200,
                        json={"data": [{"id": "ultimate", "is_enabled": "private-response-value"}]},
                        headers={"x-request-id": "req-validation"},
                    )
                )
            ),
        )

    with pytest.raises(SystemExit) as caught:
        run_cli("forward", client_type, {"models": FORWARD_SCENARIOS["models"]})
    assert caught.value.code == 1
    captured = capsys.readouterr()
    if output_format == "json":
        result = json.loads(captured.out)
        assert result[0]["passed"] is False
        error = result[0]["errors"][0]
    else:
        assert "models: FAIL" in captured.out
        error = captured.err
    assert "APIResponseValidationError" in error
    assert "HTTP 200 GET /api/v1/forward/models" in error
    assert "request_id=req-validation" in error
    assert "data.0.is_enabled" in error
    assert "bool_parsing" in error
    assert "private-response-value" not in captured.out + captured.err
    assert "test-token" not in captured.out + captured.err


def test_status_error_shows_server_reason_and_redacts_token_and_signed_url():
    from qca import BadRequestError

    with Forward(
        access_token="test-token",
        base_url="https://api.test/api/v1/forward",
        http_client=httpx.Client(
            transport=httpx.MockTransport(
                lambda _: httpx.Response(
                    400,
                    json={
                        "error": {
                            "type": "invalid_request_error",
                            "message": "Idempotency-Key header is required; test-token https://signed.test/?secret=value",
                        },
                        "private": "unrelated-response-value",
                    },
                    headers={"x-request-id": "req-missing-key"},
                )
            )
        ),
    ) as client:
        with pytest.raises(BadRequestError) as caught:
            client.memory_stores.create(name="memory", idempotency_key="key")
    error = safe_error(caught.value, "test-token")
    assert "HTTP 400 POST /api/v1/forward/memory_stores" in error
    assert "request_id=req-missing-key" in error
    assert "Idempotency-Key header is required" in error
    assert "test-token" not in error
    assert "signed.test" not in error
    assert "secret=value" not in error
    assert "unrelated-response-value" not in error
