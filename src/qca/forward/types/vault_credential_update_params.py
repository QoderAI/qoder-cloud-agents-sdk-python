from typing import Any, Dict, Literal, Optional, Union

from typing_extensions import Required, TypedDict


class StaticBearerUpdate(TypedDict, total=False):
    type: Required[Literal["static_bearer"]]
    token: str


class EnvironmentVariableUpdate(TypedDict, total=False):
    type: Required[Literal["environment_variable"]]
    secret_value: str


class MCPOAuthRefreshUpdate(TypedDict, total=False):
    refresh_token: str
    scope: Optional[str]
    token_endpoint_auth: Dict[str, Any]


class MCPOAuthUpdate(TypedDict, total=False):
    type: Required[Literal["mcp_oauth"]]
    access_token: str
    expires_at: Optional[str]
    refresh: MCPOAuthRefreshUpdate


VaultCredentialUpdateAuth = Union[StaticBearerUpdate, EnvironmentVariableUpdate, MCPOAuthUpdate]


class VaultCredentialUpdateParams(TypedDict, total=False):
    """Merge patch. At least auth or metadata is required; null clears metadata."""

    auth: VaultCredentialUpdateAuth
    metadata: Optional[Dict[str, Any]]
    identity_id: str
