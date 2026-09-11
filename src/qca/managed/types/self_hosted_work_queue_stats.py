from __future__ import annotations

from typing import Literal, Optional

from qca.common._models import BaseModel

__all__ = ["SelfHostedWorkQueueStats"]


class SelfHostedWorkQueueStats(BaseModel):
    depth: Optional[int] = None
    oldest_queued_at: Optional[str] = None
    pending: Optional[int] = None
    type: Optional[Literal["work_queue_stats"]] = None
    workers_polling: Optional[int] = None
