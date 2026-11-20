from __future__ import annotations

from typing import TYPE_CHECKING, List, Literal, Union

from typing_extensions import Required, TypedDict

if TYPE_CHECKING:
    from .advisor_params import AdvisorParams
    from .multiagent_agent_params import MultiagentAgentParams
    from .multiagent_self_params import MultiagentSelfParams

__all__ = ["MultiagentParams"]


class MultiagentParams(TypedDict, total=False):
    agents: Required[List[Union[str, MultiagentAgentParams, MultiagentSelfParams, AdvisorParams]]]
    type: Required[Literal["coordinator"]]
