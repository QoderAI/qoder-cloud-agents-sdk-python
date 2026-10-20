from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["SessionThreadUsage"]


class SessionThreadUsage(BaseModel):
    total_credits: Optional[float] = None
