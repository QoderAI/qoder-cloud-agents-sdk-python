from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .session_thread_agent_union import SessionThreadAgentUnion
    from .session_thread_stats import SessionThreadStats
    from .session_thread_usage import SessionThreadUsage

__all__ = ["SessionThread"]


class SessionThread(BaseModel):
    id: Optional[str] = None
    agent: Optional[SessionThreadAgentUnion] = None
    archived_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    parent_thread_id: Optional[str] = None
    session_id: Optional[str] = None
    stats: Optional[SessionThreadStats] = None
    status: Optional[str] = None
    type: Optional[str] = None
    updated_at: Optional[datetime] = None
    usage: Optional[SessionThreadUsage] = None
