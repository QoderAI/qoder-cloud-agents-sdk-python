from __future__ import annotations

from typing import Mapping


def sa_key_headers(sa_key: str, extra_headers: Mapping[str, str] | None) -> dict[str, str]:
    if not isinstance(sa_key, str) or not sa_key or any(ord(c) <= 0x20 or ord(c) == 0x7F for c in sa_key):
        raise ValueError("sa_key must be non-empty and contain no whitespace or control characters")
    # Remove case variants so an explicit Key wins over every request auth override.
    headers = {k: v for k, v in (extra_headers or {}).items() if k.lower() not in ("authorization", "content-type")}
    return {**headers, "Authorization": f"Bearer {sa_key}", "Content-Type": "application/json"}
