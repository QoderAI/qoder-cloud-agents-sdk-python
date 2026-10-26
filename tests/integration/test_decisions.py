"""Opt-in Decision evaluation; records are retained by the server (no delete API)."""

import os
from uuid import uuid4

import pytest

from tests.support.harness import read_env

pytestmark = pytest.mark.integration


@pytest.mark.parametrize("live_example", ["forward"], indirect=True)
@pytest.mark.parametrize("mode", ["state", "session"])
def test_decisions(live_example, mode):
    values = {**read_env(os.environ.get("QODER_LIVE_ENV_FILE", ".env.live")), **os.environ}
    for gate in ("WRITE", "EXECUTION", "DECISIONS"):
        if values.get(f"QODER_FORWARD_LIVE_ALLOW_{gate}") != "true":
            pytest.skip(f"QODER_FORWARD_LIVE_ALLOW_{gate}=true is required")
    session_id = values.get("QODER_DECISION_SESSION_ID")
    if mode == "session" and not session_id:
        pytest.skip("Set QODER_DECISION_SESSION_ID to an accessible Session with history")
    client, context = live_example
    params = {
        "questions": [
            {
                "type": "choice",
                "instructions": "Return true only if RESOLVED_SDK_TEST appears in the input.",
                "choices": [{"value": True}, {"value": False}],
            },
            {
                "type": "score",
                "instructions": "Select high if RISK_LEVEL=high appears, otherwise select low.",
                "levels": [{"label": "low", "score": 0}, {"label": "high", "score": 10}],
            },
        ],
        "idempotency_key": str(uuid4()),
        **({"session_id": session_id} if mode == "session" else {"state": {"message": "RISK_LEVEL=low"}}),
    }
    decision = client.decisions.create(**params, timeout=context.remaining())
    assert decision.id and decision.status == "completed"
    assert decision.context.mode == mode and len(decision.answers) == 2
    assert 0 < decision.context.estimated_input_tokens <= decision.context.max_input_tokens
    if mode == "state":
        assert decision.session_id is None
        assert decision.answers[0].value is False and decision.answers[1].score == 0
    else:
        assert decision.session_id == session_id and decision.context.included_event_count > 0
    replay = client.decisions.create(**params, timeout=context.remaining())
    assert replay.id == decision.id and replay.completed_at == decision.completed_at
    stored = client.decisions.retrieve(decision.id)
    assert stored.to_dict() == decision.to_dict()
    page = client.decisions.list(limit=1, **({"session_id": session_id} if mode == "session" else {}))
    assert len(page.data) == 1
    if mode == "session":
        assert page.data[0].session_id == session_id
    if page.has_next_page():
        following = page.get_next_page()
        assert following.data and following.data[0].id != page.data[0].id
    context.output("decision_id", decision.id)
