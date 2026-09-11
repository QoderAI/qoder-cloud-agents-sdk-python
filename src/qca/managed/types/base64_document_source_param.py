from __future__ import annotations

from typing import Literal

from typing_extensions import Required, TypedDict

__all__ = ["Base64DocumentSourceParam"]


class Base64DocumentSourceParam(TypedDict, total=False):
    data: Required[str]
    media_type: Required[str]
    type: Required[Literal["base64"]]
