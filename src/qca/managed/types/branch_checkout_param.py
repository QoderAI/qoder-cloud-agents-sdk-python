from __future__ import annotations

from typing import Literal

from typing_extensions import Required, TypedDict

__all__ = ["BranchCheckoutParam"]


class BranchCheckoutParam(TypedDict, total=False):
    name: Required[str]
    type: Required[Literal["branch"]]
