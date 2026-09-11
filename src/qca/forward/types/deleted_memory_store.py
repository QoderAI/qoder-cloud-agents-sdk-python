from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["DeletedMemoryStore"]


class DeletedMemoryStore(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    deleted: Optional[bool] = None
