from __future__ import annotations

from typing import List, Literal, Optional

from typing_extensions import TypedDict

__all__ = ["SessionThreadEventStreamParams"]


class SessionThreadEventStreamParams(TypedDict, total=False):
    last_event_id: Optional[str]
    workspace_id: Optional[str]
    event_deltas: List[Literal["agent.message", "agent.thinking"]]
    betas: List[str]
