from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from typing_extensions import TypedDict

if TYPE_CHECKING:
    from .permission_policy_param import PermissionPolicyParam

__all__ = ["ToolOverrideParam"]


class ToolOverrideParam(TypedDict, total=False):
    enabled: Optional[bool]
    permission_policy: PermissionPolicyParam
