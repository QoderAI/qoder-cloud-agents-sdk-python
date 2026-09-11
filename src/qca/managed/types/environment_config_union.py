from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .cloud_config_networking_union import CloudConfigNetworkingUnion
    from .packages import Packages

__all__ = ["EnvironmentConfigUnion"]


class EnvironmentConfigUnion(BaseModel):
    networking: Optional[CloudConfigNetworkingUnion] = None
    packages: Optional[Packages] = None
    type: Optional[str] = None
