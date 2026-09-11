from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Dict, List, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .agent_reference import AgentReference
    from .budget_limit import BudgetLimit
    from .deployment_initial_event_union import DeploymentInitialEventUnion
    from .deployment_paused_reason_union import DeploymentPausedReasonUnion
    from .schedule import Schedule
    from .session_resource_config_union import SessionResourceConfigUnion

__all__ = ["Deployment"]


class Deployment(BaseModel):
    environment_variables: Optional[str] = None
    id: Optional[str] = None
    agent: Optional[AgentReference] = None
    archived_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    description: Optional[str] = None
    environment_id: Optional[str] = None
    initial_events: Optional[List[DeploymentInitialEventUnion]] = None
    metadata: Optional[Dict[str, str]] = None
    name: Optional[str] = None
    paused_reason: Optional[DeploymentPausedReasonUnion] = None
    resources: Optional[List[SessionResourceConfigUnion]] = None
    schedule: Optional[Schedule] = None
    status: Optional[str] = None
    type: Optional[str] = None
    updated_at: Optional[datetime] = None
    vault_ids: Optional[List[str]] = None
    budget: Optional[BudgetLimit] = None
