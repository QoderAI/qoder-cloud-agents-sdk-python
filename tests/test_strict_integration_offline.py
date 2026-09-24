from __future__ import annotations

import httpx
import pytest

from tests.integration.conftest import live_example as live_example
from tests.integration.conftest import strict_live_client as strict_live_client
from tests.support.assertions import assert_readonly_list_response
from tests.support.harness import Config

READ_CASES = [
    ("forward", "models"),
    ("forward", "templates"),
    ("forward", "sessions"),
    ("managed", "models"),
    ("managed", "agents"),
    ("managed", "sessions"),
]


@pytest.fixture(autouse=True)
def service(monkeypatch):
    state = {"body": {"data": [{"id": "item-1"}]}, "status": 200, "requests": []}

    def handle(request):
        state["requests"].append(request)
        assert request.method == "GET"
        return httpx.Response(state["status"], json=state["body"], headers={"x-request-id": "req-schema"})

    class StubClient(httpx.Client):
        def __init__(self, **kwargs):
            super().__init__(transport=httpx.MockTransport(handle), **kwargs)

    monkeypatch.setenv("QODER_RUN_LIVE", "1")
    monkeypatch.setattr(
        Config,
        "load",
        classmethod(lambda cls, mode, **kwargs: Config(mode, "test-token", f"https://api.test/{mode}")),
    )
    monkeypatch.setattr(httpx, "Client", StubClient)
    return state


@pytest.mark.parametrize("strict_live_client,resource", READ_CASES, indirect=["strict_live_client"])
@pytest.mark.parametrize("populated", [True, False])
def test_strict_integration_checks_are_bounded_reads(strict_live_client, resource, populated, service):
    if not populated:
        service["body"] = {"data": []}
    assert_readonly_list_response(strict_live_client, resource)
    assert len(service["requests"]) == 1
    request = service["requests"][0]
    assert request.url.path.endswith(f"/{resource}")
    expected_limit = None if request.url.path == "/forward/models" else "1"
    assert request.url.params.get("limit") == expected_limit


@pytest.mark.parametrize("strict_live_client,resource", READ_CASES, indirect=["strict_live_client"])
def test_strict_integration_rejects_schema_drift_with_safe_diagnostics(strict_live_client, resource, service):
    service["body"] = {"data": [{"id": {"private": "server-value"}}]}
    with pytest.raises(AssertionError, match="APIResponseValidationError") as caught:
        assert_readonly_list_response(strict_live_client, resource)
    message = str(caught.value)
    assert "data.0.id" in message
    assert "request_id=req-schema" in message
    assert "server-value" not in message
    assert "test-token" not in message


@pytest.mark.parametrize("strict_live_client,resource", READ_CASES, indirect=["strict_live_client"])
@pytest.mark.parametrize("body", [{}, {"data": None}, {"data": [{"id": ""}]}, {"data": [{}]}])
def test_strict_integration_rejects_missing_collection_or_item_identity(strict_live_client, resource, body, service):
    service["body"] = body
    with pytest.raises(AssertionError):
        assert_readonly_list_response(strict_live_client, resource)


@pytest.mark.parametrize("strict_live_client", ["forward", "managed"], indirect=True)
def test_strict_integration_does_not_hide_http_failures(strict_live_client, service):
    service["status"] = 403
    service["body"] = {"error": {"message": "permission denied"}}
    with pytest.raises(AssertionError, match="HTTP 403"):
        assert_readonly_list_response(strict_live_client, "models")
    assert len(service["requests"]) == 1


@pytest.mark.parametrize("live_example", ["forward", "managed"], indirect=True)
def test_existing_business_scenarios_keep_default_response_parsing(live_example, service):
    client, _ = live_example
    service["body"] = {"data": [{"id": "model-1", "is_enabled": "future-value"}]}
    assert client.models.list().data[0].is_enabled == "future-value"
