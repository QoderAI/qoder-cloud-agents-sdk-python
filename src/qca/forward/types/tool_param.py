from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List, Optional

from typing_extensions import Required, TypedDict

if TYPE_CHECKING:
    from .tool_config_param import ToolConfigParam

__all__ = ["ToolParam"]


class ToolParam(TypedDict, total=False):
    type: Required[str]
    enabled_tools: List[str]
    disallowed_tools: List[str]
    configs: List[ToolConfigParam]
    mcp_server_name: Optional[str]
    name: Optional[str]
    description: Optional[str]
    input_schema: Dict[str, Any]
