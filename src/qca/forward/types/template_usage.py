from typing import Literal

from qca.common._models import BaseModel


class TemplateUsage(BaseModel):
    type: Literal["template_usage"]
    template_id: str
    active_identities: int
    session_count: int
    active_seconds: float
    credits: float
