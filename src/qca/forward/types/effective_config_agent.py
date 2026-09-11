from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List, Optional, Union

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .effective_config_agent_tools_item import EffectiveConfigAgentToolsItem
    from .model_config import ModelConfig

__all__ = ["EffectiveConfigAgent"]


class EffectiveConfigAgent(BaseModel):
    model: Optional[Union[str, ModelConfig]] = None
    system: Optional[str] = None
    tools: Optional[List[EffectiveConfigAgentToolsItem]] = None
    mcp_servers: Optional[List[Dict[str, Any]]] = None
    skills: Optional[List[Dict[str, Any]]] = None
