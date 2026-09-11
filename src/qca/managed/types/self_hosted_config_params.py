from __future__ import annotations

from typing import Literal

from typing_extensions import TypedDict

__all__ = ["SelfHostedConfigParams"]


class SelfHostedConfigParams(TypedDict, total=False):
    type: Literal["self_hosted"]
