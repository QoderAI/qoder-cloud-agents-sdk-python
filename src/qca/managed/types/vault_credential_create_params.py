from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Optional, Union

from typing_extensions import Required, TypedDict

if TYPE_CHECKING:
    from .environment_variable_create_params import EnvironmentVariableCreateParams
    from .mcpo_auth_create_params import MCPOAuthCreateParams
    from .static_bearer_create_params import StaticBearerCreateParams

__all__ = ["VaultCredentialCreateParams"]


class VaultCredentialCreateParams(TypedDict, total=False):
    auth: Required[Union[MCPOAuthCreateParams, StaticBearerCreateParams, EnvironmentVariableCreateParams]]
    display_name: Optional[str]
    workspace_id: Optional[str]
    metadata: Dict[str, str]
    betas: List[str]
