from __future__ import annotations

from typing import Optional

from typing_extensions import TypedDict

__all__ = ["FileListParams"]


class FileListParams(TypedDict, total=False):
    limit: Optional[int]
    page: Optional[str]
    after_id: Optional[str]
    before_id: Optional[str]
    name: Optional[str]
    scope_id: Optional[str]
