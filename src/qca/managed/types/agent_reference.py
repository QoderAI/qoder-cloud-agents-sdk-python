from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["AgentReference"]


class AgentReference(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    version: Optional[int] = None
