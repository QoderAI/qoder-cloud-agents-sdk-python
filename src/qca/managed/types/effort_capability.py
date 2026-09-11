from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .capability_support import CapabilitySupport

__all__ = ["EffortCapability"]


class EffortCapability(BaseModel):
    high: Optional[CapabilitySupport] = None
    low: Optional[CapabilitySupport] = None
    max: Optional[CapabilitySupport] = None
    medium: Optional[CapabilitySupport] = None
    supported: Optional[bool] = None
    xhigh: Optional[CapabilitySupport] = None
