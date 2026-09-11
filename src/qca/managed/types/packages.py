from __future__ import annotations

from typing import List, Optional

from qca.common._models import BaseModel

__all__ = ["Packages"]


class Packages(BaseModel):
    apt: Optional[List[str]] = None
    cargo: Optional[List[str]] = None
    gem: Optional[List[str]] = None
    go: Optional[List[str]] = None
    npm: Optional[List[str]] = None
    pip: Optional[List[str]] = None
    type: Optional[str] = None
