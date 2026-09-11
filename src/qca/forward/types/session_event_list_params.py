from __future__ import annotations

from typing import List, Optional

from typing_extensions import TypedDict

__all__ = ["SessionEventListParams"]


class SessionEventListParams(TypedDict, total=False):
    limit: Optional[int]
    after_id: Optional[str]
    before_id: Optional[str]
    order: Optional[str]
    type: Optional[str]
    types: List[str]
    include_tool_calls: Optional[bool]
    include_thinking: Optional[bool]
