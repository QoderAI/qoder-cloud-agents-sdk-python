from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["SystemOverride"]


class SystemOverride(BaseModel):
    mode: Optional[str] = None
    content: Optional[str] = None
