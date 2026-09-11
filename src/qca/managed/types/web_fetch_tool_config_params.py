from __future__ import annotations

from typing import TYPE_CHECKING, List, Literal, Optional, Union

from typing_extensions import TypedDict

if TYPE_CHECKING:
    from .always_allow_policy_param import AlwaysAllowPolicyParam
    from .always_ask_policy_param import AlwaysAskPolicyParam

__all__ = ["WebFetchToolConfigParams"]


class WebFetchToolConfigParams(TypedDict, total=False):
    enabled: Optional[bool]
    max_content_tokens: Optional[int]
    permission_policy: Union[AlwaysAllowPolicyParam, AlwaysAskPolicyParam]
    allowed_domains: List[str]
    blocked_domains: List[str]
    type: Literal["web_fetch"]
    name: Literal["web_fetch"]
