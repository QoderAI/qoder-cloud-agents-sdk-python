from typing import Literal, Optional

from typing_extensions import Required, TypedDict

from qca.common._models import BaseModel


class ScheduleFileResourceParam(TypedDict, total=False):
    type: Required[Literal["file"]]
    file_id: Required[str]
    mount_path: str


class ScheduleFileResource(BaseModel):
    type: Literal["file"]
    file_id: str
    mount_path: Optional[str] = None
