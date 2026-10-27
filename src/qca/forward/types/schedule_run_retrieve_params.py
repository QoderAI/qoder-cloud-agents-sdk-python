from __future__ import annotations

from typing import Optional

from typing_extensions import TypedDict

__all__ = ["ScheduleRunRetrieveParams"]


class ScheduleRunRetrieveParams(TypedDict, total=False):
    include_initial_events: Optional[bool]
    identity_id: Optional[str]
