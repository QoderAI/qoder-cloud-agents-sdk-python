from __future__ import annotations

from typing import Literal, Optional

from typing_extensions import Required, TypedDict

__all__ = ["AgentParams"]


class AgentParams(TypedDict, total=False):
    id: Required[str]
    type: Required[Literal["agent"]]
    version: Optional[int]
