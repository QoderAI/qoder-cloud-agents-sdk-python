import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "docs_check", Path(__file__).resolve().parents[1] / "scripts" / "docs-check.py"
)
docs_check = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(docs_check)


def test_source_link_assertion_flags_sha_and_line_anchor():
    bad = "[src](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/abc1234/src/qca/x.py#L5)"
    good = "[src](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/x.py)"
    assert docs_check.assert_source_links_normalized([bad])  # non-empty violations
    assert docs_check.assert_source_links_normalized([good]) == []


def test_core_surface_missing_is_reported():
    assert set(docs_check.assert_core_surface_present(["nothing here"])) >= {"Forward", "Managed", "APIError"}
    present = ["class Forward", "class AsyncForward", "class Managed", "class AsyncManaged", "class APIError"]
    assert docs_check.assert_core_surface_present(present) == []
