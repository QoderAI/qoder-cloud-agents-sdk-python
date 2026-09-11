from __future__ import annotations

from typing import Optional

from typing_extensions import TypedDict

__all__ = ["IdentityConfigListParams"]


class IdentityConfigListParams(TypedDict, total=False):
    template_id: Optional[str]
    status: Optional[str]
    limit: Optional[int]
    after_id: Optional[str]
    before_id: Optional[str]
