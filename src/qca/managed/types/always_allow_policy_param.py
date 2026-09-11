from __future__ import annotations

from typing import Literal

from typing_extensions import Required, TypedDict

__all__ = ["AlwaysAllowPolicyParam"]


class AlwaysAllowPolicyParam(TypedDict, total=False):
    type: Required[Literal["always_allow"]]
