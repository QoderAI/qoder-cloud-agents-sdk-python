from __future__ import annotations

from typing import Optional

from typing_extensions import TypedDict

__all__ = ["SystemOverrideParam"]


class SystemOverrideParam(TypedDict, total=False):
    mode: Optional[str]
    content: Optional[str]
