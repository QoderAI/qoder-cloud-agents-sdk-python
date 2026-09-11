from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["ModelConfigEffortUnion"]


class ModelConfigEffortUnion(BaseModel):
    type: Optional[str] = None
