from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List, Optional, Union

from typing_extensions import TypedDict

if TYPE_CHECKING:
    from .agent_params import AgentParams
    from .budget_limit_param import BudgetLimitParam
    from .file_resource_params import FileResourceParams
    from .git_hub_repository_resource_params import GitHubRepositoryResourceParams
    from .memory_store_resource_param import MemoryStoreResourceParam
    from .schedule_params import ScheduleParams
    from .system_message_event_params import SystemMessageEventParams
    from .user_define_outcome_event_params import UserDefineOutcomeEventParams
    from .user_message_event_params import UserMessageEventParams

__all__ = ["DeploymentUpdateParams"]


class DeploymentUpdateParams(TypedDict, total=False):
    environment_variables: Optional[str]
    description: Optional[str]
    environment_id: Optional[str]
    name: Optional[str]
    workspace_id: Optional[str]
    metadata: Dict[str, Any]
    resources: List[Union[GitHubRepositoryResourceParams, FileResourceParams, MemoryStoreResourceParam]]
    vault_ids: List[str]
    agent: Union[str, AgentParams]
    budget: BudgetLimitParam
    initial_events: List[Union[UserMessageEventParams, UserDefineOutcomeEventParams, SystemMessageEventParams]]
    schedule: ScheduleParams
    betas: List[str]
