from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SearchResultCitationsParam"]


class SearchResultCitationsParam(TypedDict, total=False):
    enabled: Required[bool]
