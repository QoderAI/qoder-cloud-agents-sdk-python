from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .bucket_storage import BucketStorage
    from .cloud_config_networking_union import CloudConfigNetworkingUnion
    from .packages import Packages

__all__ = ["EnvironmentConfigUnion"]


class EnvironmentConfigUnion(BaseModel):
    storage: Optional[BucketStorage] = None
    setup_script: Optional[str] = None
    networking: Optional[CloudConfigNetworkingUnion] = None
    packages: Optional[Packages] = None
    type: Optional[str] = None
