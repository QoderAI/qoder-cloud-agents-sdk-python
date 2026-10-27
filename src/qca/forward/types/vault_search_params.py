from __future__ import annotations

from typing import Dict

from typing_extensions import TypedDict

__all__ = ["VaultSearchParams"]


class VaultSearchParams(TypedDict, total=False):
    metadata: Dict[str, str]
    limit: int
    page: str
    include_archived: bool
    name: str
    identity_id: str
