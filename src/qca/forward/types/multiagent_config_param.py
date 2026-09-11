from __future__ import annotations

from typing import TYPE_CHECKING, List

from typing_extensions import Required, TypedDict

if TYPE_CHECKING:
    from .multiagent_entry_param import MultiagentEntryParam

__all__ = ["MultiagentConfigParam"]


class MultiagentConfigParam(TypedDict, total=False):
    type: Required[str]
    agents: Required[List[MultiagentEntryParam]]
