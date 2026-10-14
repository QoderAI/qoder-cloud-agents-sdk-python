from __future__ import annotations

from typing import Any
from urllib.parse import quote_plus

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options
from qca.forward.types.drive import (
    DriveClearResponse,
    DriveDeleteEntryResponse,
    DriveDownloadURL,
    DriveListEntriesResponse,
    DriveUploadURL,
)


def _drive_query(pairs: list[tuple[str, str]]) -> str:
    # Only path uses literal slashes; opaque cursor values stay fully encoded.
    return "&".join(
        quote_plus(key) + "=" + quote_plus(value, safe="/" if key == "path" else "") for key, value in pairs
    )


class Drives(SyncAPIResource):
    """Persistent Identity files (Beta). Identity SATs also require identity_id."""

    def list_entries(
        self,
        *,
        identity_id: str,
        path: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        page_token: str | NotGiven = NOT_GIVEN,
        extra_headers: dict[str, str] | None = None,
        extra_query: dict[str, Any] | None = None,
        extra_body: dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DriveListEntriesResponse:
        """GET /drives/entries. Returns one page in service order; reuse next_page_token in the same scope/path."""
        options = make_request_options(
            body={},
            query={"identity_id": identity_id, "path": path, "limit": limit, "page_token": page_token},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        options["query_serializer"] = _drive_query
        return self._client.request("GET", "/drives/entries", cast_to=DriveListEntriesResponse, options=options)

    def create_upload_url(
        self,
        *,
        identity_id: str,
        path: str,
        content_type: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        extra_headers: dict[str, str] | None = None,
        extra_query: dict[str, Any] | None = None,
        extra_body: dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DriveUploadURL:
        """POST /drives/upload-url. Use only the returned headers when uploading; do not send API credentials to storage."""
        options = make_request_options(
            body={"path": path, "content_type": content_type},
            query={"identity_id": identity_id},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", "/drives/upload-url", cast_to=DriveUploadURL, options=options)

    def create_download_url(
        self,
        *,
        identity_id: str,
        path: str,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        extra_headers: dict[str, str] | None = None,
        extra_query: dict[str, Any] | None = None,
        extra_body: dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DriveDownloadURL:
        """POST /drives/download-url. Use a new Idempotency-Key or omit it to refresh expiry; replay does not renew it."""
        options = make_request_options(
            body={"path": path},
            query={"identity_id": identity_id},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", "/drives/download-url", cast_to=DriveDownloadURL, options=options)

    def delete_entry(
        self,
        *,
        identity_id: str,
        path: str,
        recursive: bool | NotGiven = NOT_GIVEN,
        extra_headers: dict[str, str] | None = None,
        extra_query: dict[str, Any] | None = None,
        extra_body: dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DriveDeleteEntryResponse:
        """DELETE /drives/entries. Nonempty directories require recursive=True. Partial failures retain error.deleted_count."""
        options = make_request_options(
            body={"path": path, "recursive": recursive},
            query={"identity_id": identity_id},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("DELETE", "/drives/entries", cast_to=DriveDeleteEntryResponse, options=options)

    def clear(
        self,
        *,
        identity_id: str,
        extra_headers: dict[str, str] | None = None,
        extra_query: dict[str, Any] | None = None,
        extra_body: dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DriveClearResponse:
        """DELETE /drives. Deletes all files in the selected Identity Drive."""
        options = make_request_options(
            body={},
            query={"identity_id": identity_id},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if extra_body is None:
            options["body"] = None
        return self._client.request("DELETE", "/drives", cast_to=DriveClearResponse, options=options)


class AsyncDrives(AsyncAPIResource):
    """Persistent Identity files (Beta). Identity SATs also require identity_id."""

    async def list_entries(
        self,
        *,
        identity_id: str,
        path: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        page_token: str | NotGiven = NOT_GIVEN,
        extra_headers: dict[str, str] | None = None,
        extra_query: dict[str, Any] | None = None,
        extra_body: dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DriveListEntriesResponse:
        """GET /drives/entries. Returns one page in service order; reuse next_page_token in the same scope/path."""
        options = make_request_options(
            body={},
            query={"identity_id": identity_id, "path": path, "limit": limit, "page_token": page_token},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        options["query_serializer"] = _drive_query
        return await self._client.request("GET", "/drives/entries", cast_to=DriveListEntriesResponse, options=options)

    async def create_upload_url(
        self,
        *,
        identity_id: str,
        path: str,
        content_type: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        extra_headers: dict[str, str] | None = None,
        extra_query: dict[str, Any] | None = None,
        extra_body: dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DriveUploadURL:
        """POST /drives/upload-url. Use only the returned headers when uploading; do not send API credentials to storage."""
        options = make_request_options(
            body={"path": path, "content_type": content_type},
            query={"identity_id": identity_id},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", "/drives/upload-url", cast_to=DriveUploadURL, options=options)

    async def create_download_url(
        self,
        *,
        identity_id: str,
        path: str,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        extra_headers: dict[str, str] | None = None,
        extra_query: dict[str, Any] | None = None,
        extra_body: dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DriveDownloadURL:
        """POST /drives/download-url. Use a new Idempotency-Key or omit it to refresh expiry; replay does not renew it."""
        options = make_request_options(
            body={"path": path},
            query={"identity_id": identity_id},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", "/drives/download-url", cast_to=DriveDownloadURL, options=options)

    async def delete_entry(
        self,
        *,
        identity_id: str,
        path: str,
        recursive: bool | NotGiven = NOT_GIVEN,
        extra_headers: dict[str, str] | None = None,
        extra_query: dict[str, Any] | None = None,
        extra_body: dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DriveDeleteEntryResponse:
        """DELETE /drives/entries. Nonempty directories require recursive=True. Partial failures retain error.deleted_count."""
        options = make_request_options(
            body={"path": path, "recursive": recursive},
            query={"identity_id": identity_id},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request(
            "DELETE", "/drives/entries", cast_to=DriveDeleteEntryResponse, options=options
        )

    async def clear(
        self,
        *,
        identity_id: str,
        extra_headers: dict[str, str] | None = None,
        extra_query: dict[str, Any] | None = None,
        extra_body: dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DriveClearResponse:
        """DELETE /drives. Deletes all files in the selected Identity Drive."""
        options = make_request_options(
            body={},
            query={"identity_id": identity_id},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if extra_body is None:
            options["body"] = None
        return await self._client.request("DELETE", "/drives", cast_to=DriveClearResponse, options=options)
