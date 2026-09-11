from __future__ import annotations

from typing import Optional

from typing_extensions import Required, TypedDict

__all__ = ["ScheduleRunListParams"]


class ScheduleRunListParams(TypedDict, total=False):
    identity_id: Required[str]
    schedule_id: Optional[str]
    status: Optional[str]
    trigger_type: Optional[str]
    has_error: Optional[bool]
    limit: Optional[int]
    after_id: Optional[str]
    before_id: Optional[str]
    sort_by: Optional[str]
    order: Optional[str]
