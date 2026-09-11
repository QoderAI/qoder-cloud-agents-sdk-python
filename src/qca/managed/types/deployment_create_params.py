from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Optional, Union

from typing_extensions import Required, TypedDict

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

__all__ = ["DeploymentCreateParams"]


class DeploymentCreateParams(TypedDict, total=False):
    environment_variables: Optional[str]
    agent: Required[Union[str, AgentParams]]
    environment_id: Required[str]
    initial_events: Required[
        List[Union[UserMessageEventParams, UserDefineOutcomeEventParams, SystemMessageEventParams]]
    ]
    name: Required[str]
    description: Optional[str]
    workspace_id: Optional[str]
    budget: BudgetLimitParam
    metadata: Dict[str, str]
    resources: List[Union[GitHubRepositoryResourceParams, FileResourceParams, MemoryStoreResourceParam]]
    schedule: ScheduleParams
    vault_ids: List[str]
    betas: List[str]
