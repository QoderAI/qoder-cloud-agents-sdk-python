from __future__ import annotations

from typing import List

from typing_extensions import TypedDict

__all__ = ["EnvironmentWorkAckParams"]


class EnvironmentWorkAckParams(TypedDict, total=False):
    betas: List[str]
