from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from typing_extensions import TypedDict

__all__ = ["EnvironmentListParams"]


class EnvironmentListParams(TypedDict, total=False):
    created_at_gte: Optional[datetime]
    created_at_lte: Optional[datetime]
    page: Optional[str]
    include_archived: Optional[bool]
    limit: Optional[int]
    workspace_id: Optional[str]
    betas: List[str]
