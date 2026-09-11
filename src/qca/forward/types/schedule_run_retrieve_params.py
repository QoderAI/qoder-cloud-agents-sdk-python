from __future__ import annotations

from typing import Optional

from typing_extensions import TypedDict

__all__ = ["ScheduleRunRetrieveParams"]


class ScheduleRunRetrieveParams(TypedDict, total=False):
    identity_id: Optional[str]
