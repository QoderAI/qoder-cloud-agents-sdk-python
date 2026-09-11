from __future__ import annotations

from typing import Any, Dict, List, Literal, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.managed.types.delete_session_resource import DeleteSessionResource
from qca.managed.types.file_resource import FileResource
from qca.managed.types.session_resource_get_response_union import SessionResourceGetResponseUnion
from qca.managed.types.session_resource_union import SessionResourceUnion
from qca.managed.types.session_resource_update_response_union import SessionResourceUpdateResponseUnion

__all__ = ["Resources", "AsyncResources"]


class Resources(SyncAPIResource):
    def retrieve(
        self,
        resource_id: str,
        *,
        session_id: str,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionResourceGetResponseUnion:
        """GET /sessions/{session_id}/resources/{resource_id}."""
        _path = path_template(
            "/sessions/{session_id}/resources/{resource_id}", resource_id=resource_id, session_id=session_id
        )
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=SessionResourceGetResponseUnion, options=options)

    def update(
        self,
        resource_id: str,
        *,
        session_id: str,
        password: Union[str, None, NotGiven] = NOT_GIVEN,
        authorization_token: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionResourceUpdateResponseUnion:
        """POST /sessions/{session_id}/resources/{resource_id}."""
        _path = path_template(
            "/sessions/{session_id}/resources/{resource_id}", resource_id=resource_id, session_id=session_id
        )
        options = make_request_options(
            body={"password": password, "authorization_token": authorization_token},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=SessionResourceUpdateResponseUnion, options=options)

    def list(
        self,
        session_id: str,
        *,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[SessionResourceUnion]:
        """GET /sessions/{session_id}/resources."""
        _path = path_template("/sessions/{session_id}/resources", session_id=session_id)
        options = make_request_options(
            body={},
            query={"before_id": before_id, "after_id": after_id, "limit": limit, "page": page},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request(
            "GET", _path, cast_to=SessionResourceUnion, options=options, page_style="PageCursor"
        )

    def delete(
        self,
        resource_id: str,
        *,
        session_id: str,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeleteSessionResource:
        """DELETE /sessions/{session_id}/resources/{resource_id}."""
        _path = path_template(
            "/sessions/{session_id}/resources/{resource_id}", resource_id=resource_id, session_id=session_id
        )
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("DELETE", _path, cast_to=DeleteSessionResource, options=options)

    def add(
        self,
        session_id: str,
        *,
        file_id: str,
        type: Literal["file"],
        mount_path: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileResource:
        """POST /sessions/{session_id}/resources."""
        _path = path_template("/sessions/{session_id}/resources", session_id=session_id)
        options = make_request_options(
            body={"file_id": file_id, "type": type, "mount_path": mount_path},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=FileResource, options=options)


class AsyncResources(AsyncAPIResource):
    async def retrieve(
        self,
        resource_id: str,
        *,
        session_id: str,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionResourceGetResponseUnion:
        """GET /sessions/{session_id}/resources/{resource_id}."""
        _path = path_template(
            "/sessions/{session_id}/resources/{resource_id}", resource_id=resource_id, session_id=session_id
        )
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("GET", _path, cast_to=SessionResourceGetResponseUnion, options=options)

    async def update(
        self,
        resource_id: str,
        *,
        session_id: str,
        password: Union[str, None, NotGiven] = NOT_GIVEN,
        authorization_token: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionResourceUpdateResponseUnion:
        """POST /sessions/{session_id}/resources/{resource_id}."""
        _path = path_template(
            "/sessions/{session_id}/resources/{resource_id}", resource_id=resource_id, session_id=session_id
        )
        options = make_request_options(
            body={"password": password, "authorization_token": authorization_token},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=SessionResourceUpdateResponseUnion, options=options)

    def list(
        self,
        session_id: str,
        *,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[SessionResourceUnion]:
        """GET /sessions/{session_id}/resources."""
        _path = path_template("/sessions/{session_id}/resources", session_id=session_id)
        options = make_request_options(
            body={},
            query={"before_id": before_id, "after_id": after_id, "limit": limit, "page": page},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncPaginator(
            lambda: self._client.request(
                "GET", _path, cast_to=SessionResourceUnion, options=options, page_style="PageCursor"
            )
        )

    async def delete(
        self,
        resource_id: str,
        *,
        session_id: str,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeleteSessionResource:
        """DELETE /sessions/{session_id}/resources/{resource_id}."""
        _path = path_template(
            "/sessions/{session_id}/resources/{resource_id}", resource_id=resource_id, session_id=session_id
        )
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("DELETE", _path, cast_to=DeleteSessionResource, options=options)

    async def add(
        self,
        session_id: str,
        *,
        file_id: str,
        type: Literal["file"],
        mount_path: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileResource:
        """POST /sessions/{session_id}/resources."""
        _path = path_template("/sessions/{session_id}/resources", session_id=session_id)
        options = make_request_options(
            body={"file_id": file_id, "type": type, "mount_path": mount_path},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=FileResource, options=options)
