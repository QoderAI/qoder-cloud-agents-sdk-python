from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .identity_template import IdentityTemplate

__all__ = ["IdentityListTemplatesResponse"]


class IdentityListTemplatesResponse(BaseModel):
    data: Optional[List[IdentityTemplate]] = None
