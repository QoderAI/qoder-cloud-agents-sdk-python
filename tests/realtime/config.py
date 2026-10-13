from __future__ import annotations

from collections.abc import Mapping, Sequence
from pathlib import Path

from tests.support.harness import read_env


def realtime_environment(
    path: str | Path, environment: Mapping[str, str], selected: Sequence[tuple[str, str]]
) -> dict[str, str]:
    values = {**read_env(path), **environment}
    for flag in ("QODER_REALTIME_LIVE_ALLOW_WRITE", "QODER_REALTIME_LIVE_ALLOW_EXECUTION"):
        if values.get(flag) != "true":
            raise ValueError(f"{flag}=true is required")
    for region, auth_mode in selected:
        suffix = region.upper()
        names = [f"QODER_REALTIME_{suffix}_{auth_mode.upper()}_TEMPLATE_ID"]
        names.append(
            f"QODER_FORWARD_{suffix}_PAT"
            if auth_mode == "pat"
            else (
                f"QODER_REALTIME_{suffix}_SAT"
                if values.get(f"QODER_REALTIME_{suffix}_SAT", "").strip()
                else f"QODER_SA_{suffix}_KEY"
            )
        )
        for name in names:
            if not values.get(name, "").strip():
                raise ValueError(f"{name} is required")
    for region, _ in selected:
        pcm = (
            values.get(f"QODER_REALTIME_{region.upper()}_PCM_FILE")
            or values.get("QODER_REALTIME_PCM_FILE")
            or values.get("QODER_REALTIME_LIVE_PCM_FILE")
        )
        if pcm:
            path = Path(pcm)
            if not path.is_file() or not path.stat().st_size or path.stat().st_size % 2:
                raise ValueError("Realtime PCM fixture must contain complete, non-empty PCM16 samples")
            with path.open("rb") as stream:
                head = stream.read(12)
            if head[:4] == b"RIFF" and head[8:12] == b"WAVE":
                raise ValueError("Realtime PCM fixture must not include a WAV header")
    return values
