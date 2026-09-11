from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["BatchTaskError"]


class BatchTaskError(BaseModel):
    code: Optional[str] = None
    message: Optional[str] = None
