#!/usr/bin/env python3
"""docs-check gate (offline).

Regenerates docs/api/ deterministically, then fails (non-zero) if any of:
  - committed docs/api differs from freshly generated output (drift);
  - any generated source link is not a main-ref, file-level URL (has a commit
    SHA or a #Lxx line anchor);
  - core public surface (Forward/AsyncForward/Managed/AsyncManaged/APIError) is
    absent from the generated output (coarse non-empty/coverage sanity, consuming
    what pydoc-markdown produced -- not a self-built module map);
  - an internal relative link in docs/api resolves to nothing (external http(s)
    links are reported, never blocking);
  - a README ```python snippet fails to byte-compile (compile-only; live examples
    are never executed).
"""

from __future__ import annotations

import ast
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS_API = REPO_ROOT / "docs" / "api"
README = REPO_ROOT / "README.md"
CORE = ["Forward", "AsyncForward", "Managed", "AsyncManaged", "APIError"]

_SHA_BLOB = re.compile(r"/blob/[0-9a-fA-F]{7,40}/")
_LINE_ANCHOR = re.compile(r"\.py#L\d+")


def assert_source_links_normalized(md_texts: list[str]) -> list[str]:
    violations: list[str] = []
    for t in md_texts:
        if _SHA_BLOB.search(t) or _LINE_ANCHOR.search(t):
            violations.append(t[:120])
    return violations


def assert_core_surface_present(md_texts: list[str]) -> list[str]:
    blob = "\n".join(md_texts)
    return [name for name in CORE if name not in blob]


def _fail(msg: str, detail: str = "") -> None:
    print(f"docs-check: FAIL -- {msg}", file=sys.stderr)
    if detail:
        print(detail, file=sys.stderr)
    sys.exit(1)


def _regenerate() -> None:
    subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "generate-docs.py")],
        cwd=REPO_ROOT,
        check=True,
    )


def _assert_no_drift() -> None:
    diff = subprocess.run(["git", "diff", "--exit-code", "--", "docs/api"], cwd=REPO_ROOT)
    untracked = subprocess.run(
        ["git", "ls-files", "--others", "--exclude-standard", "--", "docs/api"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    if diff.returncode != 0 or untracked.stdout.strip():
        _fail(
            "committed docs/api differs from generated output; run `make docs` and commit",
            untracked.stdout,
        )


def _md_texts() -> list[str]:
    return [p.read_text(encoding="utf-8") for p in sorted(DOCS_API.rglob("*.md"))]


def _check_internal_links() -> None:
    broken: list[str] = []
    ext = 0
    link_re = re.compile(r"\]\(([^)]+)\)")
    for path in sorted(DOCS_API.rglob("*.md")):
        content = path.read_text(encoding="utf-8")
        for target in link_re.findall(content):
            t = target.strip().strip("<>")
            if not t or t.startswith(("#", "mailto:")):
                continue
            if re.match(r"^(https?:)?//", t) or t.startswith("/"):
                ext += 1
                continue
            clean = t.split("#")[0].split("?")[0]
            if clean and not (path.parent / clean).exists():
                broken.append(f"{path.relative_to(REPO_ROOT)} -> {target}")
    if broken:
        _fail(f"{len(broken)} dangling internal link(s)", "\n".join(broken))
    print(f"docs-check: internal links OK; {ext} external link(s) reported (not blocking)")


def _check_readme_snippets() -> None:
    lines = README.read_text(encoding="utf-8").split("\n")
    snippets: list[str] = []
    cur: list[str] | None = None
    for line in lines:
        if cur is None:
            if line.strip() in ("```python", "```py"):
                cur = []
        elif line.strip() == "```":
            snippets.append("\n".join(cur))
            cur = None
        else:
            cur.append(line)
    if not snippets:
        print("docs-check: no README python snippets")
        return
    # compile-only (never executed); PyCF_ALLOW_TOP_LEVEL_AWAIT tolerates illustrative
    # top-level await / async-with fragments while still catching real syntax errors.
    for i, s in enumerate(snippets):
        try:
            compile(s + "\n", f"<README snippet #{i}>", "exec", flags=ast.PyCF_ALLOW_TOP_LEVEL_AWAIT)
        except SyntaxError as e:
            _fail(f"README python snippet #{i} failed to compile", f"{e}")
    print(f"docs-check: {len(snippets)} README python snippet(s) compiled")


def main() -> int:
    _regenerate()
    _assert_no_drift()
    texts = _md_texts()
    if not texts:
        _fail("docs/api is empty")
    v = assert_source_links_normalized(texts)
    if v:
        _fail(f"{len(v)} non-normalized source link(s) (SHA or #Lxx)", "\n".join(v))
    missing = assert_core_surface_present(texts)
    if missing:
        _fail(f"core public surface missing from docs: {missing}")
    _check_internal_links()
    _check_readme_snippets()
    print("docs-check: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
