from __future__ import annotations

from typing import Literal

from typing_extensions import Required, TypedDict

__all__ = ["MonetaryAmountParam"]


class MonetaryAmountParam(TypedDict, total=False):
    amount: Required[str]
    currency: Required[Literal["USD"]]
