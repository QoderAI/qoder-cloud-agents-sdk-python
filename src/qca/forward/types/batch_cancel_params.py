from __future__ import annotations

from typing import Optional

from typing_extensions import TypedDict

__all__ = ["BatchCancelParams"]


class BatchCancelParams(TypedDict, total=False):
    idempotency_key: Optional[str]
