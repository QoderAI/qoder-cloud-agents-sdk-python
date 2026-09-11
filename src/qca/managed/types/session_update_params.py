from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List, Optional

from typing_extensions import TypedDict

if TYPE_CHECKING:
    from .budget_limit_param import BudgetLimitParam
    from .session_agent_update_param import SessionAgentUpdateParam

__all__ = ["SessionUpdateParams"]


class SessionUpdateParams(TypedDict, total=False):
    environment_variables: Dict[str, str]
    title: Optional[str]
    workspace_id: Optional[str]
    metadata: Dict[str, Any]
    agent: SessionAgentUpdateParam
    budget: BudgetLimitParam
    vault_ids: List[str]
    betas: List[str]
