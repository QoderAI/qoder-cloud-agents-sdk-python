from __future__ import annotations

from typing import List, Optional

from typing_extensions import TypedDict

__all__ = ["SessionEventStreamParams"]


class SessionEventStreamParams(TypedDict, total=False):
    event_deltas: List[str]
    include_tool_calls: Optional[bool]
    include_thinking: Optional[bool]
    last_event_id: Optional[str]
