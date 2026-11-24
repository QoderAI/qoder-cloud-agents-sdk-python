from typing import Literal

from typing_extensions import TypedDict

__all__ = ["TemplateRetrieveAgentCardParams"]


class TemplateRetrieveAgentCardParams(TypedDict, total=False):
    identity_id: str
    """Runtime identity selector for PAT authentication. Omit with SAT."""
    a2a_version: Literal["0.3", "1.0"]
    """Sent as A2A-Version; omission uses the server's 0.3 default."""
