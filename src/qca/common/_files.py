from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from ._utils import strip_not_given


def file_tuple(value: Any) -> tuple[Any, ...]:
    if isinstance(value, tuple):
        name, content, *rest = value
    else:
        content, rest = value, []
        name = Path(value).name if isinstance(value, os.PathLike) else Path(getattr(value, "name", "upload")).name
    if isinstance(content, os.PathLike):
        content = Path(content).read_bytes()
    elif hasattr(content, "read"):
        content = content.read()
    if not isinstance(content, bytes):
        raise TypeError("File content must be bytes, a binary file, or a pathlib.Path")
    return (name, content, *rest)


def multipart_parts(body: dict[str, Any], file_fields: list[str]) -> list[tuple[str, Any]]:
    # Snapshot each upload once so retries replay the same bytes. File handles
    # supplied by callers remain open; Path inputs are opened and closed here.
    parts: list[tuple[str, Any]] = []
    for key, value in body.items():
        if key in file_fields and value is not None:
            values = value if isinstance(value, list) else [value]
            parts.extend((key, file_tuple(item)) for item in values)
        else:
            value = strip_not_given(value)
            text = value if isinstance(value, str) else json.dumps(value, ensure_ascii=False, separators=(",", ":"))
            parts.append((key, (None, text)))
    return parts
