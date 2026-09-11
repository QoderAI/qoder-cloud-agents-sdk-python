from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["DeletedVault"]


class DeletedVault(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
