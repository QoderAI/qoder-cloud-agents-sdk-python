from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .effective_config_agent import EffectiveConfigAgent
    from .effective_config_session import EffectiveConfigSession

__all__ = ["EffectiveConfig"]


class EffectiveConfig(BaseModel):
    type: Optional[str] = None
    agent_effective_hash: Optional[str] = None
    session_effective_hash: Optional[str] = None
    effective_hash: Optional[str] = None
    agent: Optional[EffectiveConfigAgent] = None
    session: Optional[EffectiveConfigSession] = None
    id: Optional[str] = None
    identity_id: Optional[str] = None
    template_id: Optional[str] = None
