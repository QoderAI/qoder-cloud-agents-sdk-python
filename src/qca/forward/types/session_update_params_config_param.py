from __future__ import annotations

from typing import Any, Dict

from typing_extensions import TypedDict

__all__ = ["SessionUpdateParamsConfigParam"]


class SessionUpdateParamsConfigParam(TypedDict, total=False):
    environment_variables: Dict[str, Any]
