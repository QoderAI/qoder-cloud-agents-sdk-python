from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .session_thread_stop_reason import SessionThreadStopReason

__all__ = ["SessionThread"]


class SessionThread(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    session_id: Optional[str] = None
    template_id: Optional[str] = None
    role: Optional[str] = None
    status: Optional[str] = None
    stop_reason: Optional[SessionThreadStopReason] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    parent_thread_id: Optional[str] = None
    name: Optional[str] = None
    created_by_tool_use_id: Optional[str] = None
    archived_at: Optional[datetime] = None
