from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .multiagent_agent_union import MultiagentAgentUnion

__all__ = ["Multiagent"]


class Multiagent(BaseModel):
    agents: Optional[List[MultiagentAgentUnion]] = None
    type: Optional[str] = None
