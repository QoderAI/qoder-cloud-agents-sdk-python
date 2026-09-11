from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["IdentityStats"]


class IdentityStats(BaseModel):
    total_identities: Optional[int] = None
    active_identities: Optional[int] = None
    total_agents: Optional[int] = None
    total_sessions: Optional[int] = None
