from __future__ import annotations

from typing import Literal, Optional

from typing_extensions import Required, TypedDict

__all__ = ["TokenEndpointAuthBasicUpdateParam"]


class TokenEndpointAuthBasicUpdateParam(TypedDict, total=False):
    type: Required[Literal["client_secret_basic"]]
    client_secret: Optional[str]
