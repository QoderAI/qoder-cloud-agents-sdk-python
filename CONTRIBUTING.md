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

The Forward and Managed integration files also include six `strict_response_contract` checks using a separate client with `_strict_response_validation=True`: model, template/agent, and session lists. They send only GET requests, inspect the first page with `limit=1` where supported, and allow empty lists. An empty list checks the response envelope; item schemas are checked when items exist. Returned items must have a non-empty string ID, and `data` must be present even when empty. Existing business scenarios continue to use the default lenient response parsing.

To run only these read-only checks:

```bash
QODER_RUN_LIVE=1 QODER_LIVE_ENV_FILE=.env.live uv run pytest tests/integration -m integration -k strict_response_contract -v
```

These checks are included in the existing `test-live`, `test-live-managed`, and `test-live-all` targets. Offline regression tests use the same strict-client fixture and assertions with a mock HTTP transport to verify schema failures without credentials or network access.

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

## Changelog

Keep user-facing notes in [CHANGELOG.md](CHANGELOG.md). Add a concise bullet under
`## [Unreleased]` in the same PR as a feature, fix, deprecation, or behavior change.
Use English consistently with the public documentation, identify Forward or Managed
when relevant, and describe the effect on SDK users. Pure CI changes and internal
refactors normally need no entry; explain that in the PR checklist.

Use `### Added`, `### Fixed`, `### Changed`, `### Breaking changes`, and
`### Migration` as needed. Omit empty categories. Breaking changes must explain
what callers need to change, preferably with a small migration example. Use inline
links for issues and PRs so the extracted entry also works on the Releases page.

In the release PR, move the completed `Unreleased` notes into exactly one
`## [<version>]` section immediately below it, alongside the version-file updates.
Keep an empty `Unreleased` section for subsequent work. A date is optional; when
included, use `## [<version>] - YYYY-MM-DD`. Use the exact canonical package version
without `v`, including any prerelease suffix. Each SDK keeps its own version and
notes; a shared `batch_id` can associate coordinated releases.

Validate the file and preview a prepared version locally (Python 3.10+):

```bash
python3 .github/scripts/release_notes.py check
python3 .github/scripts/release_notes.py extract --version <version>
python3 -m unittest discover -s .github/scripts -p 'test_*.py'
```

PR CI checks the format and release automation tests. Release preflight requires a
nonempty entry for the requested version, rejects placeholders such as `TODO` or
`TBD`, and displays the extracted notes in the workflow summary before approval.
Only approved-commit notes are used; the workflow never writes back to `main`.

After public package verification succeeds, the workflow creates a GitHub Release
on the existing annotated `v<version>` tag using that entry. Prereleases are marked
as such and are not promoted to Latest. A rerun checks the remote tag's commit and
reuses a published Release only when its title, notes, and prerelease flag match.
Conflicting or draft Releases fail for manual inspection rather than being
silently overwritten. If only this final step fails, rerun the failed job to finish
the Release; the package may already be publicly available.

The `0.1.0` entry documents the existing baseline. This automation applies to future
release commits that contain the changelog and scripts; it does not move old tags
or republish historical packages.

## Release

Before the first release, create the GitHub `release` Environment with required reviewers and a deployment-branch rule limited to `main`. Add a tag ruleset for `refs/tags/v*` that blocks updates and deletions and allows creation only by the release automation identity. Update the PyPI Trusted Publisher for `QoderAI/qoder-cloud-agents-sdk-python` and `release.yml` to require the same `release` Environment. Do not dispatch the workflow until all settings are active.

1. Merge a release pull request that updates `project.version` in `pyproject.toml`, refreshes `uv.lock`, prepares the matching version entry in `CHANGELOG.md`, and passes all normal checks.
2. From the resulting `origin/main`, record the full lowercase 40-character commit SHA and dispatch the workflow from `main`. Use a 1-64 character `batch_id` that starts with a letter or digit and otherwise contains only letters, digits, `.`, `_`, or `-`:

   ```bash
   gh workflow run release.yml --ref main \
     -f version=0.2.0 \
     -f commit_sha=<40-character-main-sha> \
     -f batch_id=<safe-audit-token>
   ```

3. After approval, the workflow creates or reuses the annotated `v<version>` tag, publishes the approved wheel and sdist with PyPI Trusted Publishing, verifies their public digests, and performs a no-cache installation of the exact version and its synchronous and asynchronous imports. After verification, it publishes the changelog entry as a GitHub Release.

PyPI versions are immutable. Never reuse or overwrite one: fix forward with a new release pull request and version, and yank an unusable version when necessary. A safe rerun must use the same SHA, version, and `batch_id`; it verifies the existing PyPI files without uploading them again.

## Pull requests

Complete the pull request template, include exact verification commands and results, and identify public API, documentation, integration-test, and cross-SDK effects. Do not combine unrelated refactors with behavior changes.
