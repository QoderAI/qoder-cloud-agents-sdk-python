from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Union

from typing_extensions import TypedDict

__all__ = ["DeploymentSearchParams"]


class DeploymentSearchParams(TypedDict, total=False):
    metadata: Dict[str, str]
    limit: int
    page: str
    name: str
    status: Literal["active", "paused"]
    include_archived: bool
    agent_id: str
    created_at_gte: Union[datetime, str]
    created_at_lte: Union[datetime, str]
    workspace_id: str
    betas: List[str]
