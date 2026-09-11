from __future__ import annotations

from typing import List, Optional

from typing_extensions import TypedDict

__all__ = ["ModelListParams"]


class ModelListParams(TypedDict, total=False):
    after_id: Optional[str]
    before_id: Optional[str]
    limit: Optional[int]
    workspace_id: Optional[str]
    betas: List[str]
