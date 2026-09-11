from __future__ import annotations

from typing import Any

from pydantic import BaseModel as PydanticBaseModel
from pydantic import ConfigDict, PrivateAttr, TypeAdapter, ValidationError

from ._exceptions import APIResponseValidationError


class BaseModel(PydanticBaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True, protected_namespaces=(), defer_build=True)
    _request_id: str | None = PrivateAttr(default=None)

    def to_dict(
        self, *, mode: str = "python", use_api_names: bool = True, exclude_unset: bool = True
    ) -> dict[str, Any]:
        return self.model_dump(mode=mode, by_alias=use_api_names, exclude_unset=exclude_unset)

    def to_json(self, *, indent: int | None = 2, use_api_names: bool = True, exclude_unset: bool = True) -> str:
        return self.model_dump_json(indent=indent, by_alias=use_api_names, exclude_unset=exclude_unset)


def parse_response(cast_to: Any, data: Any, response: Any) -> Any:
    if cast_to is None or cast_to is type(None):
        return None
    try:
        result = TypeAdapter(cast_to).validate_python(data)
    except (ValidationError, ValueError) as exc:
        raise APIResponseValidationError(response=response, body=data) from exc
    if isinstance(result, BaseModel):
        result._request_id = response.headers.get("x-request-id") or response.headers.get("request-id")
    return result
