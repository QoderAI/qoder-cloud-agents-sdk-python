from __future__ import annotations

from typing import Optional

from typing_extensions import TypedDict

__all__ = ["SessionThreadEventStreamParams"]


class SessionThreadEventStreamParams(TypedDict, total=False):
    last_event_id: Optional[str]
