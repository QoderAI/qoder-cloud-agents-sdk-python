from __future__ import annotations

from typing import Any, Dict, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.forward.types.schedule_run import ScheduleRun

__all__ = ["ScheduleRuns", "AsyncScheduleRuns"]


class ScheduleRuns(SyncAPIResource):
    def list(
        self,
        *,
        identity_id: Union[str, None, NotGiven] = NOT_GIVEN,
        schedule_id: Union[str, None, NotGiven] = NOT_GIVEN,
        status: Union[str, None, NotGiven] = NOT_GIVEN,
        trigger_type: Union[str, None, NotGiven] = NOT_GIVEN,
        has_error: Union[bool, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        sort_by: Union[str, None, NotGiven] = NOT_GIVEN,
        order: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[ScheduleRun]:
        """GET /schedule_runs."""
        _path = path_template("/schedule_runs")
        options = make_request_options(
            body={},
            query={
                "identity_id": identity_id,
                "schedule_id": schedule_id,
                "status": status,
                "trigger_type": trigger_type,
                "has_error": has_error,
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
        return self._client.request("GET", _path, cast_to=ScheduleRun, options=options, page_style="Page")

    def retrieve(
        self,
        run_id: str,
        *,
        identity_id: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduleRun:
        """GET /schedule_runs/{run_id}."""
        _path = path_template("/schedule_runs/{run_id}", run_id=run_id)
        options = make_request_options(
            body={},
            query={"identity_id": identity_id},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=ScheduleRun, options=options)


class AsyncScheduleRuns(AsyncAPIResource):
    def list(
        self,
        *,
        identity_id: Union[str, None, NotGiven] = NOT_GIVEN,
        schedule_id: Union[str, None, NotGiven] = NOT_GIVEN,
        status: Union[str, None, NotGiven] = NOT_GIVEN,
        trigger_type: Union[str, None, NotGiven] = NOT_GIVEN,
        has_error: Union[bool, None, NotGiven] = NOT_GIVEN,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        sort_by: Union[str, None, NotGiven] = NOT_GIVEN,
        order: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ScheduleRun]:
        """GET /schedule_runs."""
        _path = path_template("/schedule_runs")
        options = make_request_options(
            body={},
            query={
                "identity_id": identity_id,
                "schedule_id": schedule_id,
                "status": status,
                "trigger_type": trigger_type,
                "has_error": has_error,
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
            lambda: self._client.request("GET", _path, cast_to=ScheduleRun, options=options, page_style="Page")
        )

    async def retrieve(
        self,
        run_id: str,
        *,
        identity_id: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduleRun:
        """GET /schedule_runs/{run_id}."""
        _path = path_template("/schedule_runs/{run_id}", run_id=run_id)
        options = make_request_options(
            body={},
            query={"identity_id": identity_id},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("GET", _path, cast_to=ScheduleRun, options=options)
