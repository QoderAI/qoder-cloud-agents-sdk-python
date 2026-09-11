from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.managed.types.dream import Dream
from qca.managed.types.dream_memory_store_input_param import DreamMemoryStoreInputParam
from qca.managed.types.dream_model_config_param import DreamModelConfigParam
from qca.managed.types.dream_sessions_input_param import DreamSessionsInputParam
from qca.managed.types.output_behavior_create_new_param import OutputBehaviorCreateNewParam
from qca.managed.types.output_behavior_update_existing_param import OutputBehaviorUpdateExistingParam

__all__ = ["Dreams", "AsyncDreams"]


class Dreams(SyncAPIResource):
    def create(
        self,
        *,
        inputs: List[Union[DreamMemoryStoreInputParam, DreamSessionsInputParam]],
        model: Union[str, DreamModelConfigParam],
        instructions: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        output_behavior: Union[
            Union[OutputBehaviorCreateNewParam, OutputBehaviorUpdateExistingParam], None, NotGiven
        ] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Dream:
        """POST /dreams."""
        _path = path_template("/dreams")
        options = make_request_options(
            body={"inputs": inputs, "model": model, "instructions": instructions, "output_behavior": output_behavior},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Dream, options=options)

    def retrieve(
        self,
        dream_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Dream:
        """GET /dreams/{dream_id}."""
        _path = path_template("/dreams/{dream_id}", dream_id=dream_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=Dream, options=options)

    def list(
        self,
        *,
        created_at_gt: Union[datetime, None, NotGiven] = NOT_GIVEN,
        created_at_lt: Union[datetime, None, NotGiven] = NOT_GIVEN,
        include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        statuses: Union[
            List[Literal["pending", "running", "completed", "failed", "canceled"]], None, NotGiven
        ] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Dream]:
        """GET /dreams."""
        _path = path_template("/dreams")
        options = make_request_options(
            body={},
            query={
                "created_at[gt]": created_at_gt,
                "created_at[lt]": created_at_lt,
                "include_archived": include_archived,
                "limit": limit,
                "page": page,
                "statuses[]": statuses,
            },
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=Dream, options=options, page_style="PageCursor")

    def archive(
        self,
        dream_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Dream:
        """POST /dreams/{dream_id}/archive."""
        _path = path_template("/dreams/{dream_id}/archive", dream_id=dream_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Dream, options=options)

    def cancel(
        self,
        dream_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Dream:
        """POST /dreams/{dream_id}/cancel."""
        _path = path_template("/dreams/{dream_id}/cancel", dream_id=dream_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Dream, options=options)


class AsyncDreams(AsyncAPIResource):
    async def create(
        self,
        *,
        inputs: List[Union[DreamMemoryStoreInputParam, DreamSessionsInputParam]],
        model: Union[str, DreamModelConfigParam],
        instructions: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        output_behavior: Union[
            Union[OutputBehaviorCreateNewParam, OutputBehaviorUpdateExistingParam], None, NotGiven
        ] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Dream:
        """POST /dreams."""
        _path = path_template("/dreams")
        options = make_request_options(
            body={"inputs": inputs, "model": model, "instructions": instructions, "output_behavior": output_behavior},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Dream, options=options)

    async def retrieve(
        self,
        dream_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Dream:
        """GET /dreams/{dream_id}."""
        _path = path_template("/dreams/{dream_id}", dream_id=dream_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("GET", _path, cast_to=Dream, options=options)

    def list(
        self,
        *,
        created_at_gt: Union[datetime, None, NotGiven] = NOT_GIVEN,
        created_at_lt: Union[datetime, None, NotGiven] = NOT_GIVEN,
        include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        statuses: Union[
            List[Literal["pending", "running", "completed", "failed", "canceled"]], None, NotGiven
        ] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Dream]:
        """GET /dreams."""
        _path = path_template("/dreams")
        options = make_request_options(
            body={},
            query={
                "created_at[gt]": created_at_gt,
                "created_at[lt]": created_at_lt,
                "include_archived": include_archived,
                "limit": limit,
                "page": page,
                "statuses[]": statuses,
            },
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncPaginator(
            lambda: self._client.request("GET", _path, cast_to=Dream, options=options, page_style="PageCursor")
        )

    async def archive(
        self,
        dream_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Dream:
        """POST /dreams/{dream_id}/archive."""
        _path = path_template("/dreams/{dream_id}/archive", dream_id=dream_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Dream, options=options)

    async def cancel(
        self,
        dream_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Dream:
        """POST /dreams/{dream_id}/cancel."""
        _path = path_template("/dreams/{dream_id}/cancel", dream_id=dream_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Dream, options=options)
