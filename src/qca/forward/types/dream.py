from datetime import datetime
from typing import List, Literal, Optional, Union

from typing_extensions import Required, TypedDict

from qca.common._models import BaseModel


class DreamMemoryStoreInputParam(TypedDict):
    type: Literal["memory_store"]
    memory_store_id: str


class DreamIdentityTemplateInputParam(TypedDict):
    type: Literal["identity_template"]
    identity_id: str
    template_id: str


class DreamSessionsInputParam(TypedDict):
    type: Literal["sessions"]
    session_ids: List[str]


DreamInputParam = Union[DreamMemoryStoreInputParam, DreamIdentityTemplateInputParam, DreamSessionsInputParam]


class DreamModelConfigParam(TypedDict, total=False):
    id: Required[str]
    effort: Literal["none", "low", "medium", "high", "xhigh", "max"]
    context_window: int


class DreamCreateParams(TypedDict, total=False):
    inputs: Required[List[DreamInputParam]]
    model: Union[str, DreamModelConfigParam, None]
    instructions: str


class DreamListParams(TypedDict, total=False):
    limit: int
    after_id: str
    before_id: str
    include_archived: bool


class DreamInput(BaseModel):
    type: str
    memory_store_id: Optional[str] = None
    identity_id: Optional[str] = None
    template_id: Optional[str] = None
    session_ids: Optional[List[str]] = None


class DreamModelConfig(BaseModel):
    id: str
    effort: Optional[str] = None
    context_window: Optional[int] = None


class DreamOutput(BaseModel):
    type: str
    memory_store_id: str
    files_touched: Optional[List[str]] = None


class DreamUsage(BaseModel):
    input_tokens: int
    output_tokens: int
    cache_creation_input_tokens: int
    cache_read_input_tokens: int


class DreamError(BaseModel):
    type: str
    code: Optional[str] = None
    message: str


class Dream(BaseModel):
    id: str
    type: Literal["dream"]
    status: str
    inputs: List[DreamInput]
    outputs: List[DreamOutput]
    model: DreamModelConfig
    instructions: str
    usage: DreamUsage
    error: Optional[DreamError] = None
    created_at: datetime
    ended_at: Optional[datetime] = None
    archived_at: Optional[datetime] = None
