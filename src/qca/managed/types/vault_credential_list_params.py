from __future__ import annotations

from typing import List, Optional

from typing_extensions import TypedDict

__all__ = ["VaultCredentialListParams"]


class VaultCredentialListParams(TypedDict, total=False):
    name: Optional[str]
    before_id: Optional[str]
    after_id: Optional[str]
    include_archived: Optional[bool]
    limit: Optional[int]
    page: Optional[str]
    workspace_id: Optional[str]
    betas: List[str]
