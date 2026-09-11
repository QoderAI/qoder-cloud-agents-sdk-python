from __future__ import annotations

from typing import TYPE_CHECKING, List, Literal, Union

from typing_extensions import Required, TypedDict

if TYPE_CHECKING:
    from .agent_toolset_default_config_params import AgentToolsetDefaultConfigParams
    from .bash_tool_config_params import BashToolConfigParams
    from .edit_tool_config_params import EditToolConfigParams
    from .glob_tool_config_params import GlobToolConfigParams
    from .grep_tool_config_params import GrepToolConfigParams
    from .read_tool_config_params import ReadToolConfigParams
    from .web_fetch_tool_config_params import WebFetchToolConfigParams
    from .web_search_tool_config_params import WebSearchToolConfigParams
    from .write_tool_config_params import WriteToolConfigParams

__all__ = ["AgentToolset20260401Params"]


class AgentToolset20260401Params(TypedDict, total=False):
    disallowed_tools: List[str]
    enabled_tools: List[str]
    type: Required[Literal["agent_toolset_20260401"]]
    configs: List[
        Union[
            BashToolConfigParams,
            EditToolConfigParams,
            ReadToolConfigParams,
            WriteToolConfigParams,
            GlobToolConfigParams,
            GrepToolConfigParams,
            WebFetchToolConfigParams,
            WebSearchToolConfigParams,
        ]
    ]
    default_config: AgentToolsetDefaultConfigParams
