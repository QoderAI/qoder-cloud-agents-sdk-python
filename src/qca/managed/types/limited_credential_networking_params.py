from __future__ import annotations

from typing import List, Literal

from typing_extensions import Required, TypedDict

__all__ = ["LimitedCredentialNetworkingParams"]


class LimitedCredentialNetworkingParams(TypedDict, total=False):
    allowed_hosts: Required[List[str]]
    type: Required[Literal["limited"]]
