from __future__ import annotations

from typing import List, Optional

from qca.common._models import BaseModel

__all__ = ["SessionStreamEventStopReason"]


class SessionStreamEventStopReason(BaseModel):
    type: Optional[str] = None
    event_ids: Optional[List[str]] = None
