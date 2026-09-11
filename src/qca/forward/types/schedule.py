from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .schedule_execution import ScheduleExecution
    from .schedule_initial_events_item import ScheduleInitialEventsItem
    from .schedule_paused_reason import SchedulePausedReason
    from .schedule_sinks_item import ScheduleSinksItem
    from .schedule_trigger_policy import ScheduleTriggerPolicy

__all__ = ["Schedule"]


class Schedule(BaseModel):
    id: Optional[str] = None
    identity_id: Optional[str] = None
    template_id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    initial_events: Optional[List[ScheduleInitialEventsItem]] = None
    execution: Optional[ScheduleExecution] = None
    trigger_policy: Optional[ScheduleTriggerPolicy] = None
    environment_id: Optional[str] = None
    sinks: Optional[List[ScheduleSinksItem]] = None
    metadata: Optional[Dict[str, Any]] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    archived_at: Optional[datetime] = None
    paused_reason: Optional[SchedulePausedReason] = None
