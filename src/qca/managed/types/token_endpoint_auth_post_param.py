from __future__ import annotations

from typing import Literal

from typing_extensions import Required, TypedDict

__all__ = ["TokenEndpointAuthPostParam"]


class TokenEndpointAuthPostParam(TypedDict, total=False):
    client_secret: Required[str]
    type: Required[Literal["client_secret_post"]]
