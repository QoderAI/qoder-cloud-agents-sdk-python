from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.managed.types.self_hosted_work import SelfHostedWork
from qca.managed.types.self_hosted_work_heartbeat_response import SelfHostedWorkHeartbeatResponse
from qca.managed.types.self_hosted_work_queue_stats import SelfHostedWorkQueueStats

__all__ = ["Work", "AsyncWork"]


class Work(SyncAPIResource):
    def retrieve(
        self,
        work_id: str,
        *,
        environment_id: str,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SelfHostedWork:
        """GET /environments/{environment_id}/work/{work_id}."""
        _path = path_template(
            "/environments/{environment_id}/work/{work_id}", work_id=work_id, environment_id=environment_id
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
        return self._client.request("GET", _path, cast_to=SelfHostedWork, options=options)

    def update(
        self,
        work_id: str,
        *,
        environment_id: str,
        metadata: Dict[str, Any],
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SelfHostedWork:
        """POST /environments/{environment_id}/work/{work_id}."""
        _path = path_template(
            "/environments/{environment_id}/work/{work_id}", work_id=work_id, environment_id=environment_id
        )
        options = make_request_options(
            body={"metadata": metadata},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=SelfHostedWork, options=options)

    def list(
        self,
        environment_id: str,
        *,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[SelfHostedWork]:
        """GET /environments/{environment_id}/work."""
        _path = path_template("/environments/{environment_id}/work", environment_id=environment_id)
        options = make_request_options(
            body={},
            query={"before_id": before_id, "after_id": after_id, "page": page, "limit": limit},
            headers={"x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=SelfHostedWork, options=options, page_style="PageCursor")

    def ack(
        self,
        work_id: str,
        *,
        environment_id: str,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SelfHostedWork:
        """POST /environments/{environment_id}/work/{work_id}/ack."""
        _path = path_template(
            "/environments/{environment_id}/work/{work_id}/ack", work_id=work_id, environment_id=environment_id
        )
        options = make_request_options(
            body={},
            query={},
            headers={"x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=SelfHostedWork, options=options)

    def heartbeat(
        self,
        work_id: str,
        *,
        environment_id: str,
        desired_ttl_seconds: Union[int, None, NotGiven] = NOT_GIVEN,
        expected_last_heartbeat: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SelfHostedWorkHeartbeatResponse:
        """POST /environments/{environment_id}/work/{work_id}/heartbeat."""
        _path = path_template(
            "/environments/{environment_id}/work/{work_id}/heartbeat", work_id=work_id, environment_id=environment_id
        )
        options = make_request_options(
            body={},
            query={"desired_ttl_seconds": desired_ttl_seconds, "expected_last_heartbeat": expected_last_heartbeat},
            headers={"x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=SelfHostedWorkHeartbeatResponse, options=options)

    def poll(
        self,
        environment_id: str,
        *,
        block_ms: Union[int, None, NotGiven] = NOT_GIVEN,
        reclaim_older_than_ms: Union[int, None, NotGiven] = NOT_GIVEN,
        worker_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SelfHostedWork]:
        """GET /environments/{environment_id}/work/poll."""
        _path = path_template("/environments/{environment_id}/work/poll", environment_id=environment_id)
        options = make_request_options(
            body={},
            query={"block_ms": block_ms, "reclaim_older_than_ms": reclaim_older_than_ms},
            headers={"Worker-ID": worker_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=Optional[SelfHostedWork], options=options)

    def stats(
        self,
        environment_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SelfHostedWorkQueueStats:
        """GET /environments/{environment_id}/work/stats."""
        _path = path_template("/environments/{environment_id}/work/stats", environment_id=environment_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=SelfHostedWorkQueueStats, options=options)

    def stop(
        self,
        work_id: str,
        *,
        environment_id: str,
        force: Union[bool, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SelfHostedWork:
        """POST /environments/{environment_id}/work/{work_id}/stop."""
        _path = path_template(
            "/environments/{environment_id}/work/{work_id}/stop", work_id=work_id, environment_id=environment_id
        )
        options = make_request_options(
            body={"force": force},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=SelfHostedWork, options=options)


class AsyncWork(AsyncAPIResource):
    async def retrieve(
        self,
        work_id: str,
        *,
        environment_id: str,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SelfHostedWork:
        """GET /environments/{environment_id}/work/{work_id}."""
        _path = path_template(
            "/environments/{environment_id}/work/{work_id}", work_id=work_id, environment_id=environment_id
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
        return await self._client.request("GET", _path, cast_to=SelfHostedWork, options=options)

    async def update(
        self,
        work_id: str,
        *,
        environment_id: str,
        metadata: Dict[str, Any],
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SelfHostedWork:
        """POST /environments/{environment_id}/work/{work_id}."""
        _path = path_template(
            "/environments/{environment_id}/work/{work_id}", work_id=work_id, environment_id=environment_id
        )
        options = make_request_options(
            body={"metadata": metadata},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=SelfHostedWork, options=options)

    def list(
        self,
        environment_id: str,
        *,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[SelfHostedWork]:
        """GET /environments/{environment_id}/work."""
        _path = path_template("/environments/{environment_id}/work", environment_id=environment_id)
        options = make_request_options(
            body={},
            query={"before_id": before_id, "after_id": after_id, "page": page, "limit": limit},
            headers={"x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncPaginator(
            lambda: self._client.request("GET", _path, cast_to=SelfHostedWork, options=options, page_style="PageCursor")
        )

    async def ack(
        self,
        work_id: str,
        *,
        environment_id: str,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SelfHostedWork:
        """POST /environments/{environment_id}/work/{work_id}/ack."""
        _path = path_template(
            "/environments/{environment_id}/work/{work_id}/ack", work_id=work_id, environment_id=environment_id
        )
        options = make_request_options(
            body={},
            query={},
            headers={"x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=SelfHostedWork, options=options)

    async def heartbeat(
        self,
        work_id: str,
        *,
        environment_id: str,
        desired_ttl_seconds: Union[int, None, NotGiven] = NOT_GIVEN,
        expected_last_heartbeat: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SelfHostedWorkHeartbeatResponse:
        """POST /environments/{environment_id}/work/{work_id}/heartbeat."""
        _path = path_template(
            "/environments/{environment_id}/work/{work_id}/heartbeat", work_id=work_id, environment_id=environment_id
        )
        options = make_request_options(
            body={},
            query={"desired_ttl_seconds": desired_ttl_seconds, "expected_last_heartbeat": expected_last_heartbeat},
            headers={"x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=SelfHostedWorkHeartbeatResponse, options=options)

    async def poll(
        self,
        environment_id: str,
        *,
        block_ms: Union[int, None, NotGiven] = NOT_GIVEN,
        reclaim_older_than_ms: Union[int, None, NotGiven] = NOT_GIVEN,
        worker_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SelfHostedWork]:
        """GET /environments/{environment_id}/work/poll."""
        _path = path_template("/environments/{environment_id}/work/poll", environment_id=environment_id)
        options = make_request_options(
            body={},
            query={"block_ms": block_ms, "reclaim_older_than_ms": reclaim_older_than_ms},
            headers={"Worker-ID": worker_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("GET", _path, cast_to=Optional[SelfHostedWork], options=options)

    async def stats(
        self,
        environment_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SelfHostedWorkQueueStats:
        """GET /environments/{environment_id}/work/stats."""
        _path = path_template("/environments/{environment_id}/work/stats", environment_id=environment_id)
        options = make_request_options(
            body={},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("GET", _path, cast_to=SelfHostedWorkQueueStats, options=options)

    async def stop(
        self,
        work_id: str,
        *,
        environment_id: str,
        force: Union[bool, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SelfHostedWork:
        """POST /environments/{environment_id}/work/{work_id}/stop."""
        _path = path_template(
            "/environments/{environment_id}/work/{work_id}/stop", work_id=work_id, environment_id=environment_id
        )
        options = make_request_options(
            body={"force": force},
            query={},
            headers={"qoder-workspace-id": workspace_id, "x-qoder-beta": betas},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=SelfHostedWork, options=options)
