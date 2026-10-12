from __future__ import annotations

from collections.abc import Mapping, Sequence
from pathlib import Path

from tests.support.harness import read_env


def sa_environment(
    path: str | Path, environment: Mapping[str, str], regions: Sequence[str], *, execution: bool
) -> dict[str, str]:
    values = {**read_env(path), **environment}
    for region in regions:
        name = "QODER_SA_CN_KEY" if region == "cn" else "QODER_SA_GLOBAL_KEY"
        if not values.get(name, "").strip():
            raise ValueError(f"{name} is required")
    if execution:
        for name in ("QODER_SA_LIVE_ALLOW_WRITE", "QODER_SA_LIVE_ALLOW_EXECUTION"):
            if values.get(name) != "true":
                raise ValueError(f"{name}=true is required")
    return values
