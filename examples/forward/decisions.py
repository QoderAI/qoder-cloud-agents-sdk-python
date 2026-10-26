"""Create a Decision using shared PAT/SA configuration.

The Decision API is in Beta. Its behavior may change in future updates.

Run: python -m examples.forward.decisions --env .env.live
Optionally set QODER_DECISION_SESSION_ID to evaluate an accessible Session.
"""

from __future__ import annotations

import os
from uuid import uuid4

from examples.common.live import Run, run_cli
from qca import Forward
from qca.forward.types import DecisionCreateParams


def run(client: Forward, context: Run) -> None:
    params: DecisionCreateParams = {
        "state": {"message": "The issue is resolved; everything works now."},
        "questions": [
            {
                "type": "choice",
                "name": "resolved",
                "instructions": "Has the user explicitly confirmed that their issue is resolved?",
                "choices": [{"value": True}, {"value": False}],
            }
        ],
        "idempotency_key": str(uuid4()),
    }
    session_id = os.environ.get("QODER_DECISION_SESSION_ID")
    if session_id:
        del params["state"]
        params["session_id"] = session_id
    decision = client.decisions.create(**params)
    stored = client.decisions.retrieve(decision.id)
    context.output("decision", stored.to_dict(mode="json"))
    page = client.decisions.list(limit=5, **({"session_id": session_id} if session_id else {}))
    context.output("page", [{"id": item.id, "status": item.status} for item in page.data])
    # Decision records expire according to server retention; there is no delete API.


if __name__ == "__main__":
    run_cli("forward", Forward, {"decisions": run})
