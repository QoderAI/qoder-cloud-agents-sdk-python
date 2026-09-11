from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Literal, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .session_work_data import SessionWorkData

__all__ = ["SelfHostedWork"]


class SelfHostedWork(BaseModel):
    id: Optional[str] = None
    acknowledged_at: Optional[str] = None
    created_at: Optional[str] = None
    data: Optional[SessionWorkData] = None
    environment_id: Optional[str] = None
    latest_heartbeat_at: Optional[str] = None
    metadata: Optional[Dict[str, str]] = None
    secret: Optional[str] = None
    started_at: Optional[str] = None
    state: Optional[str] = None
    stop_requested_at: Optional[str] = None
    stopped_at: Optional[str] = None
    type: Optional[Literal["work"]] = None
