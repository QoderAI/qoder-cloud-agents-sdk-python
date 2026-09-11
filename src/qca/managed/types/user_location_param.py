from __future__ import annotations

from typing import Literal, Optional

from typing_extensions import TypedDict

__all__ = ["UserLocationParam"]


class UserLocationParam(TypedDict, total=False):
    city: Optional[str]
    country: Optional[str]
    region: Optional[str]
    timezone: Optional[str]
    type: Literal["approximate"]
