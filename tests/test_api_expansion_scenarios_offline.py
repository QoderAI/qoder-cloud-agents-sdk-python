import httpx
import pytest

from qca import Forward, Managed
from tests.support.harness import Config, Run
from tests.support.scenarios.api_expansion import SCENARIOS
from tests.support.stub import ExampleService


@pytest.mark.parametrize("mode,scenario", list(SCENARIOS.values()), ids=list(SCENARIOS))
def test_new_api_scenario_and_cleanup(mode, scenario):
    service = ExampleService(mode)
    context = Run(
        Config(mode, "test-token", f"https://api.test/api/v1/{mode}", model="auto", timeout=2, poll_interval=0)
    )
    cls = Forward if mode == "forward" else Managed
    with cls(
        **context.config.client_options(), http_client=httpx.Client(transport=httpx.MockTransport(service))
    ) as client:
        try:
            scenario(client, context)
        finally:
            context.cleanup()
    assert not service.mounts
    created = [key for key in service.objects if not key.startswith(("event-", "memory-", "run-"))]
    assert all(key in service.deleted for key in created)
    assert not context.cleanups


@pytest.mark.parametrize("key", ["usage", "credential_update", "session_cancel"])
def test_new_api_live_assertions_reject_response_drift_and_still_cleanup(key):
    mode, scenario = SCENARIOS[key]
    service = ExampleService(mode)
    injected = False

    def handler(request):
        nonlocal injected
        response = service(request)
        data = response.json()
        target = (
            (key == "usage" and "/usage/" in request.url.path)
            or (
                key == "credential_update"
                and request.method == "POST"
                and "/credentials/" in request.url.path
                and "added" in request.content.decode()
            )
            or (key == "session_cancel" and request.url.path.endswith("/cancel"))
        )
        if target and not injected:
            injected = True
            if key == "usage":
                data["type"] = "wrong.list"
            elif key == "credential_update":
                data["metadata"]["keep"] = "wrong"
            else:
                data["type"] = "wrong"
            return httpx.Response(response.status_code, json=data)
        return response

    context = Run(Config(mode, "test-token", f"https://api.test/api/v1/{mode}", model="auto", poll_interval=0))
    cls = Forward if mode == "forward" else Managed
    with cls(
        **context.config.client_options(), http_client=httpx.Client(transport=httpx.MockTransport(handler))
    ) as client:
        try:
            with pytest.raises(AssertionError):
                scenario(client, context)
        finally:
            context.cleanup()
    assert injected
    assert not service.mounts
    created = [item for item in service.objects if not item.startswith(("event-", "memory-", "run-"))]
    assert all(item in service.deleted for item in created)
