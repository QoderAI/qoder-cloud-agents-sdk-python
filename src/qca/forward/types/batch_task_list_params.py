from __future__ import annotations

from typing import Optional

from typing_extensions import TypedDict

__all__ = ["BatchTaskListParams"]


class BatchTaskListParams(TypedDict, total=False):
    status: Optional[str]
    custom_id: Optional[str]
    limit: Optional[int]
    after_id: Optional[str]
