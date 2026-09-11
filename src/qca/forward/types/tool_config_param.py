from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from typing_extensions import Required, TypedDict

if TYPE_CHECKING:
    from .permission_policy_param import PermissionPolicyParam

__all__ = ["ToolConfigParam"]


class ToolConfigParam(TypedDict, total=False):
    name: Required[str]
    enabled: Optional[bool]
    permission_policy: PermissionPolicyParam
