from __future__ import annotations

from typing import Literal

from typing_extensions import Required, TypedDict

__all__ = ["TextBlockParam"]


class TextBlockParam(TypedDict, total=False):
    text: Required[str]
    type: Required[Literal["text"]]
