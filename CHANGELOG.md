# Changelog

User-facing changes to this SDK are recorded here. History starts at the
existing `0.1.0` release; earlier development prereleases are not listed.

## [Unreleased]

## [0.8.0]

### Fixed

- Align existing Managed Session and Deployment resource types with generic HTTP(S) `git_repository`, including write-only credentials, branch/commit checkout, and optional GitHub authorization for public repositories.
- Add Forward Template `max_tool_rounds`, Batch `ignore_idle_window` / `queue_reason`, and Session list `search`; preserve omitted, null, false, and zero values according to each API contract.
- Expose Forward Session outcome evaluations and Thread statistics/Credits, Schedule and Run source/input-version metadata, and trigger time boundaries.
- Support Forward MemoryStore creation with a native `mount` (Identity, Template, and optional access), preserving the create request's idempotency key for retries.
- Expose self-hosted Environment setup scripts, Forward Environment binding metadata, Managed MemoryStore status/count/size, and Dream output file paths.
- Decode flat `agent.artifact_delivered` fields and diagnostic `session.error.error.qoder_error_code` in Managed event history, Session SSE, and Thread SSE. No additional API endpoints are introduced.

### Migration

- Omitting `max_tool_rounds` on update preserves the configured limit; null clears it. `ignore_idle_window` accepts a boolean, with false as the server default.
- Treat an absent Schedule Run input version or Thread usage as unknown, not zero. Use `retry_status` rather than `qoder_error_code` to decide whether execution can retry.

## [0.7.0]

### Fixed

- Align Managed Session budgets with the official decimal-string `max_credit_cost` contract, shared by Deployment budgets. The limit covers cumulative model and sandbox Credits; reaching it rejects the next user message without interrupting the current turn.
- Expose Managed and Forward Session `model_credits`, `sandbox_runtime_credits`, and `total_credits`; decode top-level `session.usage` Credits and per-call `model_usage.credits` / compaction `usage.credits`. Session usage may be absent. Legacy response token/list-cost fields remain available.
- Route Identity ownership through query parameters on existing Forward Environment, Skill/Version, Vault/Credential, and File operations, including multipart uploads and content downloads.
- Allow existing channel pairing creation with either a code or `channel_pairing_id`, and expose pairing scope details. No additional API endpoints are introduced.

### Migration

- **Breaking budget field change:** Replace `{"type": "limit", "max_list_cost": {...}}` with `{"type": "limit", "max_credit_cost": "100.00"}`. Amounts are positive decimal strings, not currency objects. Omitting a budget update preserves the limit; explicit null removes it.
- Consume the three top-level Credits fields from `session.usage` events. Replace cumulative snapshots rather than adding them; compaction Credits are already included in Session totals.
- Pass the keyword argument `identity_id="idn_..."` to resource methods. Use this only with a PAT. With a SAT, omit `identity_id`; the server infers ownership from the token and rejects explicit values (including an empty string).
- Channel pairing requests must provide exactly one of `code` or `channel_pairing_id`; existing code-based calls remain supported.

## [0.6.0]

### Added

- Forward Drive Beta: typed directory listing, upload/download signed URLs, entry deletion and Drive clearing, with required Identity scope, independent cursor pagination, service ordering and canonical directory query encoding.
- Template `managed_tool_config.enabled_tools` in create/update requests and responses, including omission, empty-list and null semantics. Runnable Drive examples keep storage requests separate from QCA authentication; opt-in CN/Global lifecycle tests cover PAT, admin SAT and Identity SAT.

## [0.5.0]

### Added

- Forward admin and Identity SAT issuance and Forward SAT revocation, using explicit per-call SA Key authentication, typed issuance/revocation metadata, and no automatic retries. Existing platform credentials and PAT/SAT business authentication remain unchanged.
- Forward Realtime (Beta): synchronous/asynchronous Conversation creation with stable idempotency keys, independent history pages, and WebSocket connections that wait for readiness, preserve typed/unknown events, reuse PAT/SAT/Credential authentication, and expose text/PCM16, interruption, playback receipt, and verified graceful-close helpers.
- Bounded Realtime queues, protocol/timeout errors, opt-in CN/Global connection and history smoke checks, and text/PCM/history examples. Adds websockets 16.x while retaining Python 3.10 support; no automatic reconnect/replay or Realtime Template configuration API.
- Realtime SA access requires a Forward-issued bound SAT and a Realtime-enabled Template; a platform SAT from `ServiceAccountCredential` alone does not establish the required Forward binding.

### Fixed

- Accept string-valued Managed model effort in Agent and Session responses, including strict response validation, while retaining support for structured effort values.

## [0.4.0] - 2026-10-12

### Added

- Read-only SA Key and SAT authentication examples, plus explicit PAT/SA selection for existing business examples without duplicating scenarios.
- Shared PAT and Service Account authentication for Forward and Managed, including explicit SA mode, direct SAT access, and lazy SA Key exchange with an instance-owned cache, early renewal, concurrent request sharing, and failure cooldown.
- Separate CN/Global SA authentication smoke checks for both API surfaces, covering automatic exchange and direct SAT use, plus opt-in write/read, Session SSE and cleanup verification.

### Changed

- Support `QODER_ACCESS_TOKEN` for the selected mode. SA never falls back to `QODER_PAT`; ordinary clients never implicitly read `QODER_SA_KEY`.
- Add `access_token`, `auth_mode`, and matching sync/async SA credentials. Client copies retain authentication mode and source.
- Explicit credentials now take precedence over ambient PAT. Explicit `pat` plus a legacy custom credential retains PAT precedence.

### Migration

- For an existing SAT, select SA mode and supply the neutral token option. For automatic exchange, construct a Service Account credential with explicit region and scopes; do not combine it with a static token. Existing PAT calls require no new mode argument.
- Applications that configured both an ambient PAT and an explicit credential now use the credential. Remove the credential and configure an explicit PAT to retain personal-user authentication.

### Fixed

- The Deployment example waits for an assistant reply and completion before cleaning up its session, and fails when the run has no session or execution stops with an error.

## [0.3.0]

### Added

- Forward Vault Credential updates for secret rotation and metadata merge patches, with automatic retries disabled for write-only updates.
- Forward Usage aggregation by Identity and Template using hourly `start_at` / `end_at` windows in Asia/Shanghai, with fractional `active_seconds` and multi-ID filters. Legacy timestamp parameters are not exposed.
- Managed Session cancellation with the lightweight acknowledgement for both active and idle sessions, plus deployment-scoped Run listing and retrieval.

## [0.2.0] - 2026-09-24

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
