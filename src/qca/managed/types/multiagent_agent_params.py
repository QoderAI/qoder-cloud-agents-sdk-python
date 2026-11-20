from __future__ import annotations

from typing import Literal, Optional, Union

from typing_extensions import Required, TypedDict

__all__ = ["MultiagentAgentParams"]


class MultiagentAgentParams(TypedDict, total=False):
    id: Required[str]
    type: Required[Literal["agent"]]
    # A positive integer, "latest", or a positive integer string. Omit to pin the
    # latest numeric version at save time.
    version: Optional[Union[int, str]]
