from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .environment_config_packages import EnvironmentConfigPackages

__all__ = ["EnvironmentConfig"]


class EnvironmentConfig(BaseModel):
    setup_script: Optional[str] = None
    type: Optional[str] = None
    packages: Optional[EnvironmentConfigPackages] = None
