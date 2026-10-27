from typing import Literal, Union

from typing_extensions import TypedDict

from qca.common._models import BaseModel


class TextOutcomeRubricParam(TypedDict):
    type: Literal["text"]
    content: str


class FileOutcomeRubricParam(TypedDict):
    type: Literal["file"]
    file_id: str


OutcomeRubricParam = Union[TextOutcomeRubricParam, FileOutcomeRubricParam]


class TextOutcomeRubric(BaseModel):
    type: Literal["text"]
    content: str


class FileOutcomeRubric(BaseModel):
    type: Literal["file"]
    file_id: str


OutcomeRubric = Union[TextOutcomeRubric, FileOutcomeRubric]
