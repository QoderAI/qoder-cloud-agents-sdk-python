from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .deployment_paused_reason_error_union import DeploymentPausedReasonErrorUnion

__all__ = ["DeploymentPausedReasonUnion"]


class DeploymentPausedReasonUnion(BaseModel):
    type: Optional[str] = None
    error: Optional[DeploymentPausedReasonErrorUnion] = None
