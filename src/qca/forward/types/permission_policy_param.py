from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PermissionPolicyParam"]


class PermissionPolicyParam(TypedDict, total=False):
    type: Required[str]
