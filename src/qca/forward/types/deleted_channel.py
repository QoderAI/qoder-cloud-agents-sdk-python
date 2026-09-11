from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["DeletedChannel"]


class DeletedChannel(BaseModel):
    id: Optional[str] = None
    deleted: Optional[bool] = None
