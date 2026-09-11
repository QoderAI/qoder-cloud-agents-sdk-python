from __future__ import annotations

from typing import Optional

from typing_extensions import TypedDict

__all__ = ["MCPServerOverrideParam"]


class MCPServerOverrideParam(TypedDict, total=False):
    enabled: Optional[bool]
    type: Optional[str]
    url: Optional[str]
