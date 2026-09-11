from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["MCPServerOverride"]


class MCPServerOverride(BaseModel):
    enabled: Optional[bool] = None
    type: Optional[str] = None
    url: Optional[str] = None
