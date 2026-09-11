from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .tool_config import ToolConfig

__all__ = ["Tool"]


class Tool(BaseModel):
    type: Optional[str] = None
    enabled_tools: Optional[List[str]] = None
    disallowed_tools: Optional[List[str]] = None
    configs: Optional[List[ToolConfig]] = None
    mcp_server_name: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    input_schema: Optional[Dict[str, Any]] = None
