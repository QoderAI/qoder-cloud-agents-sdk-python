from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List, Literal, Optional, Union

from typing_extensions import TypedDict

if TYPE_CHECKING:
    from .cloud_config_params import CloudConfigParams
    from .self_hosted_config_params import SelfHostedConfigParams

__all__ = ["EnvironmentUpdateParams"]


class EnvironmentUpdateParams(TypedDict, total=False):
    description: Optional[str]
    name: Optional[str]
    workspace_id: Optional[str]
    config: Union[CloudConfigParams, SelfHostedConfigParams]
    scope: Literal["organization", "account"]
    metadata: Dict[str, Any]
    betas: List[str]
