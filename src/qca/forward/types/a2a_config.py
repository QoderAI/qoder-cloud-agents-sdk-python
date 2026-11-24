from __future__ import annotations

from typing import List, Optional

from qca.common._models import BaseModel

__all__ = ["A2AConfig", "A2ASkill"]


class A2ASkill(BaseModel):
    id: str
    name: str
    description: str
    tags: Optional[List[str]] = None
    examples: Optional[List[str]] = None


class A2AConfig(BaseModel):
    """Saved publication settings may be sparse; missing enabled means false."""

    enabled: Optional[bool] = None
    description: Optional[str] = None
    skills: Optional[List[A2ASkill]] = None
