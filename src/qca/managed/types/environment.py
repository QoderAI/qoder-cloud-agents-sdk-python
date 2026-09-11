from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Literal, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .environment_config_union import EnvironmentConfigUnion

__all__ = ["Environment"]


class Environment(BaseModel):
    id: Optional[str] = None
    archived_at: Optional[str] = None
    config: Optional[EnvironmentConfigUnion] = None
    created_at: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, str]] = None
    name: Optional[str] = None
    type: Optional[Literal["environment"]] = None
    updated_at: Optional[str] = None
    scope: Optional[str] = None
