from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from typing_extensions import Required, TypedDict

if TYPE_CHECKING:
    from .session_event_param import SessionEventParam

__all__ = ["SessionEventSendParams"]


class SessionEventSendParams(TypedDict, total=False):
    events: Required[List[SessionEventParam]]
    idempotency_key: Optional[str]
