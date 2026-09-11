from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List, Optional, Union

from typing_extensions import TypedDict

if TYPE_CHECKING:
    from .environment_variable_update_params import EnvironmentVariableUpdateParams
    from .mcpo_auth_update_params import MCPOAuthUpdateParams
    from .static_bearer_update_params import StaticBearerUpdateParams

__all__ = ["VaultCredentialUpdateParams"]


class VaultCredentialUpdateParams(TypedDict, total=False):
    workspace_id: Optional[str]
    metadata: Dict[str, Any]
    auth: Union[MCPOAuthUpdateParams, StaticBearerUpdateParams, EnvironmentVariableUpdateParams]
    betas: List[str]
