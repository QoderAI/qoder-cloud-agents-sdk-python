from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Union

from typing_extensions import Required, TypedDict

if TYPE_CHECKING:
    from .always_allow_policy_param import AlwaysAllowPolicyParam
    from .always_ask_policy_param import AlwaysAskPolicyParam
    from .always_deny_policy_param import AlwaysDenyPolicyParam

__all__ = ["ImageSearchToolConfigParams"]


class ImageSearchToolConfigParams(TypedDict, total=False):
    name: Required[Literal["ImageSearch", "image_search"]]
    enabled: bool
    permission_policy: Union[AlwaysAllowPolicyParam, AlwaysAskPolicyParam, AlwaysDenyPolicyParam]
