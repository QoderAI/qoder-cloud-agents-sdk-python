from __future__ import annotations

from typing import Optional

from typing_extensions import TypedDict

__all__ = ["IdentityClearParams"]


class IdentityClearParams(TypedDict, total=False):
    reason: Optional[str]
