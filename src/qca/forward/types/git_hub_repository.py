from __future__ import annotations

from typing import Optional

from qca.common._models import BaseModel

__all__ = ["GitHubRepository"]


class GitHubRepository(BaseModel):
    url: Optional[str] = None
    mount_path: Optional[str] = None
    enabled: Optional[bool] = None
