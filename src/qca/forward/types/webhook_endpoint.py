from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import Field

from qca.common._models import BaseModel


class WebhookEndpointCreateResponse(BaseModel):
    """The signing secret is returned only when creating an endpoint."""

    id: str | None = None
    url: str | None = None
    events: list[str] | None = None
    description: str | None = None
    metadata: dict[str, Any] | None = None
    active: bool | None = None
    created_at: datetime | None = None
    signing_secret: str | None = Field(default=None, repr=False)


class WebhookEndpoint(BaseModel):
    id: str | None = None
    url: str | None = None
    events: list[str] | None = None
    description: str | None = None
    metadata: dict[str, Any] | None = None
    active: bool | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    last_success_at: datetime | None = None
    last_failure_at: datetime | None = None
    disabled_reason: str | None = None
    consecutive_fail: int | None = None


class WebhookEndpointTestResponse(BaseModel):
    """Accepted delivery rows, not a delivery success report."""

    event_id: int | None = None
    delivery_rows: int | None = None
