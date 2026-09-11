from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Literal, Optional, Union

from typing_extensions import Required, TypedDict

if TYPE_CHECKING:
    from .cloud_config_params import CloudConfigParams
    from .self_hosted_config_params import SelfHostedConfigParams

__all__ = ["EnvironmentCreateParams"]


class EnvironmentCreateParams(TypedDict, total=False):
    name: Required[str]
    description: Optional[str]
    workspace_id: Optional[str]
    config: Union[CloudConfigParams, SelfHostedConfigParams]
    scope: Literal["organization", "account"]
    metadata: Dict[str, str]
    betas: List[str]
