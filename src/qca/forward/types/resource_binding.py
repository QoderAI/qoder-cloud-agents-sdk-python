from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["ResourceBinding"]


class ResourceBinding(BaseModel):
    enabled: Optional[bool] = None
