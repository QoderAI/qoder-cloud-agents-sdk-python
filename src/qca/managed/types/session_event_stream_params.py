from __future__ import annotations

from typing import List, Literal, Optional

from typing_extensions import TypedDict

__all__ = ["SessionEventStreamParams"]


class SessionEventStreamParams(TypedDict, total=False):
    workspace_id: Optional[str]
    event_deltas: List[Literal["agent.message", "agent.thinking"]]
    betas: List[str]
