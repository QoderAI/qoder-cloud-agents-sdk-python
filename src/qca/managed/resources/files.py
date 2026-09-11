from __future__ import annotations

from typing import Any, Dict, List, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._response import AsyncBinaryAPIResponse, BinaryAPIResponse
from qca.common._types import NOT_GIVEN, FileTypes, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.managed.types.deleted_file import DeletedFile
from qca.managed.types.file_metadata import FileMetadata

__all__ = ["Files", "AsyncFiles"]


class Files(SyncAPIResource):
    def list(
        self,
        *,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        scope_id: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        i_ds: Union[List[str], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[FileMetadata]:
        """GET /files."""
        _path = path_template("/files")
        options = make_request_options(
            body={},
            query={
                "name": name,
                "before_id": before_id,
                "after_id": after_id,
                "page": page,
                "limit": limit,
                "scope_id": scope_id,
                "ids[]": i_ds,
            },
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=FileMetadata, options=options, page_style="PageCursor")

    def delete(
        self,
        file_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeletedFile:
        """DELETE /files/{file_id}."""
        _path = path_template("/files/{file_id}", file_id=file_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("DELETE", _path, cast_to=DeletedFile, options=options)

    def download(
        self,
        file_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """GET /files/{file_id}/content."""
        _path = path_template("/files/{file_id}/content", file_id=file_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=None, options=options, binary=True, download_link=True)

    def retrieve_metadata(
        self,
        file_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileMetadata:
        """GET /files/{file_id}."""
        _path = path_template("/files/{file_id}", file_id=file_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=FileMetadata, options=options)

    def upload(
        self,
        *,
        file: FileTypes,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
        expires_in_seconds: Union[int, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileMetadata:
        """POST /files."""
        _path = path_template("/files")
        options = make_request_options(
            body={"name": name, "metadata": metadata, "file": file, "expires_in_seconds": expires_in_seconds},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=FileMetadata, options=options, file_fields=["file"])


class AsyncFiles(AsyncAPIResource):
    def list(
        self,
        *,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        scope_id: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        i_ds: Union[List[str], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[FileMetadata]:
        """GET /files."""
        _path = path_template("/files")
        options = make_request_options(
            body={},
            query={
                "name": name,
                "before_id": before_id,
                "after_id": after_id,
                "page": page,
                "limit": limit,
                "scope_id": scope_id,
                "ids[]": i_ds,
            },
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncPaginator(
            lambda: self._client.request("GET", _path, cast_to=FileMetadata, options=options, page_style="PageCursor")
        )

    async def delete(
        self,
        file_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeletedFile:
        """DELETE /files/{file_id}."""
        _path = path_template("/files/{file_id}", file_id=file_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("DELETE", _path, cast_to=DeletedFile, options=options)

    async def download(
        self,
        file_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """GET /files/{file_id}/content."""
        _path = path_template("/files/{file_id}/content", file_id=file_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("GET", _path, cast_to=None, options=options, binary=True, download_link=True)

    async def retrieve_metadata(
        self,
        file_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileMetadata:
        """GET /files/{file_id}."""
        _path = path_template("/files/{file_id}", file_id=file_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("GET", _path, cast_to=FileMetadata, options=options)

    async def upload(
        self,
        *,
        file: FileTypes,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
        expires_in_seconds: Union[int, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileMetadata:
        """POST /files."""
        _path = path_template("/files")
        options = make_request_options(
            body={"name": name, "metadata": metadata, "file": file, "expires_in_seconds": expires_in_seconds},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=FileMetadata, options=options, file_fields=["file"])
