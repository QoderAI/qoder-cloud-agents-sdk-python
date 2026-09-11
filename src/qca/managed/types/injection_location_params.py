from __future__ import annotations

from typing import Optional

from typing_extensions import TypedDict

__all__ = ["InjectionLocationParams"]


class InjectionLocationParams(TypedDict, total=False):
    body: Optional[bool]
    header: Optional[bool]
