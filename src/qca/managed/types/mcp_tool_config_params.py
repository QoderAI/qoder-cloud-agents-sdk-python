from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Union

from typing_extensions import Required, TypedDict

if TYPE_CHECKING:
    from .always_allow_policy_param import AlwaysAllowPolicyParam
    from .always_ask_policy_param import AlwaysAskPolicyParam

__all__ = ["MCPToolConfigParams"]


class MCPToolConfigParams(TypedDict, total=False):
    name: Required[str]
    enabled: Optional[bool]
    permission_policy: Union[AlwaysAllowPolicyParam, AlwaysAskPolicyParam]
