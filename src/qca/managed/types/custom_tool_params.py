from __future__ import annotations

from typing import TYPE_CHECKING, Literal

from typing_extensions import Required, TypedDict

if TYPE_CHECKING:
    from .custom_tool_input_schema_param import CustomToolInputSchemaParam

__all__ = ["CustomToolParams"]


class CustomToolParams(TypedDict, total=False):
    description: Required[str]
    input_schema: Required[CustomToolInputSchemaParam]
    name: Required[str]
    type: Required[Literal["custom"]]
