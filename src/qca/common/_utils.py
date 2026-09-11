from __future__ import annotations

from datetime import date, datetime
from typing import Any, Mapping
from urllib.parse import quote

from pydantic import BaseModel

from ._types import NOT_GIVEN, NotGiven


def strip_not_given(value: Any) -> Any:
    if isinstance(value, BaseModel):
        value = value.model_dump(mode="json", by_alias=True, exclude_unset=True)
    if isinstance(value, Mapping):
        return {k: strip_not_given(v) for k, v in value.items() if not isinstance(v, NotGiven)}
    if isinstance(value, (list, tuple)):
        return [strip_not_given(v) for v in value if not isinstance(v, NotGiven)]
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    return value


def path_template(path: str, **params: str) -> str:
    for name, value in params.items():
        if not isinstance(value, str) or not value:
            raise ValueError(f"Expected a non-empty string for {name}")
        if value in (".", ".."):
            raise ValueError(f"Invalid path segment for {name}")
        path = path.replace("{" + name + "}", quote(value, safe=""))
    return path


def make_request_options(
    *,
    body: Mapping[str, Any],
    query: Mapping[str, Any],
    headers: Mapping[str, Any],
    extra_headers: Mapping[str, str] | None,
    extra_query: Mapping[str, Any] | None,
    extra_body: Mapping[str, Any] | None,
    timeout: Any = NOT_GIVEN,
) -> dict[str, Any]:
    # Preserve tuples and file objects until multipart encoding.
    return {
        "body": {**{k: v for k, v in body.items() if not isinstance(v, NotGiven)}, **(extra_body or {})},
        "query": strip_not_given({**query, **(extra_query or {})}),
        "headers": {
            **{k: v for k, v in headers.items() if not isinstance(v, NotGiven) and v is not None},
            **(extra_headers or {}),
        },
        "timeout": timeout,
    }


def query_pairs(query: Mapping[str, Any]) -> list[tuple[str, str]]:
    pairs: list[tuple[str, str]] = []

    def add(key: str, value: Any) -> None:
        if value is None or isinstance(value, NotGiven):
            return
        if isinstance(value, Mapping):
            for child, item in value.items():
                add(f"{key}[{child}]", item)
        elif isinstance(value, (list, tuple)):
            for item in value:
                add(key, item)
        else:
            pairs.append((key, str(value).lower() if isinstance(value, bool) else str(value)))

    for key, value in query.items():
        add(key, value)
    return pairs
