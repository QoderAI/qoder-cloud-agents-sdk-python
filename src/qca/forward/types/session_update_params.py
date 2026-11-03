from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional

from typing_extensions import TypedDict

if TYPE_CHECKING:
    from .budget_limit_param import BudgetLimitParam
    from .session_update_params_config_param import SessionUpdateParamsConfigParam

__all__ = ["SessionUpdateParams"]


class SessionUpdateParams(TypedDict, total=False):
    # Omit to keep the default/current budget; None clears it.
    budget: Optional[BudgetLimitParam]
    title: Optional[str]
    metadata: Dict[str, Any]
    config: SessionUpdateParamsConfigParam
    idempotency_key: Optional[str]
