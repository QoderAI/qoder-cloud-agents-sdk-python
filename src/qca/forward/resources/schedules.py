from __future__ import annotations

from typing import Any, Dict, List, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.forward.types.schedule import Schedule
from qca.forward.types.schedule_archive_many_response import ScheduleArchiveManyResponse
from qca.forward.types.schedule_run import ScheduleRun

__all__ = ["Schedules", "AsyncSchedules"]


class Schedules(SyncAPIResource):
    def list(
        self,
        *,
        identity_id: Union[str, None, NotGiven] = NOT_GIVEN,
        template_id: Union[str, None, NotGiven] = NOT_GIVEN,
        status: Union[str, None, NotGiven] = NOT_GIVEN,
        include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        sort_by: Union[str, None, NotGiven] = NOT_GIVEN,
        order: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Schedule]:
        """GET /schedules."""
        _path = path_template("/schedules")
        options = make_request_options(
            body={},
            query={
                "identity_id": identity_id,
                "template_id": template_id,
                "status": status,
                "include_archived": include_archived,
                "limit": limit,
                "after_id": after_id,
                "before_id": before_id,
                "sort_by": sort_by,
                "order": order,
            },
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=Schedule, options=options, page_style="Page")

    def create(
        self,
        *,
        identity_id: str,
        template_id: str,
        name: str,
        initial_events: List[Dict[str, Any]],
        environment_id: str,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        execution: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        trigger_policy: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        sinks: Union[List[Dict[str, Any]], None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Schedule:
        """POST /schedules."""
        _path = path_template("/schedules")
        options = make_request_options(
            body={
                "identity_id": identity_id,
                "template_id": template_id,
                "name": name,
                "description": description,
                "initial_events": initial_events,
                "execution": execution,
                "trigger_policy": trigger_policy,
                "environment_id": environment_id,
                "sinks": sinks,
                "metadata": metadata,
            },
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Schedule, options=options)

    def archive_many(
        self,
        *,
        schedule_ids: List[str],
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduleArchiveManyResponse:
        """POST /schedules/archive. Scope is set to by_schedule_ids automatically."""
        _path = path_template("/schedules/archive")
        options = make_request_options(
            body={"scope": "by_schedule_ids", "schedule_ids": schedule_ids},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=ScheduleArchiveManyResponse, options=options)

    def retrieve(
        self,
        schedule_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Schedule:
        """GET /schedules/{schedule_id}."""
        _path = path_template("/schedules/{schedule_id}", schedule_id=schedule_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=Schedule, options=options)

    def update(
        self,
        schedule_id: str,
        *,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        template_id: Union[str, None, NotGiven] = NOT_GIVEN,
        initial_events: Union[List[Dict[str, Any]], None, NotGiven] = NOT_GIVEN,
        execution: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        trigger_policy: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        environment_id: Union[str, None, NotGiven] = NOT_GIVEN,
        sinks: Union[List[Dict[str, Any]], None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Schedule:
        """POST /schedules/{schedule_id}."""
        _path = path_template("/schedules/{schedule_id}", schedule_id=schedule_id)
        options = make_request_options(
            body={
                "name": name,
                "description": description,
                "template_id": template_id,
                "initial_events": initial_events,
                "execution": execution,
                "trigger_policy": trigger_policy,
                "environment_id": environment_id,
                "sinks": sinks,
                "metadata": metadata,
            },
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Schedule, options=options)

    def archive(
        self,
        schedule_id: str,
        *,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Schedule:
        """POST /schedules/{schedule_id}/archive."""
        _path = path_template("/schedules/{schedule_id}/archive", schedule_id=schedule_id)
        options = make_request_options(
            body={},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Schedule, options=options)

    def pause(
        self,
        schedule_id: str,
        *,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Schedule:
        """POST /schedules/{schedule_id}/pause."""
        _path = path_template("/schedules/{schedule_id}/pause", schedule_id=schedule_id)
        options = make_request_options(
            body={},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Schedule, options=options)

    def run(
        self,
        schedule_id: str,
        *,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduleRun:
        """POST /schedules/{schedule_id}/run."""
        _path = path_template("/schedules/{schedule_id}/run", schedule_id=schedule_id)
        options = make_request_options(
            body={},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=ScheduleRun, options=options)

    def unpause(
        self,
        schedule_id: str,
        *,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Schedule:
        """POST /schedules/{schedule_id}/unpause."""
        _path = path_template("/schedules/{schedule_id}/unpause", schedule_id=schedule_id)
        options = make_request_options(
            body={},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Schedule, options=options)


class AsyncSchedules(AsyncAPIResource):
    def list(
        self,
        *,
        identity_id: Union[str, None, NotGiven] = NOT_GIVEN,
        template_id: Union[str, None, NotGiven] = NOT_GIVEN,
        status: Union[str, None, NotGiven] = NOT_GIVEN,
        include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        sort_by: Union[str, None, NotGiven] = NOT_GIVEN,
        order: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Schedule]:
        """GET /schedules."""
        _path = path_template("/schedules")
        options = make_request_options(
            body={},
            query={
                "identity_id": identity_id,
                "template_id": template_id,
                "status": status,
                "include_archived": include_archived,
                "limit": limit,
                "after_id": after_id,
                "before_id": before_id,
                "sort_by": sort_by,
                "order": order,
            },
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncPaginator(
            lambda: self._client.request("GET", _path, cast_to=Schedule, options=options, page_style="Page")
        )

    async def create(
        self,
        *,
        identity_id: str,
        template_id: str,
        name: str,
        initial_events: List[Dict[str, Any]],
        environment_id: str,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        execution: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        trigger_policy: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        sinks: Union[List[Dict[str, Any]], None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Schedule:
        """POST /schedules."""
        _path = path_template("/schedules")
        options = make_request_options(
            body={
                "identity_id": identity_id,
                "template_id": template_id,
                "name": name,
                "description": description,
                "initial_events": initial_events,
                "execution": execution,
                "trigger_policy": trigger_policy,
                "environment_id": environment_id,
                "sinks": sinks,
                "metadata": metadata,
            },
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Schedule, options=options)

    async def archive_many(
        self,
        *,
        schedule_ids: List[str],
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduleArchiveManyResponse:
        """POST /schedules/archive. Scope is set to by_schedule_ids automatically."""
        _path = path_template("/schedules/archive")
        options = make_request_options(
            body={"scope": "by_schedule_ids", "schedule_ids": schedule_ids},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=ScheduleArchiveManyResponse, options=options)

    async def retrieve(
        self,
        schedule_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Schedule:
        """GET /schedules/{schedule_id}."""
        _path = path_template("/schedules/{schedule_id}", schedule_id=schedule_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("GET", _path, cast_to=Schedule, options=options)

    async def update(
        self,
        schedule_id: str,
        *,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        template_id: Union[str, None, NotGiven] = NOT_GIVEN,
        initial_events: Union[List[Dict[str, Any]], None, NotGiven] = NOT_GIVEN,
        execution: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        trigger_policy: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        environment_id: Union[str, None, NotGiven] = NOT_GIVEN,
        sinks: Union[List[Dict[str, Any]], None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Schedule:
        """POST /schedules/{schedule_id}."""
        _path = path_template("/schedules/{schedule_id}", schedule_id=schedule_id)
        options = make_request_options(
            body={
                "name": name,
                "description": description,
                "template_id": template_id,
                "initial_events": initial_events,
                "execution": execution,
                "trigger_policy": trigger_policy,
                "environment_id": environment_id,
                "sinks": sinks,
                "metadata": metadata,
            },
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Schedule, options=options)

    async def archive(
        self,
        schedule_id: str,
        *,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Schedule:
        """POST /schedules/{schedule_id}/archive."""
        _path = path_template("/schedules/{schedule_id}/archive", schedule_id=schedule_id)
        options = make_request_options(
            body={},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Schedule, options=options)

    async def pause(
        self,
        schedule_id: str,
        *,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Schedule:
        """POST /schedules/{schedule_id}/pause."""
        _path = path_template("/schedules/{schedule_id}/pause", schedule_id=schedule_id)
        options = make_request_options(
            body={},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Schedule, options=options)

    async def run(
        self,
        schedule_id: str,
        *,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduleRun:
        """POST /schedules/{schedule_id}/run."""
        _path = path_template("/schedules/{schedule_id}/run", schedule_id=schedule_id)
        options = make_request_options(
            body={},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=ScheduleRun, options=options)

    async def unpause(
        self,
        schedule_id: str,
        *,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Schedule:
        """POST /schedules/{schedule_id}/unpause."""
        _path = path_template("/schedules/{schedule_id}/unpause", schedule_id=schedule_id)
        options = make_request_options(
            body={},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Schedule, options=options)
