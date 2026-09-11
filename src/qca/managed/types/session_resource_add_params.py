from __future__ import annotations

from typing import List, Literal, Optional

from typing_extensions import Required, TypedDict

__all__ = ["SessionResourceAddParams"]


class SessionResourceAddParams(TypedDict, total=False):
    file_id: Required[str]
    type: Required[Literal["file"]]
    mount_path: Optional[str]
    workspace_id: Optional[str]
    betas: List[str]
