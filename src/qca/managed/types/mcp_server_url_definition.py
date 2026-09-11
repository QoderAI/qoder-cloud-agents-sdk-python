from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["MCPServerURLDefinition"]


class MCPServerURLDefinition(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    url: Optional[str] = None
