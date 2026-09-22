# Contributing

Thank you for contributing to the Qoder Cloud Agents Python SDK.

## Development workflow

1. Create a focused branch from the latest `main`.
2. Keep each pull request limited to one independently reviewable change.
3. Use Conventional Commits, for example `fix(forward): preserve request id`.
4. Open a pull request and wait for all required checks before merging.

GitHub `main` is the source of truth. Do not develop against or copy changes from the internal CI mirror.

## Setup and checks

Python 3.10 or newer is supported. Python 3.12 is used for deterministic documentation generation.

```bash
python3 -m pip install uv
uv sync --extra dev --locked
uv run make lint
uv run make typecheck
uv run make test
uv run make docs-check
```

The default test command excludes account-backed integration tests and must not require network access or credentials.

## Test layers

- **Unit and contract tests** live under `tests/` and run with `uv run make test`.
- **Integration tests** live under `tests/integration/` and must not import implementation from `examples/`. Copy `.env.live.example` to `.env.live`, use a dedicated test account, and run `uv run make test-live-all`.
- **Examples** are runnable documentation. Tests must not import from `examples/`; use each example's `--help` mode for a no-network smoke check.

Never commit `.env.live`, tokens, credentials, generated logs, or test output. Integration scenarios must register cleanup immediately after creating a resource. Run them explicitly with `QODER_RUN_LIVE=1`; they are not part of public pull-request CI.

## API and contract changes

When adding or changing an endpoint:

1. Update the relevant modules under `src/qca/forward/` or `src/qca/managed/` and their public types.
2. Add focused contract expectations under `tests/`; do not derive the expected contract solely from the implementation under test.
3. Cover synchronous and asynchronous clients where both expose the behavior.
4. Regenerate API documentation with `uv run make docs` and verify it with `uv run make docs-check`.
5. Call out the corresponding Go and TypeScript work in the pull request, or explain why the change is language-specific.

Contract fixtures are maintained manually. A passing fixture test proves consistency with this repository, not automatically with service routes or the other SDKs.

## Compatibility conventions

The SDK intentionally keeps Qoder-branded `X-Qoder-*` metadata headers, resumable session-event streams, and Python-native synchronous and asynchronous clients. Preserve those extensions unless the change explicitly revises the public contract. Breaking public API changes require a minor-version release while the SDK remains pre-1.0 and must include migration notes.

## Pull requests

Complete the pull request template, include exact verification commands and results, and identify public API, documentation, integration-test, and cross-SDK effects. Do not combine unrelated refactors with behavior changes.
