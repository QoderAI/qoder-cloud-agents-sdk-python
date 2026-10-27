from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .schedule_run_trigger_context import ScheduleRunTriggerContext
    from .session_event import SessionEvent

__all__ = ["ScheduleRun"]


class ScheduleRun(BaseModel):
    initial_events: Optional[List[SessionEvent]] = None
    source: Optional[str] = None
    source_session_id: Optional[str] = None
    initial_events_version: Optional[int] = None
    id: Optional[str] = None
    schedule_id: Optional[str] = None
    identity_id: Optional[str] = None
    template_id: Optional[str] = None
    session_id: Optional[str] = None
    status: Optional[str] = None
    trigger_context: Optional[ScheduleRunTriggerContext] = None
    result_payload: Optional[str] = None
    push_sink: Optional[str] = None
    push_status: Optional[str] = None
    push_finished_at: Optional[datetime] = None
    attempt: Optional[int] = None
    triggered_at: Optional[datetime] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    duration_ms: Optional[int] = None
    created_at: Optional[datetime] = None
    error: Optional[Dict[str, Any]] = None
    error_message: Optional[str] = None
