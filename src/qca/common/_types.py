from __future__ import annotations

from os import PathLike
from typing import IO, Any, Mapping, Union


class NotGiven:
    """A missing argument, distinct from an explicitly supplied None."""

    def __bool__(self) -> bool:
        return False

    def __repr__(self) -> str:
        return "NOT_GIVEN"


NOT_GIVEN = NotGiven()
FileContent = Union[bytes, IO[bytes], PathLike[str]]
FileTypes = Union[
    FileContent,
    tuple[str, FileContent],
    tuple[str, FileContent, str],
    tuple[str, FileContent, str, Mapping[str, str]],
]
Body = Mapping[str, Any]
