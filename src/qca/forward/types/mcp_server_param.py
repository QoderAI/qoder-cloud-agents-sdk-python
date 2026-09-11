from __future__ import annotations

from typing import Optional

from typing_extensions import Required, TypedDict

__all__ = ["MCPServerParam"]


class MCPServerParam(TypedDict, total=False):
    type: Optional[str]
    name: Required[str]
    url: Required[str]
