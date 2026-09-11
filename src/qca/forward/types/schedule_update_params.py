from __future__ import annotations

from typing import Any, Dict, List, Optional

from typing_extensions import TypedDict

__all__ = ["ScheduleUpdateParams"]


class ScheduleUpdateParams(TypedDict, total=False):
    name: Optional[str]
    description: Optional[str]
    template_id: Optional[str]
    initial_events: List[Dict[str, Any]]
    execution: Dict[str, Any]
    trigger_policy: Optional[Dict[str, Any]]
    environment_id: Optional[str]
    sinks: Optional[List[Dict[str, Any]]]
    metadata: Dict[str, Any]
    idempotency_key: Optional[str]
