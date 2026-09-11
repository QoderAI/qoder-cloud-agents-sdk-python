from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List, Literal, Optional

from typing_extensions import TypedDict

if TYPE_CHECKING:
    from .precondition_param import PreconditionParam

__all__ = ["MemoryStoreMemoryUpdateParams"]


class MemoryStoreMemoryUpdateParams(TypedDict, total=False):
    content_sha256: Optional[str]
    metadata: Dict[str, Any]
    content: Optional[str]
    path: Optional[str]
    workspace_id: Optional[str]
    view: Literal["basic", "full"]
    precondition: PreconditionParam
    betas: List[str]
