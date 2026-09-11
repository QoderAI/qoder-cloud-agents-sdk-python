from __future__ import annotations

from typing import List, Optional

from qca.common._models import BaseModel

__all__ = ["StreamSessionThreadEventsUnionStopReason"]


class StreamSessionThreadEventsUnionStopReason(BaseModel):
    type: Optional[str] = None
    event_ids: Optional[List[str]] = None
