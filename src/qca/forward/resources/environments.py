from __future__ import annotations

from typing import Any, Dict, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.forward.types.environment import Environment

__all__ = ["Environments", "AsyncEnvironments"]


class Environments(SyncAPIResource):
    def list(
        self,
        *,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        identity_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Environment]:
        """GET /environments.

        identity_id selects identity ownership with a PAT; omit it with a SAT.
        """
        _path = path_template("/environments")
        options = make_request_options(
            body={},
            query={
                "identity_id": identity_id,
                "limit": limit,
                "page": page,
                "after_id": after_id,
                "before_id": before_id,
            },
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=Environment, options=options, page_style="PageCursor")

    def create(
        self,
        *,
        name: str,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        config: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        identity_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Environment:
        """POST /environments.

        identity_id selects identity ownership with a PAT; omit it with a SAT.
        """
        _path = path_template("/environments")
        options = make_request_options(
            body={"name": name, "description": description, "config": config, "metadata": metadata},
            query={"identity_id": identity_id},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Environment, options=options)

    def retrieve(
        self,
        environment_id: str,
        *,
        identity_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Environment:
        """GET /environments/{environment_id}.

        identity_id selects identity ownership with a PAT; omit it with a SAT.
        """
        _path = path_template("/environments/{environment_id}", environment_id=environment_id)
        options = make_request_options(
            body={},
            query={"identity_id": identity_id},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=Environment, options=options)

    def update(
        self,
        environment_id: str,
        *,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        config: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        identity_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Environment:
        """POST /environments/{environment_id}.

        identity_id selects identity ownership with a PAT; omit it with a SAT.
        """
        _path = path_template("/environments/{environment_id}", environment_id=environment_id)
        options = make_request_options(
            body={"name": name, "description": description, "config": config, "metadata": metadata},
            query={"identity_id": identity_id},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Environment, options=options)

    def archive(
        self,
        environment_id: str,
        *,
        identity_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Environment:
        """POST /environments/{environment_id}/archive.

        identity_id selects identity ownership with a PAT; omit it with a SAT.
        """
        _path = path_template("/environments/{environment_id}/archive", environment_id=environment_id)
        options = make_request_options(
            body={},
            query={"identity_id": identity_id},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Environment, options=options)

    def delete(
        self,
        environment_id: str,
        *,
        identity_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """DELETE /environments/{environment_id}.

        identity_id selects identity ownership with a PAT; omit it with a SAT.
        """
        _path = path_template("/environments/{environment_id}", environment_id=environment_id)
        options = make_request_options(
            body={},
            query={"identity_id": identity_id},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("DELETE", _path, cast_to=None, options=options)


class AsyncEnvironments(AsyncAPIResource):
    def list(
        self,
        *,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        page: Union[str, None, NotGiven] = NOT_GIVEN,
        after_id: Union[str, None, NotGiven] = NOT_GIVEN,
        before_id: Union[str, None, NotGiven] = NOT_GIVEN,
        identity_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Environment]:
        """GET /environments.

        identity_id selects identity ownership with a PAT; omit it with a SAT.
        """
        _path = path_template("/environments")
        options = make_request_options(
            body={},
            query={
                "identity_id": identity_id,
                "limit": limit,
                "page": page,
                "after_id": after_id,
                "before_id": before_id,
            },
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncPaginator(
            lambda: self._client.request("GET", _path, cast_to=Environment, options=options, page_style="PageCursor")
        )

    async def create(
        self,
        *,
        name: str,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        config: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        identity_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Environment:
        """POST /environments.

        identity_id selects identity ownership with a PAT; omit it with a SAT.
        """
        _path = path_template("/environments")
        options = make_request_options(
            body={"name": name, "description": description, "config": config, "metadata": metadata},
            query={"identity_id": identity_id},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Environment, options=options)

    async def retrieve(
        self,
        environment_id: str,
        *,
        identity_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Environment:
        """GET /environments/{environment_id}.

        identity_id selects identity ownership with a PAT; omit it with a SAT.
        """
        _path = path_template("/environments/{environment_id}", environment_id=environment_id)
        options = make_request_options(
            body={},
            query={"identity_id": identity_id},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("GET", _path, cast_to=Environment, options=options)

    async def update(
        self,
        environment_id: str,
        *,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        config: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        identity_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Environment:
        """POST /environments/{environment_id}.

        identity_id selects identity ownership with a PAT; omit it with a SAT.
        """
        _path = path_template("/environments/{environment_id}", environment_id=environment_id)
        options = make_request_options(
            body={"name": name, "description": description, "config": config, "metadata": metadata},
            query={"identity_id": identity_id},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Environment, options=options)

    async def archive(
        self,
        environment_id: str,
        *,
        identity_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Environment:
        """POST /environments/{environment_id}/archive.

        identity_id selects identity ownership with a PAT; omit it with a SAT.
        """
        _path = path_template("/environments/{environment_id}/archive", environment_id=environment_id)
        options = make_request_options(
            body={},
            query={"identity_id": identity_id},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Environment, options=options)

    async def delete(
        self,
        environment_id: str,
        *,
        identity_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """DELETE /environments/{environment_id}.

        identity_id selects identity ownership with a PAT; omit it with a SAT.
        """
        _path = path_template("/environments/{environment_id}", environment_id=environment_id)
        options = make_request_options(
            body={},
            query={"identity_id": identity_id},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("DELETE", _path, cast_to=None, options=options)
