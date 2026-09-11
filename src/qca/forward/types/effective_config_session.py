from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .effective_config_session_resources_item import EffectiveConfigSessionResourcesItem

__all__ = ["EffectiveConfigSession"]


class EffectiveConfigSession(BaseModel):
    environment_id: Optional[str] = None
    environment_variables: Optional[Dict[str, str]] = None
    vault_ids: Optional[List[str]] = None
    resources: Optional[List[EffectiveConfigSessionResourcesItem]] = None
