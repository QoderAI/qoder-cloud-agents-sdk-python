from __future__ import annotations

from datetime import datetime
from typing import Optional

from qca.common._models import BaseModel

__all__ = ["BatchFile"]


class BatchFile(BaseModel):
    url: Optional[str] = None
    expires_at: Optional[datetime] = None
