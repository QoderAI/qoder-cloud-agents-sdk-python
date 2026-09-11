from __future__ import annotations

from typing import Literal, Optional

from typing_extensions import Required, TypedDict

__all__ = ["TokenEndpointAuthPostUpdateParam"]


class TokenEndpointAuthPostUpdateParam(TypedDict, total=False):
    type: Required[Literal["client_secret_post"]]
    client_secret: Optional[str]
