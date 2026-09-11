from __future__ import annotations

from typing import Literal

from typing_extensions import Required, TypedDict

__all__ = ["URLMCPServerParams"]


class URLMCPServerParams(TypedDict, total=False):
    name: Required[str]
    type: Required[Literal["url"]]
    url: Required[str]
