from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .capability_support import CapabilitySupport

__all__ = ["ThinkingTypes"]


class ThinkingTypes(BaseModel):
    adaptive: Optional[CapabilitySupport] = None
    enabled: Optional[CapabilitySupport] = None
