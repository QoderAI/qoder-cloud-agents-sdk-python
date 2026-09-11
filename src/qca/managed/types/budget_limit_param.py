from __future__ import annotations

from typing import TYPE_CHECKING, Literal

from typing_extensions import Required, TypedDict

if TYPE_CHECKING:
    from .monetary_amount_param import MonetaryAmountParam

__all__ = ["BudgetLimitParam"]


class BudgetLimitParam(TypedDict, total=False):
    max_list_cost: Required[MonetaryAmountParam]
    type: Required[Literal["limit"]]
