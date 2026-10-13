from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from qca.common._models import BaseModel

__all__ = ["ServiceAccountToken"]


class ServiceAccountToken(BaseModel):
    """A newly issued Forward SAT. Treat serialized responses as secrets; renewal is caller-owned."""

    type: Literal["service_account_token"]
    access_token: str = Field(repr=False)
    token_type: Literal["Bearer"]
    expires_in: int
    expires_at: datetime
    auth_token_id: str
    service_account_id: str
    credential_id: str
    subject_type: Literal["admin", "identity"]
    identity_id: str | None = None
