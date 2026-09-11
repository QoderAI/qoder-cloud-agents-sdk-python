from __future__ import annotations

from typing import Any, Dict, List, Literal

from typing_extensions import TypedDict

__all__ = ["CustomToolInputSchemaParam"]


class CustomToolInputSchemaParam(TypedDict, total=False):
    properties: Dict[str, Any]
    required: List[str]
    type: Literal["object"]
