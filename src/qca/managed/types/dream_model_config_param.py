from typing import Literal

from typing_extensions import Required, TypedDict

__all__ = ["DreamModelConfigParam"]


class DreamModelConfigParam(TypedDict, total=False):
    id: Required[str]
    effort: Literal["none", "low", "medium", "high", "xhigh", "max"]
    context_window: int
