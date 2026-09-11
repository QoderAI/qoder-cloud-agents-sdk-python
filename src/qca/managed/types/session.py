from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Dict, List, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .budget_limit import BudgetLimit
    from .outcome_evaluation_resource import OutcomeEvaluationResource
    from .session_agent import SessionAgent
    from .session_resource_union import SessionResourceUnion
    from .session_stats import SessionStats
    from .session_usage import SessionUsage

__all__ = ["Session"]


class Session(BaseModel):
    environment_variables: Optional[Dict[str, str]] = None
    id: Optional[str] = None
    agent: Optional[SessionAgent] = None
    archived_at: Optional[datetime] = None
    budget: Optional[BudgetLimit] = None
    created_at: Optional[datetime] = None
    environment_id: Optional[str] = None
    metadata: Optional[Dict[str, str]] = None
    outcome_evaluations: Optional[List[OutcomeEvaluationResource]] = None
    resources: Optional[List[SessionResourceUnion]] = None
    stats: Optional[SessionStats] = None
    status: Optional[str] = None
    title: Optional[str] = None
    type: Optional[str] = None
    updated_at: Optional[datetime] = None
    usage: Optional[SessionUsage] = None
    vault_ids: Optional[List[str]] = None
    deployment_id: Optional[str] = None
