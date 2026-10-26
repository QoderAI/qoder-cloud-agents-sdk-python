import copy
import inspect
import json
from pathlib import Path

import httpx
import pytest

from qca import APIStatusError, AsyncForward, Forward
from qca.forward.types import Decision

FIXTURE = json.loads((Path(__file__).parent / "fixtures/decisions.json").read_text())


async def resolve(value):
    return await value if inspect.isawaitable(value) else value


def client_for(async_, handle, **options):
    http = (httpx.AsyncClient if async_ else httpx.Client)(transport=httpx.MockTransport(handle))
    return (AsyncForward if async_ else Forward)(http_client=http, **options)


@pytest.mark.parametrize("async_", [False, True])
@pytest.mark.parametrize("auth", [{"pat": "token"}, {"auth_mode": "sa", "access_token": "token"}])
async def test_decision_state_session_and_response_metadata(async_, auth):
    calls = []

    def handle(request):
        calls.append(request)
        assert request.headers["authorization"] == "Bearer token"
        assert "x-qoder-beta" not in request.headers
        assert not request.url.query
        result = copy.deepcopy(FIXTURE["response"])
        result["future_field"] = 1
        if request.method == "POST":
            assert request.url.path == "/api/v1/forward/decisions"
            body = json.loads(request.content)
            assert body["questions"] == FIXTURE["request"]["questions"]
            if len(calls) == 1:
                assert body == FIXTURE["request"]
                assert request.headers["Idempotency-Key"] == "header-wins"
            else:
                assert body == {"session_id": "sess_own", "questions": FIXTURE["request"]["questions"]}
                result["session_id"] = "sess_own"
                result["context"].update(
                    mode="session",
                    snapshot_at="2026-10-26T00:00:00.123456789Z",
                    truncated=True,
                    truncation_reasons=["segment_budget"],
                    included_segment_count=12,
                    scan_limited=False,
                    future_context=True,
                )
                result["answers"] = [{"type": "refusal", "name": "private", "refusal": "Cannot assess"}]
        else:
            assert request.url.raw_path.endswith(b"/decisions/opaque%20%2F%3F%25%23")
            assert not request.content
        return httpx.Response(200, json=result, headers={"x-request-id": "req_decision"})

    client = client_for(async_, handle, _strict_response_validation=True, **auth)
    try:
        result = await resolve(
            client.decisions.create(
                **FIXTURE["request"], idempotency_key="parameter-key", extra_headers={"Idempotency-Key": "header-wins"}
            )
        )
        assert isinstance(result, Decision)
        assert result.answers[0].value is False and result.answers[1].score == 0
        assert "value" not in result.answers[1].model_fields_set
        assert result.session_id is None and result.usage is None and result.error is None
        assert result.created_at.microsecond == 123456
        assert result._request_id == "req_decision" and result.model_extra["future_field"] == 1
        result = await resolve(
            client.decisions.create(session_id="sess_own", questions=FIXTURE["request"]["questions"])
        )
        assert result.context.truncated and result.context.included_segment_count == 12
        assert result.context.scan_limited is False and result.context.model_extra["future_context"] is True
        assert result.answers[0].refusal == "Cannot assess" and "value" not in result.answers[0].model_fields_set
        assert (await resolve(client.decisions.retrieve("opaque /?%#"))).id == "dec_contract"
        with pytest.raises(ValueError):
            await resolve(client.decisions.retrieve(""))
        assert len(calls) == 3
    finally:
        await resolve(client.close())


@pytest.mark.parametrize("async_", [False, True])
@pytest.mark.parametrize("cursor", ["after_id", "before_id"])
async def test_decision_pagination_keeps_filter_options_and_order(async_, cursor):
    calls = []

    def handle(request):
        calls.append(request)
        assert request.url.params["session_id"] == "sess_own"
        assert request.url.params["limit"] == "1" and "page" not in request.url.params
        assert request.headers["X-Page"] == "kept"
        assert not request.content
        other = "before_id" if cursor == "after_id" else "after_id"
        assert other not in request.url.params
        assert request.url.params[cursor] == ("dec_start" if len(calls) == 1 else "dec_z")
        if len(calls) == 1:
            return httpx.Response(
                200,
                json={
                    "data": [
                        {"id": "dec_z", "status": "running", "context": {"mode": "session"}, "completed_at": None}
                    ],
                    "first_id": "dec_z",
                    "last_id": "dec_z",
                    "has_more": True,
                },
            )
        return httpx.Response(
            200,
            json={
                "data": [
                    {
                        "id": "dec_a",
                        "status": "failed",
                        "error": {"code": "decision_upstream_timeout", "message": "Timed out"},
                    }
                ],
                "first_id": "dec_a",
                "last_id": "dec_a",
                "has_more": False,
            },
        )

    client = client_for(async_, handle, pat="token")
    try:
        page = client.decisions.list(
            session_id="sess_own", limit=1, extra_headers={"X-Page": "kept"}, **{cursor: "dec_start"}
        )
        items = [d async for d in page] if async_ else list(page)
        assert [d.id for d in items] == ["dec_z", "dec_a"] and len(calls) == 2
        assert items[0].completed_at is None and items[1].error.code == "decision_upstream_timeout"
    finally:
        await resolve(client.close())


@pytest.mark.parametrize("async_", [False, True])
@pytest.mark.parametrize("keyed", [False, True])
async def test_decision_retry_requires_key_and_preserves_exact_body(async_, keyed):
    calls = []

    def handle(request):
        calls.append(request)
        assert request.headers.get("Idempotency-Key") == ("decision-once" if keyed else None)
        if len(calls) == 1:
            return httpx.Response(503, json={"error": {"message": "unavailable"}}, headers={"retry-after-ms": "1"})
        return httpx.Response(200, json=FIXTURE["response"])

    client = client_for(async_, handle, pat="token", max_retries=1)
    try:
        params = {**FIXTURE["request"], **({"idempotency_key": "decision-once"} if keyed else {})}
        if keyed:
            assert (await resolve(client.decisions.create(**params))).id == "dec_contract"
            assert len(calls) == 2 and calls[0].content == calls[1].content
        else:
            with pytest.raises(APIStatusError):
                await resolve(client.decisions.create(**params))
            assert len(calls) == 1
    finally:
        await resolve(client.close())


@pytest.mark.parametrize("async_", [False, True])
@pytest.mark.parametrize("status", [400, 401, 403, 404, 409, 422, 429, 504])
async def test_decision_error_keeps_correlation_and_server_validation(async_, status):
    calls = []

    def handle(request):
        calls.append(request)
        assert json.loads(request.content)["session_id"] == "sess_own"
        assert json.loads(request.content)["state"] == FIXTURE["request"]["state"]
        return httpx.Response(
            status,
            json={
                "request_id": "req_decision",
                "decision_id": "dec_failed",
                "error": {"type": "api_error", "code": "decision_test_error", "message": "Decision failed"},
            },
        )

    client = client_for(async_, handle, pat="token", max_retries=1 if status == 409 else 0)
    try:
        with pytest.raises(APIStatusError) as error:
            await resolve(client.decisions.create(**FIXTURE["request"], session_id="sess_own", idempotency_key="key"))
        assert error.value.status_code == status and error.value.body["decision_id"] == "dec_failed"
        assert error.value.request_id == "req_decision" and error.value.code == "decision_test_error"
        assert len(calls) == 1
    finally:
        await resolve(client.close())
