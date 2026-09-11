from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional

from typing_extensions import Required, TypedDict

if TYPE_CHECKING:
    from .identity_config_spec_param import IdentityConfigSpecParam

__all__ = ["IdentityConfigUpsertParams"]


class IdentityConfigUpsertParams(TypedDict, total=False):
    name: Optional[str]
    identity_config: Required[IdentityConfigSpecParam]
    metadata: Dict[str, Any]
    idempotency_key: Optional[str]
