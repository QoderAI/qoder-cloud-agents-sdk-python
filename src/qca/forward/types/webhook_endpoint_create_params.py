from __future__ import annotations

from typing_extensions import Required, TypedDict


class WebhookEndpointCreateParams(TypedDict, total=False):
    url: Required[str]
    events: Required[list[str]]
    description: str
    metadata: dict[str, str]
    idempotency_key: str
