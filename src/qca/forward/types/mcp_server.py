from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["MCPServer"]


class MCPServer(BaseModel):
    type: Optional[str] = None
    name: Optional[str] = None
    url: Optional[str] = None
