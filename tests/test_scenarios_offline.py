from __future__ import annotations

import httpx
import pytest

from qca import Forward, Managed
from tests.support.assertions import TurnResult
from tests.support.harness import Config, Run, choose_model, read_env, safe_error
from tests.support.memory import ProjectMemory
from tests.support.scenarios.forward import SCENARIOS as FORWARD_SCENARIOS
from tests.support.scenarios.managed import SCENARIOS as MANAGED_SCENARIOS
from tests.support.stub import ExampleService, patch_batch_rows


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
            patch_batch_rows(monkeypatch, service)
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
    assert config.pat == "env-token"
    assert config.model == "ultimate"
    assert "env-token" not in repr(config)
    assert "env-token" not in safe_error(ValueError("env-token"), config.pat)


def test_choose_model_rejects_disabled_preference():
    from types import SimpleNamespace

    models = SimpleNamespace(
        data=[SimpleNamespace(id="ultimate", is_enabled=True), SimpleNamespace(id="disabled", is_enabled=False)]
    )
    assert choose_model(models, "") == "ultimate"
    with pytest.raises(AssertionError):
        choose_model(models, "disabled")


def test_validation_error_identifies_field_without_response_contents():
    from qca import APIResponseValidationError

    with Forward(
        pat="test-token",
        base_url="https://api.test/api/v1/forward",
        http_client=httpx.Client(
            transport=httpx.MockTransport(
                lambda _: httpx.Response(
                    200,
                    json={"data": [{"id": "ultimate", "is_enabled": "private-response-value"}]},
                    headers={"x-request-id": "req-validation"},
                )
            )
        ),
    ) as client:
        with pytest.raises(APIResponseValidationError) as caught:
            client.models.list()
    error = safe_error(caught.value, "test-token")
    assert "APIResponseValidationError" in error
    assert "HTTP 200 GET /api/v1/forward/models" in error
    assert "request_id=req-validation" in error
    assert "data.0.is_enabled" in error
    assert "bool_parsing" in error
    assert "private-response-value" not in error
    assert "test-token" not in error


def test_status_error_shows_server_reason_and_redacts_token_and_signed_url():
    from qca import BadRequestError

    with Forward(
        pat="test-token",
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
