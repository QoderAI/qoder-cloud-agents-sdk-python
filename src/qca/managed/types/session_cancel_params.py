from typing import List

from typing_extensions import TypedDict


class SessionCancelParams(TypedDict, total=False):
    workspace_id: str
    betas: List[str]
