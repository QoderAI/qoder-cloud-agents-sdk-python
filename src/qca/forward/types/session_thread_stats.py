from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["SessionThreadStats"]


class SessionThreadStats(BaseModel):
    active_seconds: Optional[int] = None
    duration_seconds: Optional[int] = None
    startup_seconds: Optional[int] = None
