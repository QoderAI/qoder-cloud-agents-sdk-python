from __future__ import annotations

from typing import Literal

from typing_extensions import Required, TypedDict

__all__ = ["SearchResultContentParam"]


class SearchResultContentParam(TypedDict, total=False):
    text: Required[str]
    type: Required[Literal["text"]]
