from __future__ import annotations

from typing import Any, Dict, List, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.forward.types.identity_usage import IdentityUsage
from qca.forward.types.template_usage import TemplateUsage

__all__ = ["Usage", "AsyncUsage"]


class Usage(SyncAPIResource):
    def list_identities(
        self,
        *,
        start_at: str,
        end_at: str,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        identity_id: Union[str, None, NotGiven] = NOT_GIVEN,
        identity_ids: Union[str, List[str], None, NotGiven] = NOT_GIVEN,
        template_id: Union[str, None, NotGiven] = NOT_GIVEN,
        template_ids: Union[str, List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[IdentityUsage]:
        """GET /usage/identities.

        PAT or Admin SAT. YYYY-MM-DDTHH:00:00 in Asia/Shanghai, start inclusive, end exclusive; maximum 744 hours. Only hourly parameters are supported.
        """
        _path = path_template("/usage/identities")
        options = make_request_options(
            body={},
            query={
                "start_at": start_at,
                "end_at": end_at,
                "limit": limit,
                "after_id": after_id,
                "before_id": before_id,
                "identity_id": identity_id,
                "identity_ids": identity_ids,
                "template_id": template_id,
                "template_ids": template_ids,
            },
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=IdentityUsage, options=options, page_style="Page")

    def list_templates(
        self,
        *,
        start_at: str,
        end_at: str,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        identity_id: Union[str, None, NotGiven] = NOT_GIVEN,
        identity_ids: Union[str, List[str], None, NotGiven] = NOT_GIVEN,
        template_id: Union[str, None, NotGiven] = NOT_GIVEN,
        template_ids: Union[str, List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[TemplateUsage]:
        """GET /usage/templates.

        PAT or Admin SAT. YYYY-MM-DDTHH:00:00 in Asia/Shanghai, start inclusive, end exclusive; maximum 744 hours. Only hourly parameters are supported.
        """
        _path = path_template("/usage/templates")
        options = make_request_options(
            body={},
            query={
                "start_at": start_at,
                "end_at": end_at,
                "limit": limit,
                "after_id": after_id,
                "before_id": before_id,
                "identity_id": identity_id,
                "identity_ids": identity_ids,
                "template_id": template_id,
                "template_ids": template_ids,
            },
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=TemplateUsage, options=options, page_style="Page")


class AsyncUsage(AsyncAPIResource):
    def list_identities(
        self,
        *,
        start_at: str,
        end_at: str,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        identity_id: Union[str, None, NotGiven] = NOT_GIVEN,
        identity_ids: Union[str, List[str], None, NotGiven] = NOT_GIVEN,
        template_id: Union[str, None, NotGiven] = NOT_GIVEN,
        template_ids: Union[str, List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[IdentityUsage]:
        """GET /usage/identities.

        PAT or Admin SAT. YYYY-MM-DDTHH:00:00 in Asia/Shanghai, start inclusive, end exclusive; maximum 744 hours. Only hourly parameters are supported.
        """
        _path = path_template("/usage/identities")
        options = make_request_options(
            body={},
            query={
                "start_at": start_at,
                "end_at": end_at,
                "limit": limit,
                "after_id": after_id,
                "before_id": before_id,
                "identity_id": identity_id,
                "identity_ids": identity_ids,
                "template_id": template_id,
                "template_ids": template_ids,
            },
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncPaginator(
            lambda: self._client.request("GET", _path, cast_to=IdentityUsage, options=options, page_style="Page")
        )

    def list_templates(
        self,
        *,
        start_at: str,
        end_at: str,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        identity_id: Union[str, None, NotGiven] = NOT_GIVEN,
        identity_ids: Union[str, List[str], None, NotGiven] = NOT_GIVEN,
        template_id: Union[str, None, NotGiven] = NOT_GIVEN,
        template_ids: Union[str, List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[TemplateUsage]:
        """GET /usage/templates.

        PAT or Admin SAT. YYYY-MM-DDTHH:00:00 in Asia/Shanghai, start inclusive, end exclusive; maximum 744 hours. Only hourly parameters are supported.
        """
        _path = path_template("/usage/templates")
        options = make_request_options(
            body={},
            query={
                "start_at": start_at,
                "end_at": end_at,
                "limit": limit,
                "after_id": after_id,
                "before_id": before_id,
                "identity_id": identity_id,
                "identity_ids": identity_ids,
                "template_id": template_id,
                "template_ids": template_ids,
            },
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncPaginator(
            lambda: self._client.request("GET", _path, cast_to=TemplateUsage, options=options, page_style="Page")
        )
