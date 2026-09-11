from __future__ import annotations

from typing import List, Optional

from typing_extensions import TypedDict

__all__ = ["AgentRetrieveParams"]


class AgentRetrieveParams(TypedDict, total=False):
    version: Optional[int]
    workspace_id: Optional[str]
    betas: List[str]
