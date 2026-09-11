from __future__ import annotations

from typing import Literal

from typing_extensions import Required, TypedDict

__all__ = ["DreamModelConfigParam"]


class DreamModelConfigParam(TypedDict, total=False):
    id: Required[str]
    speed: Literal["standard", "fast"]
