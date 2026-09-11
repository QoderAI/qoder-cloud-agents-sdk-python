from __future__ import annotations

from typing import Optional

from typing_extensions import TypedDict

__all__ = ["ScheduleUnpauseParams"]


class ScheduleUnpauseParams(TypedDict, total=False):
    idempotency_key: Optional[str]
