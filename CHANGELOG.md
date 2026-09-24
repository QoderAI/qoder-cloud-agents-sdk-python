# Changelog

User-facing changes to this SDK are recorded here. History starts at the
existing `0.1.0` release; earlier development prereleases are not listed.

## [Unreleased]

### Added

- Export `RequestTooLargeError` for HTTP 413 and `OverloadedError` for HTTP 529 from `qca` and `qca.common`, matching Anthropic's Python SDK.
- Add `_strict_response_validation=True` to all four clients to require Pydantic validation of responses, including pagination and SSE. The setting is retained by `with_options` and response views.

### Changed

- **Breaking:** Responses now use lenient model construction by default, matching Anthropic's Python SDK. Unexpected field types are preserved instead of raising `APIResponseValidationError`; nested models, extra fields, and request IDs remain available. Enable `_strict_response_validation=True` to retain the previous schema validation behavior. Invalid JSON and invalid download URLs still raise in either mode.
- **Breaking:** HTTP 529 now raises `OverloadedError`, which inherits directly from `APIStatusError`, rather than `InternalServerError`. Callers catching `InternalServerError` for overloads should also catch `OverloadedError` or use `APIStatusError`.
- Honor positive `Retry-After` and `Retry-After-Ms` delays above 60 seconds, capped at 4,294,967 seconds. Zero and negative delays use exponential backoff; numeric millisecond headers take precedence. Retry eligibility is unchanged.
- Forward and Managed clients, both synchronous and asynchronous, now default to a 5-second connection timeout and 600-second read, write, and connection-pool timeouts, matching Anthropic's Python SDK. SSE streams can continue beyond 10 minutes while data keeps arriving within the read timeout.

## [0.1.0]

### Added

- Forward and Managed: synchronous and asynchronous clients with typed requests and responses.
- Support pagination, SSE streaming, and file transfer on Python 3.10 and newer.
