from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .send_session_events_data_union import SendSessionEventsDataUnion

__all__ = ["SendSessionEvents"]


class SendSessionEvents(BaseModel):
    data: Optional[List[SendSessionEventsDataUnion]] = None
