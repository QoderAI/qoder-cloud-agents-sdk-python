from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["DeploymentPausedReasonErrorUnion"]


class DeploymentPausedReasonErrorUnion(BaseModel):
    type: Optional[str] = None
