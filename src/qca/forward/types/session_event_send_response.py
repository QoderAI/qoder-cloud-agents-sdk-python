from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .session_event import SessionEvent

__all__ = ["SessionEventSendResponse"]


class SessionEventSendResponse(BaseModel):
    data: Optional[List[SessionEvent]] = None
