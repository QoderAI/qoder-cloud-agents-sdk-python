from __future__ import annotations

from typing import Literal, Optional

from typing_extensions import Required, TypedDict

__all__ = ["StaticBearerUpdateParams"]


class StaticBearerUpdateParams(TypedDict, total=False):
    type: Required[Literal["static_bearer"]]
    token: Optional[str]
