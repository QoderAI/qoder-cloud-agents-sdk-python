from __future__ import annotations

from typing import Any

from typing_extensions import Required, TypedDict

__all__ = ["ServiceAccountTokenCreateParams"]


class ServiceAccountTokenCreateParams(TypedDict, total=False):
    # Request authentication only; not a JSON field.
    sa_key: Required[str]
    ttl_seconds: int
    metadata: dict[str, Any]
