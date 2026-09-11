from __future__ import annotations

from typing import Literal

from typing_extensions import Required, TypedDict

__all__ = ["PlainTextDocumentSourceParam"]


class PlainTextDocumentSourceParam(TypedDict, total=False):
    data: Required[str]
    media_type: Required[Literal["text/plain"]]
    type: Required[Literal["text"]]
