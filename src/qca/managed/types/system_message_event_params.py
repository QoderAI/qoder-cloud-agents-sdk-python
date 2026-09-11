from __future__ import annotations

from typing import TYPE_CHECKING, List, Literal

from typing_extensions import Required, TypedDict

if TYPE_CHECKING:
    from .system_content_block_param import SystemContentBlockParam

__all__ = ["SystemMessageEventParams"]


class SystemMessageEventParams(TypedDict, total=False):
    content: Required[List[SystemContentBlockParam]]
    type: Required[Literal["system.message"]]
