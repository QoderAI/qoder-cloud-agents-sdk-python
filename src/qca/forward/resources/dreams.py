from __future__ import annotations

from typing import Any, Dict, List, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.forward.types.dream import Dream, DreamInputParam, DreamModelConfigParam


class Dreams(SyncAPIResource):
    """Forward memory consolidation; requires PAT or an admin SAT."""

    def create(
        self,
        *,
        inputs: List[DreamInputParam],
        model: Union[str, DreamModelConfigParam, None, NotGiven] = NOT_GIVEN,
        instructions: Union[str, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Dream:
        """POST /dreams."""
        _path = path_template("/dreams")
        options = make_request_options(
            body={"inputs": inputs, "model": model, "instructions": instructions},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Dream, options=options)

    def list(
        self,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        after_id: Union[str, NotGiven] = NOT_GIVEN,
        before_id: Union[str, NotGiven] = NOT_GIVEN,
        include_archived: Union[bool, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Dream]:
        """GET /dreams."""
        _path = path_template("/dreams")
        options = make_request_options(
            body={},
            query={"limit": limit, "after_id": after_id, "before_id": before_id, "include_archived": include_archived},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=Dream, options=options, page_style="Page")

    def retrieve(
        self,
        dream_id: str,
        *,
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
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=Dream, options=options)

    def cancel(
        self,
        dream_id: str,
        *,
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
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not options["body"]:
            options["body"] = None
        return self._client.request("POST", _path, cast_to=Dream, options=options)

    def archive(
        self,
        dream_id: str,
        *,
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
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not options["body"]:
            options["body"] = None
        return self._client.request("POST", _path, cast_to=Dream, options=options)


class AsyncDreams(AsyncAPIResource):
    """Forward memory consolidation; requires PAT or an admin SAT."""

    async def create(
        self,
        *,
        inputs: List[DreamInputParam],
        model: Union[str, DreamModelConfigParam, None, NotGiven] = NOT_GIVEN,
        instructions: Union[str, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Dream:
        """POST /dreams."""
        _path = path_template("/dreams")
        options = make_request_options(
            body={"inputs": inputs, "model": model, "instructions": instructions},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Dream, options=options)

    def list(
        self,
        *,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        after_id: Union[str, NotGiven] = NOT_GIVEN,
        before_id: Union[str, NotGiven] = NOT_GIVEN,
        include_archived: Union[bool, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Dream]:
        """GET /dreams."""
        _path = path_template("/dreams")
        options = make_request_options(
            body={},
            query={"limit": limit, "after_id": after_id, "before_id": before_id, "include_archived": include_archived},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncPaginator(
            lambda: self._client.request("GET", _path, cast_to=Dream, options=options, page_style="Page")
        )

    async def retrieve(
        self,
        dream_id: str,
        *,
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
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("GET", _path, cast_to=Dream, options=options)

    async def cancel(
        self,
        dream_id: str,
        *,
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
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not options["body"]:
            options["body"] = None
        return await self._client.request("POST", _path, cast_to=Dream, options=options)

    async def archive(
        self,
        dream_id: str,
        *,
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
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not options["body"]:
            options["body"] = None
        return await self._client.request("POST", _path, cast_to=Dream, options=options)
