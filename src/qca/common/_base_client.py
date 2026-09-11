from __future__ import annotations

import inspect
import os
import random
import time
from email.utils import parsedate_to_datetime
from typing import Any, Mapping

import anyio
import httpx
from typing_extensions import Self

from qca._version import __version__

from ._exceptions import APIConnectionError, APIResponseValidationError, APITimeoutError, status_error
from ._files import multipart_parts
from ._models import parse_response
from ._response import (
    APIResponse,
    AsyncAPIResponse,
    AsyncBinaryAPIResponse,
    BinaryAPIResponse,
    aread_response,
    read_response,
)
from ._streaming import AsyncStream, Stream
from ._types import NOT_GIVEN, NotGiven
from ._utils import query_pairs, strip_not_given
from .credentials import AsyncCredential, Credential
from .pagination import AsyncPage, SyncPage

DEFAULT_TIMEOUT = httpx.Timeout(60.0, connect=10.0)


class BaseClient:
    _client: Any
    _default_base_url: str
    _base_url_env: str
    _raw_response = False
    _stream_response = False
    _is_async = False

    def _configure(
        self,
        *,
        access_token: str | None,
        base_url: str | httpx.URL | None,
        timeout: float | httpx.Timeout | None,
        max_retries: int,
        default_headers: Mapping[str, str] | None,
        default_query: Mapping[str, Any] | None,
        credential: Credential | AsyncCredential | None,
    ) -> None:
        if not isinstance(max_retries, int) or isinstance(max_retries, bool) or max_retries < 0:
            raise ValueError("max_retries must be a non-negative integer")
        self.access_token = access_token if access_token is not None else os.environ.get("QODER_PAT")
        self.credential = credential
        self.base_url = httpx.URL(base_url or os.environ.get(self._base_url_env) or self._default_base_url)
        if self.base_url.scheme not in ("http", "https") or not self.base_url.host or self.base_url.userinfo:
            raise ValueError("base_url must be an absolute HTTP(S) URL without credentials")
        if self.base_url.query or self.base_url.fragment:
            raise ValueError("base_url must not contain a query or fragment")
        if not self.base_url.path.endswith("/"):
            self.base_url = self.base_url.copy_with(path=self.base_url.path + "/")
        self.timeout = timeout
        self.max_retries = max_retries
        self.default_headers = dict(default_headers or {})
        self.default_query = dict(default_query or {})

    def _copy(self, *, raw: bool = False, streaming: bool = False, **overrides: Any) -> Self:
        options = dict(
            access_token=self.access_token,
            base_url=self.base_url,
            timeout=self.timeout,
            max_retries=self.max_retries,
            default_headers=self.default_headers,
            default_query=self.default_query,
            credential=self.credential,
            http_client=self._client,
        )
        options.update(overrides)
        client = type(self)(**options)
        client._raw_response = raw
        client._stream_response = streaming
        return client

    def with_options(
        self,
        *,
        access_token: str | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | NotGiven = NOT_GIVEN,
        default_query: Mapping[str, Any] | NotGiven = NOT_GIVEN,
    ) -> Self:
        values: dict[str, Any] = dict(
            access_token=access_token, base_url=base_url, timeout=timeout, max_retries=max_retries
        )
        if not isinstance(default_headers, NotGiven):
            values["default_headers"] = {**self.default_headers, **default_headers}
        if not isinstance(default_query, NotGiven):
            values["default_query"] = {**self.default_query, **default_query}
        return self._copy(**{k: v for k, v in values.items() if not isinstance(v, NotGiven)})

    def _raw_response_view(self, *, streaming: bool = False) -> Self:
        return self._copy(raw=True, streaming=streaming)

    def is_closed(self) -> bool:
        return self._client.is_closed

    def _headers(self, options: dict[str, Any], token: str | None) -> httpx.Headers:
        headers = httpx.Headers({"Accept": "application/json", "User-Agent": f"qca-python/{__version__}"})
        if token:
            headers["Authorization"] = f"Bearer {token}"
        for source in (self.default_headers, options.get("headers", {})):
            for key, value in source.items():
                headers[key] = ",".join(str(v) for v in value) if isinstance(value, (list, tuple)) else str(value)
        return headers

    def _request_args(
        self,
        method: str,
        path: str,
        options: dict[str, Any],
        token: str | None,
        file_fields: list[str] | None,
    ) -> dict[str, Any]:
        headers = self._headers(options, token)
        timeout = options.get("timeout", NOT_GIVEN)
        args = dict(
            method=method,
            url=self.base_url.join(path.lstrip("/")),
            headers=headers,
            params=query_pairs({**self.default_query, **options.get("query", {})}),
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
        )
        if file_fields:
            args["files"] = multipart_parts(options.get("body", {}), file_fields)
        elif method not in ("GET", "HEAD") and options.get("body") is not None:
            args["json"] = strip_not_given(options["body"])
        return args

    def _retryable(self, request: httpx.Request, response: httpx.Response | None) -> bool:
        safe = request.method in ("GET", "HEAD") or bool(request.headers.get("Idempotency-Key"))
        if response is None:
            return safe
        if response.status_code == 409:
            return False
        if not safe and response.status_code != 429:
            return False
        directive = response.headers.get("x-should-retry")
        if directive == "false":
            return False
        if directive == "true":
            return True
        return response.status_code in (408, 429) or response.status_code >= 500

    def _retry_delay(self, retry: int, response: httpx.Response | None) -> float:
        if response is not None:
            for header, divisor in (("retry-after-ms", 1000), ("retry-after", 1)):
                value = response.headers.get(header)
                if value is None:
                    continue
                try:
                    delay = float(value) / divisor
                except ValueError:
                    try:
                        delay = parsedate_to_datetime(value).timestamp() - time.time()
                    except (ValueError, TypeError, OverflowError):
                        continue
                if 0 <= delay <= 60:
                    return delay
        return min(0.5 * (2 ** min(retry, 10)), 8.0) * (1 - 0.25 * random.random())

    def _download_request(self, response: httpx.Response, data: Any) -> httpx.Request:
        try:
            url = httpx.URL(data["url"])
        except (KeyError, TypeError, ValueError) as exc:
            raise APIResponseValidationError(response=response, body=data) from exc
        if url.scheme not in ("http", "https") or not url.host or url.userinfo:
            raise APIResponseValidationError(response=response, body=data)
        # Construct directly: build_request would merge API client defaults and cookies.
        return httpx.Request("GET", url, extensions={"timeout": response.request.extensions.get("timeout", {})})

    def _data(self, response: httpx.Response) -> Any:
        if response.status_code == 204 or not response.content:
            return None
        try:
            return response.json()
        except ValueError as exc:
            raise APIResponseValidationError(response=response, body=response.text) from exc

    def _parse_api_response(
        self,
        response: httpx.Response,
        method: str,
        path: str,
        cast_to: Any,
        options: dict[str, Any],
        page_style: str | None,
    ) -> Any:
        if cast_to is None:
            return None
        data = self._data(response)
        if not page_style:
            return parse_response(cast_to, data, response)
        page_cls = AsyncPage if self._is_async else SyncPage
        page = parse_response(page_cls[cast_to], data, response)
        page._style = page_style
        page._query = {**self.default_query, **options.get("query", {})}
        client = self._copy() if self._raw_response else self
        page._fetch = lambda query: getattr(client, "request")(
            method, path, cast_to=cast_to, options={**options, "query": query}, page_style=page_style
        )
        return page


class SyncAPIClient(BaseClient):
    def __init__(
        self,
        *,
        access_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | httpx.Timeout | None = DEFAULT_TIMEOUT,
        max_retries: int = 2,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, Any] | None = None,
        http_client: httpx.Client | None = None,
        credential: Credential | None = None,
    ) -> None:
        self._configure(
            access_token=access_token,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            default_headers=default_headers,
            default_query=default_query,
            credential=credential,
        )
        if http_client is not None and not isinstance(http_client, httpx.Client):
            raise TypeError("http_client must be an httpx.Client")
        self._client = http_client or httpx.Client(timeout=timeout, follow_redirects=False)

    def _send(self, request: httpx.Request, *, storage: bool = False) -> httpx.Response:
        for attempt in range(self.max_retries + 1):
            if (
                not storage
                and self.credential
                and not self.access_token
                and "Authorization" not in self.default_headers
            ):
                # Dynamic credentials can rotate between retries. Explicit request
                # headers still take priority and are marked by request().
                if not request.extensions.get("qca_explicit_auth"):
                    request.headers["Authorization"] = f"Bearer {self.credential.get_token()}"
            try:
                response = self._client.send(request, stream=True, auth=None, follow_redirects=False)
            except httpx.TransportError as exc:
                if attempt < self.max_retries and self._retryable(request, None):
                    time.sleep(self._retry_delay(attempt, None))
                    continue
                cls = APITimeoutError if isinstance(exc, httpx.TimeoutException) else APIConnectionError
                raise cls(request=request) from exc
            if response.is_success:
                return response
            if attempt < self.max_retries and self._retryable(request, response):
                delay = self._retry_delay(attempt, response)
                response.close()
                time.sleep(delay)
                continue
            try:
                read_response(response)
                raise status_error(response)
            finally:
                response.close()
        raise AssertionError("Unreachable retry state")

    def request(
        self,
        method: str,
        path: str,
        *,
        cast_to: Any,
        options: dict[str, Any],
        page_style: str | None = None,
        stream: bool = False,
        binary: bool = False,
        download_link: bool = False,
        file_fields: list[str] | None = None,
    ) -> Any:
        args = self._request_args(method, path, options, self.access_token, file_fields)
        if stream:
            args["headers"]["Accept"] = "text/event-stream"
        request = self._client.build_request(**args)
        request.extensions["qca_explicit_auth"] = any(
            key.lower() == "authorization" for key in (*self.default_headers, *options.get("headers", {}))
        )
        # httpx multipart streams are single-use. Cache the encoded request once.
        request.read()
        response = self._send(request)
        if stream:
            return Stream(response, cast_to)
        if binary and not download_link:
            return BinaryAPIResponse(response)

        def parse() -> Any:
            return self._parse_api_response(response, method, path, cast_to, options, page_style)

        if self._stream_response and not binary:
            return APIResponse(response, parse)
        try:
            read_response(response)
            if binary:
                storage = self._download_request(response, self._data(response))
                return BinaryAPIResponse(self._send(storage, storage=True))

            return APIResponse(response, parse) if self._raw_response else parse()
        finally:
            response.close()

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()


class AsyncAPIClient(BaseClient):
    _is_async = True

    def __init__(
        self,
        *,
        access_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | httpx.Timeout | None = DEFAULT_TIMEOUT,
        max_retries: int = 2,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, Any] | None = None,
        http_client: httpx.AsyncClient | None = None,
        credential: Credential | AsyncCredential | None = None,
    ) -> None:
        self._configure(
            access_token=access_token,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            default_headers=default_headers,
            default_query=default_query,
            credential=credential,
        )
        if http_client is not None and not isinstance(http_client, httpx.AsyncClient):
            raise TypeError("http_client must be an httpx.AsyncClient")
        self._client = http_client or httpx.AsyncClient(timeout=timeout, follow_redirects=False)

    async def _send(self, request: httpx.Request, *, storage: bool = False) -> httpx.Response:
        for attempt in range(self.max_retries + 1):
            if (
                not storage
                and self.credential
                and not self.access_token
                and not request.extensions.get("qca_explicit_auth")
            ):
                token = self.credential.get_token()
                if inspect.isawaitable(token):
                    token = await token
                request.headers["Authorization"] = f"Bearer {token}"
            try:
                response = await self._client.send(request, stream=True, auth=None, follow_redirects=False)
            except httpx.TransportError as exc:
                if attempt < self.max_retries and self._retryable(request, None):
                    await anyio.sleep(self._retry_delay(attempt, None))
                    continue
                cls = APITimeoutError if isinstance(exc, httpx.TimeoutException) else APIConnectionError
                raise cls(request=request) from exc
            if response.is_success:
                return response
            if attempt < self.max_retries and self._retryable(request, response):
                delay = self._retry_delay(attempt, response)
                await response.aclose()
                await anyio.sleep(delay)
                continue
            try:
                await aread_response(response)
                raise status_error(response)
            finally:
                await response.aclose()
        raise AssertionError("Unreachable retry state")

    async def request(
        self,
        method: str,
        path: str,
        *,
        cast_to: Any,
        options: dict[str, Any],
        page_style: str | None = None,
        stream: bool = False,
        binary: bool = False,
        download_link: bool = False,
        file_fields: list[str] | None = None,
    ) -> Any:
        if file_fields:
            # Reading local file objects should not block the event loop.
            args = await anyio.to_thread.run_sync(
                lambda: self._request_args(method, path, options, self.access_token, file_fields)
            )
        else:
            args = self._request_args(method, path, options, self.access_token, None)
        if stream:
            args["headers"]["Accept"] = "text/event-stream"
        request = self._client.build_request(**args)
        request.extensions["qca_explicit_auth"] = any(
            key.lower() == "authorization" for key in (*self.default_headers, *options.get("headers", {}))
        )
        await request.aread()
        response = await self._send(request)
        if stream:
            return AsyncStream(response, cast_to)
        if binary and not download_link:
            return AsyncBinaryAPIResponse(response)

        def parse() -> Any:
            return self._parse_api_response(response, method, path, cast_to, options, page_style)

        if self._stream_response and not binary:
            return AsyncAPIResponse(response, parse)
        try:
            await aread_response(response)
            if binary:
                storage = self._download_request(response, self._data(response))
                return AsyncBinaryAPIResponse(await self._send(storage, storage=True))

            return AsyncAPIResponse(response, parse) if self._raw_response else parse()
        finally:
            await response.aclose()

    async def close(self) -> None:
        await self._client.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, *_: object) -> None:
        await self.close()
