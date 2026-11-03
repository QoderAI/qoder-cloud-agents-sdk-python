from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List, Optional

from typing_extensions import Required, TypedDict

if TYPE_CHECKING:
    from .budget_limit_param import BudgetLimitParam
    from .session_create_params_config_param import SessionCreateParamsConfigParam
    from .session_resource_spec_param import SessionResourceSpecParam

__all__ = ["SessionCreateParams"]


class SessionCreateParams(TypedDict, total=False):
    # Omit to keep the default/current budget; None clears it.
    budget: Optional[BudgetLimitParam]
    identity_id: Required[str]
    template_id: Required[str]
    title: Optional[str]
    metadata: Dict[str, Any]
    config: SessionCreateParamsConfigParam
    resources: List[SessionResourceSpecParam]
    idempotency_key: Optional[str]
