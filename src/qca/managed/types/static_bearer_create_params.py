from __future__ import annotations

from typing import Literal

from typing_extensions import Required, TypedDict

__all__ = ["StaticBearerCreateParams"]


class StaticBearerCreateParams(TypedDict, total=False):
    token: Required[str]
    mcp_server_url: Required[str]
    type: Required[Literal["static_bearer"]]
