from __future__ import annotations

from typing import Literal

from typing_extensions import Required, TypedDict

__all__ = ["OutputBehaviorUpdateExistingParam"]


class OutputBehaviorUpdateExistingParam(TypedDict, total=False):
    memory_store_id: Required[str]
    type: Required[Literal["update_existing"]]
