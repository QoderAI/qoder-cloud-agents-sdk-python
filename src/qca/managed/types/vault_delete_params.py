from __future__ import annotations

from typing import List, Optional

from typing_extensions import TypedDict

__all__ = ["VaultDeleteParams"]


class VaultDeleteParams(TypedDict, total=False):
    workspace_id: Optional[str]
    betas: List[str]
