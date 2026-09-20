#!/usr/bin/env python3
"""Deterministic API reference generator: wraps pydoc-markdown and normalizes output.

Runs offline. Reads only public symbols from src/qca via pydoc-markdown's docspec
static parsing (loader=python). Wipes docs/api/ before regenerating so deleted or
renamed symbols surface as a git diff. Post-processes every generated file so that
re-running on the same commit + same pydoc-markdown version yields byte-identical
output: source links are normalized to a main-ref, file-level GitHub URL with no
commit SHA and no line anchor, and any absolute paths / timestamps are stripped.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS_API = REPO_ROOT / "docs" / "api"
CONFIG = REPO_ROOT / "pydoc-markdown.yml"

_SHA_BLOB = re.compile(r"(/blob/)[0-9a-fA-F]{7,40}(/)")
_LINE_ANCHOR = re.compile(r"(\.py)#L\d+(?:-L\d+)?")
_ISO_TS = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z?")
_MODULE_SECTION_START = re.compile(r'^<a id="(qca(?:\.[^"]+)*)"></a>\n\n# ', re.MULTILINE)


def normalize_source_links(text: str) -> str:
    text = _SHA_BLOB.sub(r"\1main\2", text)
    text = _LINE_ANCHOR.sub(r"\1", text)
    return text


def sort_module_sections(text: str) -> str:
    starts = list(_MODULE_SECTION_START.finditer(text))
    if not starts:
        return text

    prefix = text[: starts[0].start()].rstrip()
    sections = [
        (match.group(1), text[match.start() : next_start])
        for match, next_start in zip(starts, [m.start() for m in starts[1:]] + [len(text)])
    ]
    body = "\n\n".join(section.rstrip() for _, section in sorted(sections))
    return f"{prefix}\n\n{body}\n" if prefix else f"{body}\n"


def strip_nondeterminism(text: str, repo_root: str) -> str:
    text = text.replace(repo_root, "")
    text = _ISO_TS.sub("", text)
    return text


def _pydoc_markdown_cmd() -> list[str]:
    # pydoc-markdown ships a console script (pydoc_markdown.main:cli); the package has
    # no __main__, so `python -m pydoc_markdown` fails. Prefer the console script that
    # sits next to the running interpreter (works under `uv run`), else fall back to PATH.
    candidate = Path(sys.executable).parent / "pydoc-markdown"
    exe = str(candidate) if candidate.exists() else "pydoc-markdown"
    return [exe, str(CONFIG)]


def _run_pydoc_markdown() -> None:
    # pydoc-markdown reads CONFIG and writes docs/api/reference.md (renderer.filename).
    subprocess.run(_pydoc_markdown_cmd(), cwd=REPO_ROOT, check=True)


def _post_process() -> None:
    for md in sorted(DOCS_API.rglob("*.md")):
        original = md.read_text(encoding="utf-8")
        fixed = sort_module_sections(normalize_source_links(original))
        fixed = strip_nondeterminism(fixed, str(REPO_ROOT)).rstrip() + "\n"
        if fixed != original:
            md.write_text(fixed, encoding="utf-8")


def main() -> int:
    if DOCS_API.exists():
        for p in sorted(DOCS_API.rglob("*"), reverse=True):
            p.unlink() if p.is_file() else p.rmdir()
    DOCS_API.mkdir(parents=True, exist_ok=True)
    _run_pydoc_markdown()
    _post_process()
    if not any(DOCS_API.rglob("*.md")):
        print("generate-docs: FAIL — no markdown produced", file=sys.stderr)
        return 1
    print(f"generate-docs: wrote {sum(1 for _ in DOCS_API.rglob('*.md'))} file(s) under docs/api/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
