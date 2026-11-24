from __future__ import annotations

from typing import Any, Dict, Optional, Union

from typing_extensions import Required, TypedDict

from .environment_config_param import EnvironmentConfigParam

__all__ = ["EnvironmentCreateParams"]


class EnvironmentCreateParams(TypedDict, total=False):
    identity_id: str
    """Select identity ownership with a PAT. Omit when using a SAT."""
    name: Required[str]
    description: Optional[str]
    config: Union[EnvironmentConfigParam, Dict[str, Any]]
    metadata: Dict[str, Any]
    idempotency_key: Optional[str]
