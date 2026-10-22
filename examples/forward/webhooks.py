"""List webhook endpoints; parse_delivery can be used inside your HTTP receiver.

Run: python -m examples.forward.webhooks
The management client uses the shared PAT/SA configuration (administrator SAT required).
"""

from __future__ import annotations

import json
from collections.abc import Mapping
from typing import Any

from examples.common.live import Run, run_cli
from qca import Forward
from qca.forward import verify_webhook_signature


def parse_delivery(raw_body: bytes, headers: Mapping[str, str], secret: str) -> Any:
    verify_webhook_signature(raw_body, headers, secret)
    return json.loads(raw_body)


def run(client: Forward, context: Run) -> None:
    for endpoint in client.webhooks.endpoints.list(limit=20):
        context.output("webhook_endpoint", {"id": endpoint.id, "active": endpoint.active})


if __name__ == "__main__":
    run_cli("forward", Forward, {"webhooks": run})
