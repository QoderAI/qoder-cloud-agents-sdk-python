from __future__ import annotations

from typing import List, Optional

from typing_extensions import Required, TypedDict

__all__ = ["ScheduleArchiveManyParams"]


class ScheduleArchiveManyParams(TypedDict, total=False):
    schedule_ids: Required[List[str]]
    idempotency_key: Optional[str]
