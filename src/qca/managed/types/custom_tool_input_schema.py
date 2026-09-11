from __future__ import annotations

from typing import Any, Dict, List, Literal, Optional

from qca.common._models import BaseModel

__all__ = ["CustomToolInputSchema"]


class CustomToolInputSchema(BaseModel):
    type: Optional[Literal["object"]] = None
    properties: Optional[Dict[str, Any]] = None
    required: Optional[List[str]] = None
