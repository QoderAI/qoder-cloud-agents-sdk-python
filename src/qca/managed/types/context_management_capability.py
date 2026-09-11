from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .capability_support import CapabilitySupport

__all__ = ["ContextManagementCapability"]


class ContextManagementCapability(BaseModel):
    clear_thinking_20251015: Optional[CapabilitySupport] = None
    clear_tool_uses_20250919: Optional[CapabilitySupport] = None
    compact_20260112: Optional[CapabilitySupport] = None
    supported: Optional[bool] = None
