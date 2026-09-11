from __future__ import annotations

from typing import List, Optional

from typing_extensions import TypedDict

__all__ = ["SessionResourceListParams"]


class SessionResourceListParams(TypedDict, total=False):
    before_id: Optional[str]
    after_id: Optional[str]
    limit: Optional[int]
    page: Optional[str]
    workspace_id: Optional[str]
    betas: List[str]
