from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Union

from typing_extensions import TypedDict

__all__ = ["SessionSearchParams"]


class SessionSearchParams(TypedDict, total=False):
    metadata: Dict[str, str]
    limit: int
    page: str
    name: str
    order: Literal["desc", "asc"]
    include_archived: bool
    statuses: List[Literal["running", "idle", "rescheduling", "terminated"]]
    agent_id: str
    agent_version: int
    deployment_id: str
    memory_store_id: str
    created_at_gt: Union[datetime, str]
    created_at_gte: Union[datetime, str]
    created_at_lt: Union[datetime, str]
    created_at_lte: Union[datetime, str]
    workspace_id: str
    betas: List[str]
