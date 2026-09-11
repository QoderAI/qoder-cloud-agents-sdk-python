from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Optional, Union

from typing_extensions import TypedDict

if TYPE_CHECKING:
    from .always_allow_policy_param import AlwaysAllowPolicyParam
    from .always_ask_policy_param import AlwaysAskPolicyParam

__all__ = ["GrepToolConfigParams"]


class GrepToolConfigParams(TypedDict, total=False):
    enabled: Optional[bool]
    permission_policy: Union[AlwaysAllowPolicyParam, AlwaysAskPolicyParam]
    type: Literal["grep"]
    name: Literal["grep"]
