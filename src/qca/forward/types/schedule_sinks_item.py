from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .schedule_sinks_item_target import ScheduleSinksItemTarget

__all__ = ["ScheduleSinksItem"]


class ScheduleSinksItem(BaseModel):
    type: Optional[str] = None
    channel_id: Optional[str] = None
    target: Optional[ScheduleSinksItemTarget] = None
