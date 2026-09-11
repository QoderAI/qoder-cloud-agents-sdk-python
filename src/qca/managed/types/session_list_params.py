from __future__ import annotations

from datetime import datetime
from typing import List, Literal, Optional

from typing_extensions import TypedDict

__all__ = ["SessionListParams"]


class SessionListParams(TypedDict, total=False):
    agent_id: Optional[str]
    agent_version: Optional[int]
    created_at_gt: Optional[datetime]
    created_at_gte: Optional[datetime]
    created_at_lt: Optional[datetime]
    created_at_lte: Optional[datetime]
    deployment_id: Optional[str]
    include_archived: Optional[bool]
    limit: Optional[int]
    memory_store_id: Optional[str]
    page: Optional[str]
    workspace_id: Optional[str]
    order: Literal["asc", "desc"]
    statuses: List[str]
    betas: List[str]
