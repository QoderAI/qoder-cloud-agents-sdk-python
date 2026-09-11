from __future__ import annotations

from typing import Optional

from typing_extensions import Required, TypedDict

__all__ = ["EnvironmentVariableOverrideParam"]


class EnvironmentVariableOverrideParam(TypedDict, total=False):
    op: Required[str]
    value: Optional[str]
