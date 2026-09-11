from __future__ import annotations

from typing import Optional

from typing_extensions import TypedDict

__all__ = ["SessionThreadEventListParams"]


class SessionThreadEventListParams(TypedDict, total=False):
    limit: Optional[int]
    after_id: Optional[str]
    before_id: Optional[str]
