from __future__ import annotations

from typing import Literal

from typing_extensions import TypedDict

__all__ = ["SelfHostedConfigParams"]


class SelfHostedConfigParams(TypedDict, total=False):
    # Runs on start/resume; self-hosted execution depends on the worker.
    startup_script: str
    setup_script: str
    type: Literal["self_hosted"]
