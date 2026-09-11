from __future__ import annotations

from typing import Optional

from typing_extensions import TypedDict

__all__ = ["BatchListParams"]


class BatchListParams(TypedDict, total=False):
    status: Optional[str]
    limit: Optional[int]
    after_id: Optional[str]
    before_id: Optional[str]
