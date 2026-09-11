from __future__ import annotations

from typing import List, Optional

from typing_extensions import TypedDict

__all__ = ["IdentityListParams"]


class IdentityListParams(TypedDict, total=False):
    external_id: Optional[str]
    identity_i_ds: List[str]
    search: Optional[str]
    enabled: Optional[bool]
    limit: Optional[int]
    after_id: Optional[str]
    before_id: Optional[str]
