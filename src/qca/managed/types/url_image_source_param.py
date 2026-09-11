from __future__ import annotations

from typing import Literal

from typing_extensions import Required, TypedDict

__all__ = ["URLImageSourceParam"]


class URLImageSourceParam(TypedDict, total=False):
    type: Required[Literal["url"]]
    url: Required[str]
