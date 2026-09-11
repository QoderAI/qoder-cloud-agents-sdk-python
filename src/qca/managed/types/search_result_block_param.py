from __future__ import annotations

from typing import TYPE_CHECKING, List, Literal

from typing_extensions import Required, TypedDict

if TYPE_CHECKING:
    from .search_result_citations_param import SearchResultCitationsParam
    from .search_result_content_param import SearchResultContentParam

__all__ = ["SearchResultBlockParam"]


class SearchResultBlockParam(TypedDict, total=False):
    citations: Required[SearchResultCitationsParam]
    content: Required[List[SearchResultContentParam]]
    source: Required[str]
    title: Required[str]
    type: Required[Literal["search_result"]]
