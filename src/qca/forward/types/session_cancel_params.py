from __future__ import annotations

from typing import Optional

from typing_extensions import TypedDict

__all__ = ["SessionCancelParams"]


class SessionCancelParams(TypedDict, total=False):
    idempotency_key: Optional[str]
