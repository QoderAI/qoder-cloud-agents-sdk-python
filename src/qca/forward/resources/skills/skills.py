from __future__ import annotations

from functools import cached_property
from typing import Any, Dict, List, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, FileTypes, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.forward.resources.skills.versions import AsyncVersions, Versions
from qca.forward.types.skill import Skill

__all__ = ["Skills", "AsyncSkills"]


class Skills(SyncAPIResource):
    @cached_property
    def versions(self) -> Versions:
        return Versions(self._client)

    def list(
        self,
        *,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        display_title: Union[str, None, NotGiven] = NOT_GIVEN,
        source: Union[str, None, NotGiven] = NOT_GIVEN,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Skill]:
        """GET /skills."""
        _path = path_template("/skills")
        options = make_request_options(
            body={},
            query={
                "limit": limit,
                "page": page,
                "after_id": after_id,
                "before_id": before_id,
                "display_title": display_title,
                "source": source,
                "name": name,
            },
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=Skill, options=options, page_style="PageCursor")

    def create(
        self,
        *,
        files: Union[List[FileTypes], None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        icon_id: Union[str, None, NotGiven] = NOT_GIVEN,
        file: Union[FileTypes, None, NotGiven] = NOT_GIVEN,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        type: Union[str, None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Skill:
        """POST /skills."""
        _path = path_template("/skills")
        options = make_request_options(
            body={
                "files": files,
                "metadata": metadata,
                "icon_id": icon_id,
                "file": file,
                "name": name,
                "description": description,
                "type": type,
            },
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Skill, options=options, file_fields=["files", "file"])

    def retrieve(
        self,
        skill_id: str,
        *,
        include_content: Union[bool, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Skill:
        """GET /skills/{skill_id}."""
        _path = path_template("/skills/{skill_id}", skill_id=skill_id)
        options = make_request_options(
            body={},
            query={"include_content": include_content},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=Skill, options=options)

    def update(
        self,
        skill_id: str,
        *,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        content: Union[str, None, NotGiven] = NOT_GIVEN,
        content_encoding: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        icon_id: Union[str, None, NotGiven] = NOT_GIVEN,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Skill:
        """PUT /skills/{skill_id}."""
        _path = path_template("/skills/{skill_id}", skill_id=skill_id)
        options = make_request_options(
            body={
                "description": description,
                "content": content,
                "content_encoding": content_encoding,
                "metadata": metadata,
                "icon_id": icon_id,
                "name": name,
            },
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("PUT", _path, cast_to=Skill, options=options)

    def delete(
        self,
        skill_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """DELETE /skills/{skill_id}."""
        _path = path_template("/skills/{skill_id}", skill_id=skill_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("DELETE", _path, cast_to=None, options=options)


class AsyncSkills(AsyncAPIResource):
    @cached_property
    def versions(self) -> AsyncVersions:
        return AsyncVersions(self._client)

    def list(
        self,
        *,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        display_title: Union[str, None, NotGiven] = NOT_GIVEN,
        source: Union[str, None, NotGiven] = NOT_GIVEN,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Skill]:
        """GET /skills."""
        _path = path_template("/skills")
        options = make_request_options(
            body={},
            query={
                "limit": limit,
                "page": page,
                "after_id": after_id,
                "before_id": before_id,
                "display_title": display_title,
                "source": source,
                "name": name,
            },
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncPaginator(
            lambda: self._client.request("GET", _path, cast_to=Skill, options=options, page_style="PageCursor")
        )

    async def create(
        self,
        *,
        files: Union[List[FileTypes], None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        icon_id: Union[str, None, NotGiven] = NOT_GIVEN,
        file: Union[FileTypes, None, NotGiven] = NOT_GIVEN,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        type: Union[str, None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Skill:
        """POST /skills."""
        _path = path_template("/skills")
        options = make_request_options(
            body={
                "files": files,
                "metadata": metadata,
                "icon_id": icon_id,
                "file": file,
                "name": name,
                "description": description,
                "type": type,
            },
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Skill, options=options, file_fields=["files", "file"])

    async def retrieve(
        self,
        skill_id: str,
        *,
        include_content: Union[bool, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Skill:
        """GET /skills/{skill_id}."""
        _path = path_template("/skills/{skill_id}", skill_id=skill_id)
        options = make_request_options(
            body={},
            query={"include_content": include_content},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("GET", _path, cast_to=Skill, options=options)

    async def update(
        self,
        skill_id: str,
        *,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        content: Union[str, None, NotGiven] = NOT_GIVEN,
        content_encoding: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        icon_id: Union[str, None, NotGiven] = NOT_GIVEN,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Skill:
        """PUT /skills/{skill_id}."""
        _path = path_template("/skills/{skill_id}", skill_id=skill_id)
        options = make_request_options(
            body={
                "description": description,
                "content": content,
                "content_encoding": content_encoding,
                "metadata": metadata,
                "icon_id": icon_id,
                "name": name,
            },
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("PUT", _path, cast_to=Skill, options=options)

    async def delete(
        self,
        skill_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """DELETE /skills/{skill_id}."""
        _path = path_template("/skills/{skill_id}", skill_id=skill_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("DELETE", _path, cast_to=None, options=options)
