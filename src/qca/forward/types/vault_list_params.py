from __future__ import annotations

from typing import Optional

from typing_extensions import TypedDict

__all__ = ["VaultListParams"]


class VaultListParams(TypedDict, total=False):
    limit: Optional[int]
    page: Optional[str]
    after_id: Optional[str]
    before_id: Optional[str]
    name: Optional[str]
