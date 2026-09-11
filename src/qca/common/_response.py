from __future__ import annotations

from collections.abc import AsyncIterator, Iterator
from pathlib import Path
from typing import Any, Callable, Generic, TypeVar

import anyio
import httpx

from ._exceptions import APIConnectionError, APITimeoutError

T = TypeVar("T")


def read_response(response: httpx.Response) -> bytes:
    try:
        return response.read()
    except httpx.TimeoutException as exc:
        raise APITimeoutError(request=response.request) from exc
    except httpx.TransportError as exc:
        raise APIConnectionError(request=response.request) from exc


async def aread_response(response: httpx.Response) -> bytes:
    try:
        return await response.aread()
    except httpx.TimeoutException as exc:
        raise APITimeoutError(request=response.request) from exc
    except httpx.TransportError as exc:
        raise APIConnectionError(request=response.request) from exc


class APIResponse(Generic[T]):
    def __init__(self, response: httpx.Response, parse: Callable[[], T]) -> None:
        self.http_response = response
        self._parse = parse

    @property
    def headers(self) -> httpx.Headers:
        return self.http_response.headers

    @property
    def status_code(self) -> int:
        return self.http_response.status_code

    def parse(self) -> T:
        self.read()
        return self._parse()

    def read(self) -> bytes:
        return read_response(self.http_response)

    def iter_bytes(self, chunk_size: int | None = None) -> Iterator[bytes]:
        return self.http_response.iter_bytes(chunk_size)

    def iter_lines(self) -> Iterator[str]:
        return self.http_response.iter_lines()

    def close(self) -> None:
        self.http_response.close()


class AsyncAPIResponse(Generic[T]):
    def __init__(self, response: httpx.Response, parse: Callable[[], T]) -> None:
        self.http_response = response
        self._parse = parse

    @property
    def headers(self) -> httpx.Headers:
        return self.http_response.headers

    @property
    def status_code(self) -> int:
        return self.http_response.status_code

    async def parse(self) -> T:
        await self.read()
        return self._parse()

    async def read(self) -> bytes:
        return await aread_response(self.http_response)

    async def iter_bytes(self, chunk_size: int | None = None) -> AsyncIterator[bytes]:
        async for chunk in self.http_response.aiter_bytes(chunk_size):
            yield chunk

    async def iter_lines(self) -> AsyncIterator[str]:
        async for line in self.http_response.aiter_lines():
            yield line

    async def close(self) -> None:
        await self.http_response.aclose()


class BinaryAPIResponse:
    """A streaming download. Close it explicitly or use a context manager."""

    def __init__(self, response: httpx.Response) -> None:
        self.http_response = response

    @property
    def headers(self) -> httpx.Headers:
        return self.http_response.headers

    @property
    def status_code(self) -> int:
        return self.http_response.status_code

    def read(self) -> bytes:
        return read_response(self.http_response)

    def iter_bytes(self, chunk_size: int | None = None) -> Iterator[bytes]:
        return self.http_response.iter_bytes(chunk_size)

    def write_to_file(self, path: str | Path) -> None:
        try:
            with Path(path).open("wb") as output:
                for chunk in self.iter_bytes():
                    output.write(chunk)
        finally:
            self.close()

    def close(self) -> None:
        self.http_response.close()

    def __enter__(self) -> BinaryAPIResponse:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()


class AsyncBinaryAPIResponse:
    def __init__(self, response: httpx.Response) -> None:
        self.http_response = response

    @property
    def headers(self) -> httpx.Headers:
        return self.http_response.headers

    @property
    def status_code(self) -> int:
        return self.http_response.status_code

    async def read(self) -> bytes:
        return await aread_response(self.http_response)

    async def iter_bytes(self, chunk_size: int | None = None) -> AsyncIterator[bytes]:
        async for chunk in self.http_response.aiter_bytes(chunk_size):
            yield chunk

    async def write_to_file(self, path: str | Path) -> None:
        try:
            async with await anyio.open_file(path, "wb") as output:
                async for chunk in self.iter_bytes():
                    await output.write(chunk)
        finally:
            await self.close()

    async def close(self) -> None:
        await self.http_response.aclose()

    async def __aenter__(self) -> AsyncBinaryAPIResponse:
        return self

    async def __aexit__(self, *_: object) -> None:
        await self.close()


class RawResponseResource:
    def __init__(self, resource: Any, *, streaming: bool = False) -> None:
        self._resource = resource
        self._streaming = streaming

    def __getattr__(self, name: str) -> Any:
        resource = self._resource
        attr = getattr(resource, name)
        if not callable(attr):
            return RawResponseResource(attr, streaming=self._streaming)

        def wrapped(*args: Any, **kwargs: Any) -> Any:
            # A separate view carries the response mode, avoiding shared mutable
            # flags when the same client is used concurrently.
            view = type(resource)(resource._client._raw_response_view(streaming=self._streaming))

            def call() -> Any:
                return getattr(view, name)(*args, **kwargs)

            if self._streaming:
                manager = AsyncResponseContextManager if resource._client._is_async else ResponseContextManager
                return manager(call)
            return call()

        return wrapped


class ResponseContextManager:
    def __init__(self, request: Callable[[], Any]) -> None:
        self._request = request
        self.response: Any = None

    def __enter__(self) -> Any:
        self.response = self._request()
        return self.response

    def __exit__(self, *_: object) -> None:
        self.response.close()


class AsyncResponseContextManager:
    def __init__(self, request: Callable[[], Any]) -> None:
        self._request = request
        self.response: Any = None

    async def __aenter__(self) -> Any:
        self.response = await self._request()
        return self.response

    async def __aexit__(self, *_: object) -> None:
        await self.response.close()
