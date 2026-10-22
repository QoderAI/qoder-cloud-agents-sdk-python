import base64
import inspect
import json
from pathlib import Path
from unittest.mock import patch

import httpx
import pytest

from qca import AsyncForward, Forward, InternalServerError
from qca.forward import WebhookVerificationError, verify_webhook_signature


async def resolve(value):
    return await value if inspect.isawaitable(value) else value


@pytest.mark.parametrize("async_", [False, True])
@pytest.mark.parametrize("auth", [{"pat": "token"}, {"auth_mode": "sa", "access_token": "token"}])
async def test_webhook_lifecycle(async_, auth):
    requests = []

    def handle(r):
        requests.append(r)
        assert r.headers["authorization"] == "Bearer token"
        if r.method == "POST" and r.url.path.endswith("/endpoints"):
            assert r.headers["Idempotency-Key"] == "create-once"
            assert json.loads(r.content) == {"url": "https://hooks.example.com/qca", "events": ["future.event"]}
            return httpx.Response(201, json={"id": "endpoint", "signing_secret": "synthetic", "future": 1})
        if r.method == "PUT":
            assert json.loads(r.content) == {"active": False, "metadata": {"remove": None, "keep": "value"}}
            return httpx.Response(200, json={"id": "endpoint", "active": False, "last_success_at": None})
        assert not r.content
        if r.method == "DELETE":
            return httpx.Response(204)
        if r.url.path.endswith("/test"):
            return httpx.Response(202, json={"event_id": 7, "delivery_rows": 0})
        return httpx.Response(200, json={"id": "endpoint", "events": ["future.event"], "future": 1})

    http = (httpx.AsyncClient if async_ else httpx.Client)(transport=httpx.MockTransport(handle))
    client = (AsyncForward if async_ else Forward)(http_client=http, **auth)
    try:
        resource = client.webhooks.endpoints
        created = await resolve(
            resource.create(url="https://hooks.example.com/qca", events=["future.event"], idempotency_key="create-once")
        )
        assert created.signing_secret == "synthetic" and "synthetic" not in repr(created)
        updated = await resolve(
            resource.update("opaque /?%#", active=False, metadata={"remove": None, "keep": "value"})
        )
        assert updated.active is False and updated.last_success_at is None
        for name in ["retrieve", "enable", "disable"]:
            endpoint = await resolve(getattr(resource, name)("opaque /?%#"))
            assert endpoint.events == ["future.event"] and endpoint.model_extra["future"] == 1
        result = await resolve(resource.test("opaque /?%#"))
        assert result.delivery_rows == 0
        assert await resolve(resource.delete("opaque /?%#")) is None
        for r in requests[1:]:
            assert "/webhook/endpoints/opaque%20%2F%3F%25%23" in r.url.raw_path.decode()
    finally:
        await resolve(client.close())


@pytest.mark.parametrize("async_", [False, True])
async def test_webhook_cursor_order_and_unsafe_retry(async_):
    calls = []

    def handle(r):
        calls.append(r)
        if r.method == "POST":
            return httpx.Response(503, json={"error": {"message": "unavailable"}})
        assert "page" not in r.url.params and r.url.params["limit"] == "2"
        if len(calls) == 1:
            return httpx.Response(
                200, json={"data": [{"id": "z"}, {"id": "a"}], "last_id": "opaque/+?", "has_more": True}
            )
        assert r.url.params["after_id"] == "opaque/+?"
        return httpx.Response(200, json={"data": [], "last_id": None, "first_id": None, "has_more": False})

    http = (httpx.AsyncClient if async_ else httpx.Client)(transport=httpx.MockTransport(handle))
    client = (AsyncForward if async_ else Forward)(pat="test", http_client=http, max_retries=2)
    try:
        page = await resolve(client.webhooks.endpoints.list(limit=2))
        items = [item async for item in page] if async_ else list(page)
        assert [i.id for i in items] == ["z", "a"] and len(calls) == 2
        with pytest.raises(InternalServerError):
            await resolve(client.webhooks.endpoints.test("id"))
        assert len(calls) == 3
    finally:
        await resolve(client.close())


@pytest.fixture
def vector():
    return json.loads((Path(__file__).parent / "fixtures/webhook-signature.json").read_text())


def test_webhook_signature_vector_and_window(vector):
    v = vector
    headers = {
        "webhook-id": v["id"],
        "Webhook-Timestamp": v["timestamp"],
        "Webhook-Signature": "v2,unknown v1,invalid " + v["signature"],
    }
    for delta in [-300, 0, 300]:
        with patch("qca.forward.webhook_signature.time.time", return_value=int(v["timestamp"]) + delta):
            verify_webhook_signature(v["payload"].encode(), headers, v["secret"])
    for delta in [-301, 301]:
        with (
            patch("qca.forward.webhook_signature.time.time", return_value=int(v["timestamp"]) + delta),
            pytest.raises(WebhookVerificationError),
        ):
            verify_webhook_signature(v["payload"].encode(), headers, v["secret"])
    with patch("qca.forward.webhook_signature.time.time", return_value=int(v["timestamp"])):
        for name, value in [
            ("Webhook-Timestamp", "9223372036854775807"),
            ("Webhook-Timestamp", "-1"),
            ("Webhook-Signature", "v2,abc"),
            ("webhook-id", "other"),
        ]:
            with pytest.raises(WebhookVerificationError):
                verify_webhook_signature(v["payload"].encode(), {**headers, name: value}, v["secret"])
        with pytest.raises(WebhookVerificationError):
            verify_webhook_signature((v["payload"] + " ").encode(), headers, v["secret"])
        for secret in ["", "whsec_", "whsec_bad!", "whsec_" + base64.b64encode(b"too short").decode()]:
            with pytest.raises(WebhookVerificationError):
                verify_webhook_signature(v["payload"].encode(), headers, secret)


def test_receiver_example_preserves_unknown_and_synthetic_events():
    import hashlib
    import hmac
    import time

    from examples.forward.webhooks import parse_delivery

    key = b"0123456789abcdef0123456789abcdef"
    secret = "whsec_" + base64.b64encode(key).decode()
    for event in [
        {"type": "event", "data": {"type": "future.event", "extra": 42}},
        {"type": "event", "endpoint_id": "id", "note": "synthetic"},
    ]:
        body = json.dumps(event).encode()
        timestamp = str(int(time.time()))
        signature = base64.b64encode(
            hmac.new(key, b"whe_test." + timestamp.encode() + b"." + body, hashlib.sha256).digest()
        ).decode()
        headers = {"Webhook-ID": "whe_test", "Webhook-Timestamp": timestamp, "Webhook-Signature": "v1," + signature}
        assert parse_delivery(body, headers, secret) == event
        with pytest.raises(WebhookVerificationError):
            parse_delivery(body + b" ", headers, secret)
