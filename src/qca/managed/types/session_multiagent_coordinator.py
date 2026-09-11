from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .session_multiagent_coordinator_agent_union import SessionMultiagentCoordinatorAgentUnion

__all__ = ["SessionMultiagentCoordinator"]


class SessionMultiagentCoordinator(BaseModel):
    agents: Optional[List[SessionMultiagentCoordinatorAgentUnion]] = None
    type: Optional[str] = None
