from typing import Literal

from qca.common._models import BaseModel


class SessionCancelResponse(BaseModel):
    id: str
    type: Literal["session"]
    status: Literal["canceling"]
