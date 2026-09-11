from __future__ import annotations

from typing import Literal

from typing_extensions import Required, TypedDict

__all__ = ["AdvisorParams"]


class AdvisorParams(TypedDict, total=False):
    model: Required[str]
    type: Required[Literal["advisor"]]
