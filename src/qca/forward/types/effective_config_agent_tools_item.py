from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .effective_config_agent_tools_item_configs_item import EffectiveConfigAgentToolsItemConfigsItem

__all__ = ["EffectiveConfigAgentToolsItem"]


class EffectiveConfigAgentToolsItem(BaseModel):
    type: Optional[str] = None
    configs: Optional[List[EffectiveConfigAgentToolsItemConfigsItem]] = None
