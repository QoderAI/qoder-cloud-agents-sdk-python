from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .capability_support import CapabilitySupport
    from .context_management_capability import ContextManagementCapability
    from .effort_capability import EffortCapability
    from .thinking_capability import ThinkingCapability

__all__ = ["ModelCapabilities"]


class ModelCapabilities(BaseModel):
    batch: Optional[CapabilitySupport] = None
    citations: Optional[CapabilitySupport] = None
    code_execution: Optional[CapabilitySupport] = None
    context_management: Optional[ContextManagementCapability] = None
    effort: Optional[EffortCapability] = None
    image_input: Optional[CapabilitySupport] = None
    pdf_input: Optional[CapabilitySupport] = None
    structured_outputs: Optional[CapabilitySupport] = None
    thinking: Optional[ThinkingCapability] = None
