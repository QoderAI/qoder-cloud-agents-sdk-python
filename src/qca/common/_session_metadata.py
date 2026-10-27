from __future__ import annotations

from typing import Any, Mapping

from qca._version import __version__

from ._types import NotGiven


def with_session_metadata(body: Mapping[str, Any]) -> dict[str, Any]:
    metadata = body.get("metadata")
    if metadata is None or isinstance(metadata, NotGiven):
        metadata = {}
    if not isinstance(metadata, Mapping):
        raise ValueError("session creation metadata must be a JSON object or null")
    merged = {key: value for key, value in metadata.items() if not isinstance(value, NotGiven)}
    for key, expected in {
        "__qca_sdk_created": "true",
        "__qca_sdk_language": "python",
        "__qca_sdk_version": __version__,
    }.items():
        if key in merged and (not isinstance(merged[key], str) or merged[key] != expected):
            raise ValueError(f"conflicting SDK metadata field: {key}")
        merged[key] = expected
    return {**body, "metadata": merged}
