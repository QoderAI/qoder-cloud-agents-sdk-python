from __future__ import annotations

from typing import Dict, List

from typing_extensions import TypedDict

__all__ = ["FileSearchParams"]


class FileSearchParams(TypedDict, total=False):
    metadata: Dict[str, str]
    limit: int
    page: str
    name: str
    scope_id: str
    workspace_id: str
    betas: List[str]
