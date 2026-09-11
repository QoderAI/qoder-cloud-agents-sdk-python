from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from qca.common._models import BaseModel

if TYPE_CHECKING:
    from .search_result_citations import SearchResultCitations
    from .search_result_content import SearchResultContent

__all__ = ["UserCustomToolResultEventContentUnion"]


class UserCustomToolResultEventContentUnion(BaseModel):
    text: Optional[str] = None
    type: Optional[str] = None
    source: Optional[str] = None
    context: Optional[str] = None
    title: Optional[str] = None
    citations: Optional[SearchResultCitations] = None
    content: Optional[List[SearchResultContent]] = None
