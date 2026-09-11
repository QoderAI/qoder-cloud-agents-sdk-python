from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .identity_clear_response_summary import IdentityClearResponseSummary

__all__ = ["IdentityClearResponse"]


class IdentityClearResponse(BaseModel):
    identity_id: Optional[str] = None
    status: Optional[str] = None
    completed_at: Optional[datetime] = None
    summary: Optional[IdentityClearResponseSummary] = None
