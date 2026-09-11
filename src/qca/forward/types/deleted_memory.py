from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["DeletedMemory"]


class DeletedMemory(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    deleted: Optional[bool] = None
