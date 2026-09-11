from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["DreamModelConfig"]


class DreamModelConfig(BaseModel):
    id: Optional[str] = None
    speed: Optional[str] = None
