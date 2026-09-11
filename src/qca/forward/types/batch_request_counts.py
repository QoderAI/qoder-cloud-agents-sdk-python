from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["BatchRequestCounts"]


class BatchRequestCounts(BaseModel):
    total: Optional[int] = None
    pending: Optional[int] = None
    running: Optional[int] = None
    completed: Optional[int] = None
    failed: Optional[int] = None
    cancelled: Optional[int] = None
    expired: Optional[int] = None
