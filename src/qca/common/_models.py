from __future__ import annotations

from datetime import date, datetime
from types import UnionType
from typing import Annotated, Any, Union, get_args, get_origin

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


def _construct_response(cast_to: Any, data: Any) -> Any:
    """Build nested response models, preserving values that don't fit the schema."""
    origin = get_origin(cast_to) or cast_to
    args = get_args(cast_to)
    if origin is Annotated:
        return _construct_response(args[0], data)
    if origin in (Union, UnionType):
        try:
            return TypeAdapter(cast_to).validate_python(data)
        except (ValidationError, ValueError):
            return _construct_response(args[0], data)
    if origin is dict and isinstance(data, dict):
        return {key: _construct_response(args[1] if args else Any, value) for key, value in data.items()}
    if origin is list and isinstance(data, list):
        return [_construct_response(args[0] if args else Any, item) for item in data]
    if isinstance(origin, type) and issubclass(origin, BaseModel):
        if isinstance(data, list):
            return [_construct_response(cast_to, item) if isinstance(item, dict) else item for item in data]
        if isinstance(data, dict):
            origin.model_rebuild()
            values = dict(data)
            missing = []
            for name, field in origin.model_fields.items():
                key = field.alias if field.alias in data else name
                if key in data:
                    values[key] = _construct_response(field.annotation, data[key])
                elif field.is_required():
                    missing.append(name)
            result = origin.model_construct(**values)
            # Missing required fields have a usable default but remain absent from fields_set.
            for name in missing:
                result.__dict__[name] = None
            return result
    if origin is float and isinstance(data, int):
        value = float(data)
        return value if value == data else data
    if origin in (datetime, date):
        try:
            return TypeAdapter(cast_to).validate_python(data)
        except (ValidationError, ValueError):
            pass
    return data


def parse_response(cast_to: Any, data: Any, response: Any, *, strict: bool = False) -> Any:
    if data is None or cast_to is None or cast_to is type(None):
        return None
    try:
        result = TypeAdapter(cast_to).validate_python(data) if strict else _construct_response(cast_to, data)
    except (ValidationError, ValueError) as exc:
        raise APIResponseValidationError(response=response, body=data) from exc
    if isinstance(result, BaseModel):
        result._request_id = response.headers.get("x-request-id") or response.headers.get("request-id")
    return result
