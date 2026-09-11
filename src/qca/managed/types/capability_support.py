from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["CapabilitySupport"]


class CapabilitySupport(BaseModel):
    supported: Optional[bool] = None
