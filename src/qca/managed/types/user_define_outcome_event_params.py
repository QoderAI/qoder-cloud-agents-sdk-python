from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Optional, Union

from typing_extensions import Required, TypedDict

if TYPE_CHECKING:
    from .file_rubric_params import FileRubricParams
    from .text_rubric_params import TextRubricParams

__all__ = ["UserDefineOutcomeEventParams"]


class UserDefineOutcomeEventParams(TypedDict, total=False):
    description: Required[str]
    rubric: Required[Union[FileRubricParams, TextRubricParams]]
    type: Required[Literal["user.define_outcome"]]
    max_iterations: Optional[int]
