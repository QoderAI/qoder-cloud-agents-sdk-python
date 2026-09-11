from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["BatchUsage"]


class BatchUsage(BaseModel):
    total_credits: Optional[float] = None
