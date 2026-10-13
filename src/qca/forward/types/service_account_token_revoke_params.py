from __future__ import annotations

from datetime import datetime

from typing_extensions import Required, TypedDict

__all__ = ["ServiceAccountTokenRevokeParams"]


class ServiceAccountTokenRevokeParams(TypedDict, total=False):
    sa_key: Required[str]
    target_credential_id: str
    target_expires_at: str | datetime
    reason: str
