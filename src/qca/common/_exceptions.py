from __future__ import annotations

from typing import Any

import httpx


class APIError(Exception):
    def __init__(self, message: str, *, request: httpx.Request, body: Any = None) -> None:
        super().__init__(message)
        self.message = message
        self.request = request
        self.body = body
        error = body.get("error", body) if isinstance(body, dict) else {}
        error = error if isinstance(error, dict) else {}
        self.code = error.get("code")
        self.type = error.get("type")


class APIConnectionError(APIError):
    def __init__(self, *, request: httpx.Request, message: str = "Connection error.") -> None:
        super().__init__(message, request=request)


class APITimeoutError(APIConnectionError):
    def __init__(self, *, request: httpx.Request) -> None:
        super().__init__(request=request, message="Request timed out.")


class APIResponseValidationError(APIError):
    def __init__(self, *, response: httpx.Response, body: Any) -> None:
        super().__init__("Response does not match the expected schema.", request=response.request, body=body)
        self.response = response
        self.status_code = response.status_code


class APIStatusError(APIError):
    def __init__(self, message: str, *, response: httpx.Response, body: Any) -> None:
        super().__init__(message, request=response.request, body=body)
        self.response = response
        self.status_code = response.status_code
        self.request_id = (
            response.headers.get("x-request-id")
            or response.headers.get("request-id")
            or (body.get("request_id") if isinstance(body, dict) else None)
        )


class BadRequestError(APIStatusError):
    pass


class AuthenticationError(APIStatusError):
    pass


class PermissionDeniedError(APIStatusError):
    pass


class NotFoundError(APIStatusError):
    pass


class ConflictError(APIStatusError):
    pass


class UnprocessableEntityError(APIStatusError):
    pass


class RateLimitError(APIStatusError):
    pass


class InternalServerError(APIStatusError):
    pass


def status_error(response: httpx.Response) -> APIStatusError:
    try:
        body = response.json()
    except ValueError:
        body = response.text
    error = body.get("error", body) if isinstance(body, dict) else body
    message = error.get("message", str(error)) if isinstance(error, dict) else str(error)
    cls = {
        400: BadRequestError,
        401: AuthenticationError,
        403: PermissionDeniedError,
        404: NotFoundError,
        409: ConflictError,
        422: UnprocessableEntityError,
        429: RateLimitError,
    }.get(response.status_code, InternalServerError if response.status_code >= 500 else APIStatusError)
    return cls(f"Error code: {response.status_code} - {message}", response=response, body=body)
