from __future__ import annotations

from typing import Literal

from typing_extensions import Required, TypedDict

__all__ = ["OutputBehaviorCreateNewParam"]


class OutputBehaviorCreateNewParam(TypedDict, total=False):
    type: Required[Literal["create_new"]]
