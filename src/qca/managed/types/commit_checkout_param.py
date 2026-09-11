from __future__ import annotations

from typing import Literal

from typing_extensions import Required, TypedDict

__all__ = ["CommitCheckoutParam"]


class CommitCheckoutParam(TypedDict, total=False):
    sha: Required[str]
    type: Required[Literal["commit"]]
