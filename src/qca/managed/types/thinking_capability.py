from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .thinking_types import ThinkingTypes

__all__ = ["ThinkingCapability"]


class ThinkingCapability(BaseModel):
    supported: Optional[bool] = None
    types: Optional[ThinkingTypes] = None
