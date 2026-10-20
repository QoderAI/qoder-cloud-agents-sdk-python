from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .session_error_event_error_union_retry_status import SessionErrorEventErrorUnionRetryStatus

__all__ = ["SessionErrorEventErrorUnion"]


class SessionErrorEventErrorUnion(BaseModel):
    qoder_error_code: Optional[str] = None
    """Diagnostic only; use retry_status to determine retry behavior."""
    message: Optional[str] = None
    retry_status: Optional[SessionErrorEventErrorUnionRetryStatus] = None
    type: Optional[str] = None
    mcp_server_name: Optional[str] = None
    credential_id: Optional[str] = None
    vault_id: Optional[str] = None
