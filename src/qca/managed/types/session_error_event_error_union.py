from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .session_error_event_error_union_retry_status import SessionErrorEventErrorUnionRetryStatus

__all__ = ["SessionErrorEventErrorUnion"]


class SessionErrorEventErrorUnion(BaseModel):
    message: Optional[str] = None
    retry_status: Optional[SessionErrorEventErrorUnionRetryStatus] = None
    type: Optional[str] = None
    mcp_server_name: Optional[str] = None
    credential_id: Optional[str] = None
    vault_id: Optional[str] = None
