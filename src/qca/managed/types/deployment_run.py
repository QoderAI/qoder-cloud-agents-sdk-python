from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .agent_reference import AgentReference
    from .deployment_run_error_union import DeploymentRunErrorUnion
    from .trigger_context_union import TriggerContextUnion

__all__ = ["DeploymentRun"]


class DeploymentRun(BaseModel):
    id: Optional[str] = None
    agent: Optional[AgentReference] = None
    created_at: Optional[datetime] = None
    deployment_id: Optional[str] = None
    error: Optional[DeploymentRunErrorUnion] = None
    session_id: Optional[str] = None
    trigger_context: Optional[TriggerContextUnion] = None
    type: Optional[str] = None
