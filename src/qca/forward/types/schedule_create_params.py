from __future__ import annotations

from typing import Any, Dict, List, Optional

from typing_extensions import Required, TypedDict

__all__ = ["ScheduleCreateParams"]


class ScheduleCreateParams(TypedDict, total=False):
    identity_id: Required[str]
    template_id: Required[str]
    name: Required[str]
    description: Optional[str]
    initial_events: Required[List[Dict[str, Any]]]
    execution: Dict[str, Any]
    trigger_policy: Optional[Dict[str, Any]]
    environment_id: Required[str]
    sinks: Optional[List[Dict[str, Any]]]
    metadata: Dict[str, Any]
    idempotency_key: Optional[str]
