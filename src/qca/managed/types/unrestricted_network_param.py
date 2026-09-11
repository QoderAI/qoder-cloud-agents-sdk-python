from __future__ import annotations

from typing import Literal

from typing_extensions import TypedDict

__all__ = ["UnrestrictedNetworkParam"]


class UnrestrictedNetworkParam(TypedDict, total=False):
    type: Literal["unrestricted"]
