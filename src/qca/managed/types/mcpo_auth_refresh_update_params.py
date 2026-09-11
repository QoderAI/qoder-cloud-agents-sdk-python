from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Union

from typing_extensions import TypedDict

if TYPE_CHECKING:
    from .token_endpoint_auth_basic_update_param import TokenEndpointAuthBasicUpdateParam
    from .token_endpoint_auth_post_update_param import TokenEndpointAuthPostUpdateParam

__all__ = ["MCPOAuthRefreshUpdateParams"]


class MCPOAuthRefreshUpdateParams(TypedDict, total=False):
    refresh_token: Optional[str]
    scope: Optional[str]
    token_endpoint_auth: Union[TokenEndpointAuthBasicUpdateParam, TokenEndpointAuthPostUpdateParam]
