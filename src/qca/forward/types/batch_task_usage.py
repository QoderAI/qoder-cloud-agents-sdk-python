from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["BatchTaskUsage"]


class BatchTaskUsage(BaseModel):
    total_credits: Optional[float] = None
