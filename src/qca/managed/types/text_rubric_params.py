from __future__ import annotations

from typing import Literal

from typing_extensions import Required, TypedDict

__all__ = ["TextRubricParams"]


class TextRubricParams(TypedDict, total=False):
    content: Required[str]
    type: Required[Literal["text"]]
