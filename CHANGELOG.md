# Changelog

User-facing changes to this SDK are recorded here. History starts at the
existing `0.1.0` release; earlier development prereleases are not listed.

## [Unreleased]

### Changed

- Forward and Managed clients, both synchronous and asynchronous, now default to a 5-second connection timeout and 600-second read, write, and connection-pool timeouts, matching Anthropic's Python SDK. SSE streams can continue beyond 10 minutes while data keeps arriving within the read timeout.

## [0.1.0]

### Added

- Forward and Managed: synchronous and asynchronous clients with typed requests and responses.
- Support pagination, SSE streaming, and file transfer on Python 3.10 and newer.
