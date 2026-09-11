from __future__ import annotations

from typing import Literal

from typing_extensions import Required, TypedDict

__all__ = ["ScheduleParams"]


class ScheduleParams(TypedDict, total=False):
    expression: Required[str]
    timezone: Required[str]
    type: Required[Literal["cron"]]
