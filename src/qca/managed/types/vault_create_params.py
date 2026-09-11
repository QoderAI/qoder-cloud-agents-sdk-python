from __future__ import annotations

from typing import Dict, List, Optional

from typing_extensions import Required, TypedDict

__all__ = ["VaultCreateParams"]


class VaultCreateParams(TypedDict, total=False):
    display_name: Required[str]
    workspace_id: Optional[str]
    metadata: Dict[str, str]
    betas: List[str]
