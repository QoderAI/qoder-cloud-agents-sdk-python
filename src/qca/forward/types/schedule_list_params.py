from __future__ import annotations

from typing import Optional

from typing_extensions import TypedDict

__all__ = ["ScheduleListParams"]


class ScheduleListParams(TypedDict, total=False):
    identity_id: Optional[str]
    template_id: Optional[str]
    status: Optional[str]
    include_archived: Optional[bool]
    limit: Optional[int]
    after_id: Optional[str]
    before_id: Optional[str]
    sort_by: Optional[str]
    order: Optional[str]
