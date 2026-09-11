from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Optional, Union

from typing_extensions import Required, TypedDict

if TYPE_CHECKING:
    from .base64_document_source_param import Base64DocumentSourceParam
    from .file_document_source_param import FileDocumentSourceParam
    from .plain_text_document_source_param import PlainTextDocumentSourceParam
    from .url_document_source_param import URLDocumentSourceParam

__all__ = ["DocumentBlockParam"]


class DocumentBlockParam(TypedDict, total=False):
    source: Required[
        Union[Base64DocumentSourceParam, PlainTextDocumentSourceParam, URLDocumentSourceParam, FileDocumentSourceParam]
    ]
    type: Required[Literal["document"]]
    context: Optional[str]
    title: Optional[str]
