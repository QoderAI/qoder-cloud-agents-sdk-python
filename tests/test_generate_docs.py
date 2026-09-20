import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "generate_docs", Path(__file__).resolve().parents[1] / "scripts" / "generate-docs.py"
)
generate_docs = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(generate_docs)


def test_normalize_source_links_strips_sha_and_line_anchor():
    raw = (
        "See [source](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/"
        "blob/1a2b3c4d5e6f7a8b9c0d/src/qca/managed/types/agent.py#L42)"
    )
    out = generate_docs.normalize_source_links(raw)
    assert "blob/main/src/qca/managed/types/agent.py" in out
    assert "#L42" not in out
    assert "1a2b3c4d5e6f7a8b9c0d" not in out


def test_normalize_source_links_strips_line_range_anchor():
    raw = "https://github.com/x/y/blob/deadbeef1234/src/qca/_client.py#L10-L20"
    out = generate_docs.normalize_source_links(raw)
    assert out.endswith("src/qca/_client.py")


def test_strip_nondeterminism_removes_local_paths():
    raw = "generated from /Users/someone/checkout/src/qca by someone at 2026-01-01T00:00:00Z"
    out = generate_docs.strip_nondeterminism(raw, repo_root="/Users/someone/checkout")
    assert "/Users/someone/checkout" not in out
    assert "2026-01-01T00:00:00Z" not in out


def test_sort_module_sections_uses_qualified_module_name():
    raw = """<a id="qca.zeta"></a>

# qca.zeta

<a id="qca.zeta.Client"></a>

## Client

<a id="qca.alpha"></a>

# qca.alpha

<a id="qca.alpha.Model"></a>

## Model
"""

    out = generate_docs.sort_module_sections(raw)

    assert out.index("# qca.alpha") < out.index("# qca.zeta")
    assert out.index('id="qca.alpha.Model"') < out.index("# qca.zeta")
