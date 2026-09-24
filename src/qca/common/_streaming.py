from __future__ import annotations

import json
from collections.abc import AsyncIterator, Iterator
from typing import Any, Generic, TypeVar

import httpx

from ._exceptions import APIConnectionError, APIError, APIResponseValidationError, APITimeoutError
from ._models import parse_response

T = TypeVar("T")


class SSEDecoder:
    def __init__(self) -> None:
        self.last_event_id: str | None = None
        self.event: str | None = None
        self.data: list[str] = []

    def decode(self, line: str) -> tuple[str | None, str] | None:
        if not line:
            result = (self.event, "\n".join(self.data)) if self.data else None
            self.event = None
            self.data = []
            return result
        if line.startswith(":"):
            return None
        field, _, value = line.partition(":")
        if value.startswith(" "):
            value = value[1:]
        if field == "data":
            self.data.append(value)
        elif field == "event":
            self.event = value
        elif field == "id" and "\x00" not in value:
            self.last_event_id = value
        return None


class BaseStream(Generic[T]):
    def __init__(self, response: httpx.Response, cast_to: Any, *, strict: bool = False) -> None:
        self.response = response
        self._cast_to = cast_to
        self._strict = strict
        self._decoder = SSEDecoder()
        self._last_event_id: str | None = None

    @property
    def last_event_id(self) -> str | None:
        return self._last_event_id

    def _parse(self, frame: tuple[str | None, str]) -> T:
        event_type, text = frame
        try:
            data = json.loads(text)
        except ValueError as exc:
            raise APIResponseValidationError(response=self.response, body=text) from exc
        if event_type == "error" or (isinstance(data, dict) and data.get("type") == "error"):
            error = data.get("error", data) if isinstance(data, dict) else data
            message = error.get("message", str(error)) if isinstance(error, dict) else str(error)
            raise APIError(message, request=self.response.request, body=data)
        if isinstance(data, dict):
            data = dict(data)
            if event_type:
                data.setdefault("type", event_type)
            if self._decoder.last_event_id:
                data.setdefault("id", self._decoder.last_event_id)
        result = parse_response(self._cast_to, data, self.response, strict=self._strict)
        # Checkpoint only after a complete frame is parsed, never on a partial ID.
        self._last_event_id = self._decoder.last_event_id
        return result


class Stream(BaseStream[T], Iterator[T]):
    def __init__(self, response: httpx.Response, cast_to: Any, *, strict: bool = False) -> None:
        super().__init__(response, cast_to, strict=strict)
        self._iterator = self._iter_events()

    def __next__(self) -> T:
        return next(self._iterator)

    def _iter_events(self) -> Iterator[T]:
        try:
            for line in self.response.iter_lines():
                frame = self._decoder.decode(line)
                if frame is None:
                    continue
                if frame[0] == "ping":
                    continue
                if frame[1] == "[DONE]":
                    return
                yield self._parse(frame)
        except httpx.TimeoutException as exc:
            raise APITimeoutError(request=self.response.request) from exc
        except httpx.TransportError as exc:
            raise APIConnectionError(request=self.response.request) from exc
        finally:
            self.close()

    def close(self) -> None:
        self.response.close()

    def __enter__(self) -> Stream[T]:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()


class AsyncStream(BaseStream[T], AsyncIterator[T]):
    def __init__(self, response: httpx.Response, cast_to: Any, *, strict: bool = False) -> None:
        super().__init__(response, cast_to, strict=strict)
        self._iterator = self._iter_events()

    async def __anext__(self) -> T:
        return await self._iterator.__anext__()

    async def _iter_events(self) -> AsyncIterator[T]:
        try:
            async for line in self.response.aiter_lines():
                frame = self._decoder.decode(line)
                if frame is None:
                    continue
                if frame[0] == "ping":
                    continue
                if frame[1] == "[DONE]":
                    return
                yield self._parse(frame)
        except httpx.TimeoutException as exc:
            raise APITimeoutError(request=self.response.request) from exc
        except httpx.TransportError as exc:
            raise APIConnectionError(request=self.response.request) from exc
        finally:
            await self.close()

    async def close(self) -> None:
        await self.response.aclose()

    async def __aenter__(self) -> AsyncStream[T]:
        return self

    async def __aexit__(self, *_: object) -> None:
        await self.close()
