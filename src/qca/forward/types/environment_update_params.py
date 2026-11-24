from __future__ import annotations

from typing import Any, Dict, Optional, Union

from typing_extensions import TypedDict

from .environment_config_param import EnvironmentConfigParam

__all__ = ["EnvironmentUpdateParams"]


class EnvironmentUpdateParams(TypedDict, total=False):
    identity_id: str
    """Select identity ownership with a PAT. Omit when using a SAT."""
    name: Optional[str]
    description: Optional[str]
    config: Union[EnvironmentConfigParam, Dict[str, Any]]
    metadata: Dict[str, Any]
