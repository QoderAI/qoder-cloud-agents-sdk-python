from __future__ import annotations

from typing import List, Optional

from typing_extensions import TypedDict

__all__ = ["FileListParams"]


class FileListParams(TypedDict, total=False):
    name: Optional[str]
    before_id: Optional[str]
    after_id: Optional[str]
    page: Optional[str]
    limit: Optional[int]
    scope_id: Optional[str]
    workspace_id: Optional[str]
    i_ds: List[str]
    betas: List[str]
