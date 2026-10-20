from __future__ import annotations

from typing import Literal

from typing_extensions import Required, TypedDict

__all__ = ["BudgetLimitParam"]


class BudgetLimitParam(TypedDict, total=False):
    # Positive decimal Credits, at most 12 integer and 2 fractional digits.
    max_credit_cost: Required[str]
    type: Required[Literal["limit"]]
