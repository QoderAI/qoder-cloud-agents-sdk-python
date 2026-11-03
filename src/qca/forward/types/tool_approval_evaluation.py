from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["ToolApprovalDecision", "ToolApprovalEvaluation"]


class ToolApprovalDecision(BaseModel):
    """Automatic decision; reason_code may be indeterminate or high_risk."""

    type: Optional[str] = None
    reason_code: Optional[str] = None


class ToolApprovalEvaluation(BaseModel):
    """Policy source (always_allow, always_ask, auto) and optional automatic decision."""

    type: Optional[str] = None
    evaluated_permission: Optional[ToolApprovalDecision] = None
