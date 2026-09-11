from __future__ import annotations

from typing import List, Optional

from typing_extensions import TypedDict

__all__ = ["SessionResourceUpdateParams"]


class SessionResourceUpdateParams(TypedDict, total=False):
    password: Optional[str]
    authorization_token: str
    workspace_id: Optional[str]
    betas: List[str]
