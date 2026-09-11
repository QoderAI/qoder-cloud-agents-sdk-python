from __future__ import annotations

from typing import Optional

from typing_extensions import Required, TypedDict

__all__ = ["ModelConfigParam"]


class ModelConfigParam(TypedDict, total=False):
    id: Required[str]
    effort: Optional[str]
    context_window: Optional[int]
