from __future__ import annotations

from typing_extensions import TypedDict


class WebhookEndpointUpdateParams(TypedDict, total=False):
    url: str
    events: list[str]
    description: str
    active: bool
    metadata: dict[str, str | None]
