# Documentation

The API reference under `docs/api/` is **generated** from the public source of
`src/qca` and committed to the repository. Do not hand-edit files under
`docs/api/` — they are overwritten on every regeneration.

Regenerate and verify:

```bash
make docs          # regenerate docs/api/ from src/qca
make docs-check    # regenerate + drift/link/snippet checks (offline)
```

## How it works (pinned from the Task 1 spike)

- Tool: [`pydoc-markdown`](https://pypi.org/project/pydoc-markdown/) `>=4,<5`
  (locked in `uv.lock`), run through `uv` on a pinned Python 3.12 for a
  reproducible interpreter.
- Loader `python` uses **static docspec parsing** — it never imports `src/qca`,
  so `if TYPE_CHECKING:` forward-ref field types cannot cause import errors.
- The `markdown` renderer emits a **single** `docs/api/reference.md` (its
  `filename:` option), not a multi-page tree.
- `filter.documented_only: false` is required: the Stainless-style client
  classes (`Forward`/`AsyncForward`/`Managed`/`AsyncManaged`) and the field-only
  pydantic models carry no class docstring, so `documented_only: true` would drop
  the entire real surface. The filter `expression` drops imported-name
  `Indirection`s (`datetime`, `Optional`, `TYPE_CHECKING`, ...) that would
  otherwise render as spurious `## <name>` headers on every module page.
- The GitHub `source_linker` natively emits `blob/<HEAD-sha>/<path>#L<line>`.
  `scripts/generate-docs.py` normalizes every link to `blob/main/<path>` (no
  commit SHA, no line anchor) so regenerating after a commit produces no churn.
- Determinism: on a fixed commit + pinned version, two raw runs are
  byte-identical; the only per-commit variance is the source-link SHA / line
  anchor, which normalization collapses. This is what the `docs-check` drift gate
  (`git diff --exit-code -- docs/api`) relies on.
