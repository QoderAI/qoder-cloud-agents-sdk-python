from __future__ import annotations

from typing import Literal

from typing_extensions import Required, TypedDict

__all__ = ["SystemContentBlockParam"]


class SystemContentBlockParam(TypedDict, total=False):
    text: Required[str]
    type: Required[Literal["text"]]
