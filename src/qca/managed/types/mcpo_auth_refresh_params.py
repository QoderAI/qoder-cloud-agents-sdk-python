from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Union

from typing_extensions import Required, TypedDict

if TYPE_CHECKING:
    from .token_endpoint_auth_basic_param import TokenEndpointAuthBasicParam
    from .token_endpoint_auth_none_param import TokenEndpointAuthNoneParam
    from .token_endpoint_auth_post_param import TokenEndpointAuthPostParam

__all__ = ["MCPOAuthRefreshParams"]


class MCPOAuthRefreshParams(TypedDict, total=False):
    client_id: Required[str]
    refresh_token: Required[str]
    token_endpoint: Required[str]
    token_endpoint_auth: Required[
        Union[TokenEndpointAuthNoneParam, TokenEndpointAuthBasicParam, TokenEndpointAuthPostParam]
    ]
    resource: Optional[str]
    scope: Optional[str]
