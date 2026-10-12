from __future__ import annotations

import math
import os
import re
import threading
import time
from datetime import datetime
from email.utils import parsedate_to_datetime
from typing import Any, Literal, Sequence

import anyio
import httpx
from typing_extensions import Self

from ._exceptions import (
    APIConnectionError,
    APIError,
    APIResponseValidationError,
    APIStatusError,
    APITimeoutError,
    status_error,
)


class _ServiceAccountBase:
    def __init__(
        self,
        *,
        sa_key: str,
        region: Literal["cn", "global"],
        scopes: Sequence[str],
        ttl_seconds: int = 3600,
        timeout: float = 30,
    ) -> None:
        if not isinstance(sa_key, str) or not sa_key.strip():
            raise ValueError("sa_key must not be empty")
        if region not in ("cn", "global"):
            raise ValueError("region must be cn or global")
        if (
            isinstance(scopes, str)
            or not scopes
            or any(not isinstance(scope, str) or not scope or any(char.isspace() for char in scope) for scope in scopes)
        ):
            raise ValueError("scopes must be a nonempty sequence of scope names")
        if isinstance(ttl_seconds, bool) or not isinstance(ttl_seconds, int) or not 1 <= ttl_seconds <= 43200:
            raise ValueError("ttl_seconds must be an integer from 1 to 43200")
        if isinstance(timeout, bool) or not math.isfinite(timeout) or timeout <= 0:
            raise ValueError("exchange timeout must be positive and finite")
        self.region = region
        self._key = sa_key
        self._scope = " ".join(dict.fromkeys(scopes))
        self._ttl = ttl_seconds
        self._timeout = timeout
        host = "https://openapi.qoder.com.cn" if region == "cn" else "https://openapi.qoder.sh"
        self._url = host + "/api/v1/serviceToken/exchange"
        self._token: str | None = None
        self._refresh_at = self._safe_until = self._retry_at = 0.0
        self._failure: APIError | None = None
        self._transient = False
        self._closed = False

    def __repr__(self) -> str:
        return f"{type(self).__name__}(region={self.region!r}, credentials=redacted)"

    @classmethod
    def from_env(cls, *, region: Literal["cn", "global"], scopes: Sequence[str], **options: Any) -> Self:
        return cls(sa_key=os.environ.get("QODER_SA_KEY", ""), region=region, scopes=scopes, **options)

    def validate_region(self, host: str) -> None:
        expected = {"api.qoder.com": "global", "api.qoder.com.cn": "cn"}.get(host)
        if expected is not None and expected != self.region:
            raise ValueError("SA credential region does not match base_url")

    def _current(self) -> str | None:
        if self._closed:
            raise RuntimeError("Service account credential is closed")
        now = time.monotonic()
        if now < self._retry_at:
            return self._fallback()
        if self._token is not None and now < self._refresh_at:
            return self._token
        return None

    def _fallback(self) -> str:
        if self._transient and self._token is not None and time.monotonic() < self._safe_until:
            return self._token
        assert self._failure is not None
        raise self._failure from None

    def _redact(self, value: Any) -> str | None:
        if not isinstance(value, str):
            return None
        for secret in (self._key, self._token):
            if secret:
                value = value.replace(secret, "[redacted]")
        return value[:256]

    def _safe_request(self) -> httpx.Request:
        return httpx.Request("POST", self._url)

    def _decode(self, response: httpx.Response, started: float) -> str:
        try:
            body = response.json()
        except ValueError:
            body = {}
        safe_body: dict[str, Any] = {"message": "Service account token exchange failed"}
        if isinstance(body, dict):
            detail = body.get("error", body)
            if isinstance(detail, dict):
                safe_body["code"] = self._redact(detail.get("code"))
            safe_body["request_id"] = self._redact(body.get("request_id"))
        safe_response = httpx.Response(
            response.status_code,
            json=safe_body,
            request=self._safe_request(),
            headers={
                "x-request-id": self._redact(response.headers.get("x-request-id") or response.headers.get("request-id"))
                or ""
            },
        )
        if not response.is_success:
            raise status_error(safe_response)
        invalid = APIResponseValidationError(
            response=safe_response, body={"message": "Invalid token exchange response"}
        )
        if not isinstance(body, dict):
            raise invalid
        ttl = body.get("expires_in")
        if isinstance(ttl, str) and ttl.isascii() and ttl.isdecimal():
            ttl = int(ttl)
        if (
            not isinstance(body.get("access_token"), str)
            or not body["access_token"].strip()
            or not isinstance(body.get("token_type"), str)
            or body["token_type"].lower() != "bearer"
            or isinstance(ttl, bool)
            or not isinstance(ttl, int)
            or not 1 <= ttl <= 43200
        ):
            raise invalid
        if "expires_at" in body:
            try:
                if not isinstance(body["expires_at"], str) or not re.fullmatch(
                    r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})", body["expires_at"]
                ):
                    raise ValueError("invalid timestamp")
                expires_at = datetime.fromisoformat(body["expires_at"].replace("Z", "+00:00"))
                if expires_at.tzinfo is None:
                    raise ValueError("missing timezone")
            except (ValueError, TypeError, AttributeError):
                raise invalid from None
        safe_until = started + ttl - min(5, ttl * 0.05)
        if time.monotonic() >= safe_until:
            raise invalid
        self._token = body["access_token"]
        self._safe_until = safe_until
        self._refresh_at = started + ttl - min(60, ttl * 0.1)
        self._retry_at = 0
        self._failure = None
        return self._token

    def _record_failure(self, error: APIError, response: httpx.Response | None) -> str:
        self._failure = error
        self._transient = isinstance(error, APIConnectionError) or (
            isinstance(error, APIStatusError) and (error.status_code == 429 or error.status_code >= 500)
        )
        cooldown = 5.0
        if response is not None and response.status_code == 429:
            value = response.headers.get("retry-after", "")
            try:
                delay = float(value)
            except ValueError:
                try:
                    delay = parsedate_to_datetime(value).timestamp() - time.time()
                except (ValueError, TypeError, OverflowError):
                    delay = 0
            if math.isfinite(delay) and 0 < delay <= (2**31 - 1) / 1000:
                cooldown = max(cooldown, delay)
        self._retry_at = time.monotonic() + cooldown
        return self._fallback()

    def _exchange_args(self) -> dict[str, Any]:
        return dict(
            url=self._url,
            headers={"Authorization": f"Bearer {self._key}", "Accept": "application/json"},
            json={
                "grant_type": "client_credentials",
                "audience": "qoder",
                "scope": self._scope,
                "ttl_seconds": self._ttl,
            },
            timeout=self._timeout,
            follow_redirects=False,
            auth=None,
        )


class ServiceAccountCredential(_ServiceAccountBase):
    """Synchronous, lazy SAT cache. An injected HTTP client remains caller-owned."""

    def __init__(
        self,
        *,
        sa_key: str,
        region: Literal["cn", "global"],
        scopes: Sequence[str],
        ttl_seconds: int = 3600,
        timeout: float = 30,
        http_client: httpx.Client | None = None,
    ) -> None:
        super().__init__(sa_key=sa_key, region=region, scopes=scopes, ttl_seconds=ttl_seconds, timeout=timeout)
        if http_client is not None and not isinstance(http_client, httpx.Client):
            raise TypeError("http_client must be an httpx.Client")
        self._client = http_client or httpx.Client(timeout=timeout, follow_redirects=False)
        self._owns_client = http_client is None
        self._lock = threading.Lock()

    def get_token(self) -> str:
        with self._lock:
            current = self._current()
            if current is not None:
                return current
            response = None
            started = time.monotonic()
            try:
                response = self._client.post(**self._exchange_args())
                return self._decode(response, started)
            except httpx.TransportError as exc:
                cls = APITimeoutError if isinstance(exc, httpx.TimeoutException) else APIConnectionError
                error = cls(request=self._safe_request())
                return self._record_failure(error, response)
            except APIError as error:
                return self._record_failure(error, response)
            finally:
                if response is not None:
                    response.close()

    def close(self) -> None:
        with self._lock:
            self._closed = True
            if self._owns_client:
                self._client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()


class AsyncServiceAccountCredential(_ServiceAccountBase):
    """Async SAT cache shared on one event loop, using the caller's anyio backend.

    Cancelling the exchange owner releases the lock so another caller can exchange.
    Cancelling a waiter does not cancel the owner. No permanent task is created.
    """

    def __init__(
        self,
        *,
        sa_key: str,
        region: Literal["cn", "global"],
        scopes: Sequence[str],
        ttl_seconds: int = 3600,
        timeout: float = 30,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        super().__init__(sa_key=sa_key, region=region, scopes=scopes, ttl_seconds=ttl_seconds, timeout=timeout)
        if http_client is not None and not isinstance(http_client, httpx.AsyncClient):
            raise TypeError("http_client must be an httpx.AsyncClient")
        self._client = http_client or httpx.AsyncClient(timeout=timeout, follow_redirects=False)
        self._owns_client = http_client is None
        self._lock = anyio.Lock()

    async def get_token(self) -> str:
        async with self._lock:
            current = self._current()
            if current is not None:
                return current
            response = None
            started = time.monotonic()
            try:
                with anyio.fail_after(self._timeout):
                    response = await self._client.post(**self._exchange_args())
                return self._decode(response, started)
            except (httpx.TransportError, TimeoutError) as exc:
                cls = APITimeoutError if isinstance(exc, (httpx.TimeoutException, TimeoutError)) else APIConnectionError
                return self._record_failure(cls(request=self._safe_request()), response)
            except APIError as error:
                return self._record_failure(error, response)
            finally:
                if response is not None:
                    with anyio.CancelScope(shield=True):
                        await response.aclose()

    async def aclose(self) -> None:
        async with self._lock:
            self._closed = True
            if self._owns_client:
                await self._client.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, *_: object) -> None:
        await self.aclose()
