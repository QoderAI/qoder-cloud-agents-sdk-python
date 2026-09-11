from __future__ import annotations

from typing import TYPE_CHECKING, List, Literal, Optional, Union

from typing_extensions import TypedDict

if TYPE_CHECKING:
    from .always_allow_policy_param import AlwaysAllowPolicyParam
    from .always_ask_policy_param import AlwaysAskPolicyParam
    from .user_location_param import UserLocationParam

__all__ = ["WebSearchToolConfigParams"]


class WebSearchToolConfigParams(TypedDict, total=False):
    enabled: Optional[bool]
    permission_policy: Union[AlwaysAllowPolicyParam, AlwaysAskPolicyParam]
    allowed_domains: List[str]
    blocked_domains: List[str]
    type: Literal["web_search"]
    user_location: UserLocationParam
    name: Literal["web_search"]
