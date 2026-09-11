from __future__ import annotations

from typing import Literal, Optional

from typing_extensions import Required, TypedDict

__all__ = ["PreconditionParam"]


class PreconditionParam(TypedDict, total=False):
    type: Required[Literal["content_sha256"]]
    content_sha256: Optional[str]
