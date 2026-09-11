from __future__ import annotations

from typing import Literal

from typing_extensions import Required, TypedDict

__all__ = ["EffortXhighParam"]


class EffortXhighParam(TypedDict, total=False):
    type: Required[Literal["xhigh"]]
