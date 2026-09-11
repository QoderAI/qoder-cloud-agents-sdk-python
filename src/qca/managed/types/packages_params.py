from __future__ import annotations

from typing import List, Literal

from typing_extensions import TypedDict

__all__ = ["PackagesParams"]


class PackagesParams(TypedDict, total=False):
    apt: List[str]
    cargo: List[str]
    gem: List[str]
    go: List[str]
    npm: List[str]
    pip: List[str]
    type: Literal["packages"]
