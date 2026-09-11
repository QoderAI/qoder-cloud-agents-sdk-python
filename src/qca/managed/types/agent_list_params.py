from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from typing_extensions import TypedDict

__all__ = ["AgentListParams"]


class AgentListParams(TypedDict, total=False):
    created_at_gte: Optional[datetime]
    created_at_lte: Optional[datetime]
    include_archived: Optional[bool]
    limit: Optional[int]
    page: Optional[str]
    workspace_id: Optional[str]
    betas: List[str]
