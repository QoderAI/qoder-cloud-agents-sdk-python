from __future__ import annotations

from typing import Any, Dict, List, Union

import httpx

from qca.common._resource import AsyncAPIResource, SyncAPIResource
from qca.common._types import NOT_GIVEN, NotGiven
from qca.common._utils import make_request_options, path_template
from qca.common.pagination import AsyncPaginator, SyncPage
from qca.forward.types.decision import Decision
from qca.forward.types.decision_create_params import DecisionQuestionParam

__all__ = ["Decisions", "AsyncDecisions"]


class Decisions(SyncAPIResource):
    def create(
        self,
        *,
        questions: List[DecisionQuestionParam],
        session_id: Union[str, NotGiven] = NOT_GIVEN,
        state: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Decision:
        """POST /decisions.

        Synchronous evaluation using normal PAT/SAT authentication. Provide exactly
        one of session_id and nonempty state; state.session_context is reserved.
        Questions are choice (string/boolean options) or score (numeric levels).
        Reusing an idempotency key with identical bytes replays the stored result;
        different bytes or an in-progress request return HTTP 409.
        Explicit state/questions are never shortened; over-budget input is HTTP 422.
        """
        _path = path_template("/decisions")
        options = make_request_options(
            body={"questions": questions, "session_id": session_id, "state": state},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("POST", _path, cast_to=Decision, options=options)

    def retrieve(
        self,
        decision_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Decision:
        """GET /decisions/{decision_id}.

        Retrieve a stored Decision, including running or failed records.
        """
        _path = path_template("/decisions/{decision_id}", decision_id=decision_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=Decision, options=options)

    def list(
        self,
        *,
        session_id: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        after_id: Union[str, NotGiven] = NOT_GIVEN,
        before_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Decision]:
        """GET /decisions.

        List in server order, optionally filtered by an accessible Session.
        Limit is 1-100 (default 20). after_id and before_id are mutually exclusive.
        Identity scope comes from authentication, not a query parameter.
        """
        _path = path_template("/decisions")
        options = make_request_options(
            body={},
            query={"session_id": session_id, "limit": limit, "after_id": after_id, "before_id": before_id},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._client.request("GET", _path, cast_to=Decision, options=options, page_style="Page")


class AsyncDecisions(AsyncAPIResource):
    async def create(
        self,
        *,
        questions: List[DecisionQuestionParam],
        session_id: Union[str, NotGiven] = NOT_GIVEN,
        state: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Decision:
        """POST /decisions.

        Synchronous evaluation using normal PAT/SAT authentication. Provide exactly
        one of session_id and nonempty state; state.session_context is reserved.
        Questions are choice (string/boolean options) or score (numeric levels).
        Reusing an idempotency key with identical bytes replays the stored result;
        different bytes or an in-progress request return HTTP 409.
        Explicit state/questions are never shortened; over-budget input is HTTP 422.
        """
        _path = path_template("/decisions")
        options = make_request_options(
            body={"questions": questions, "session_id": session_id, "state": state},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("POST", _path, cast_to=Decision, options=options)

    async def retrieve(
        self,
        decision_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Decision:
        """GET /decisions/{decision_id}.

        Retrieve a stored Decision, including running or failed records.
        """
        _path = path_template("/decisions/{decision_id}", decision_id=decision_id)
        options = make_request_options(
            body={},
            query={},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self._client.request("GET", _path, cast_to=Decision, options=options)

    def list(
        self,
        *,
        session_id: Union[str, NotGiven] = NOT_GIVEN,
        limit: Union[int, NotGiven] = NOT_GIVEN,
        after_id: Union[str, NotGiven] = NOT_GIVEN,
        before_id: Union[str, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Decision]:
        """GET /decisions.

        List in server order, optionally filtered by an accessible Session.
        Limit is 1-100 (default 20). after_id and before_id are mutually exclusive.
        Identity scope comes from authentication, not a query parameter.
        """
        _path = path_template("/decisions")
        options = make_request_options(
            body={},
            query={"session_id": session_id, "limit": limit, "after_id": after_id, "before_id": before_id},
            headers={},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncPaginator(
            lambda: self._client.request("GET", _path, cast_to=Decision, options=options, page_style="Page")
        )
