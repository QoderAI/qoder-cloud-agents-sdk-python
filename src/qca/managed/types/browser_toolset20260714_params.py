from typing import Literal

from typing_extensions import Required, TypedDict

__all__ = ["BrowserToolset20260714Params"]


class BrowserToolset20260714Params(TypedDict, total=False):
    """Type-only toolset, gated by the browser-use-2026-07-14 beta header."""

    type: Required[Literal["browser_toolset_20260714"]]
