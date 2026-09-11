"""Reads docs/{forward,managed}-api.md as the expected request contract.

Each reference doc states, per endpoint, its route, its full signature and where
every argument travels on the wire (path / query / body / header) plus the
pagination protocol of list operations. The suite parses those statements and
replays them against the client, so drift on either side fails.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from ._surface import UPLOAD

DOCS = Path(__file__).resolve().parents[1] / "docs"
BLOCK = re.compile(
    r"^### `([\w.]+)`\n+`(GET|POST|PUT|PATCH|DELETE) (/\S*)`\n+```python\n(.*?)\n```(.*?)(?=^### |\Z)",
    re.S | re.M,
)
SECTIONS = {"路径": "path", "查询": "query", "正文": "body", "请求头": "header"}
FIELDS = re.compile(r"`(\w+)`(?: → `([^`]+)`)?")
TIMESTAMP = datetime(2026, 1, 2, 3, 4, 5, tzinfo=timezone.utc)


def _split(text: str) -> list[str]:
    """Split on the commas that separate items rather than type arguments."""
    items, depth, start = [], 0, 0
    for index, char in enumerate(text):
        if char in "[(":
            depth += 1
        elif char in ")]":
            depth -= 1
        elif char == "," and depth == 0:
            items.append(text[start:index])
            start = index + 1
    items.append(text[start:])
    return [item.strip() for item in items if item.strip() not in ("", "*")]


def _declared(annotation: str) -> str:
    """The annotation with the optional/omitted alternatives removed."""
    if not annotation.startswith("Union["):
        return annotation
    kept = [item for item in _split(annotation[len("Union[") : -1]) if item not in ("None", "NotGiven")]
    return kept[0] if len(kept) == 1 else f"Union[{', '.join(kept)}]"


def value(name: str, annotation: str) -> Any:
    """An argument of the documented type, distinctive enough to locate on the wire."""
    declared = _declared(annotation)
    if declared == "FileTypes":
        return UPLOAD
    if declared.startswith("List["):
        item = declared[len("List[") : -1]
        return [UPLOAD] if item == "FileTypes" else [value(name, item)]
    if declared.startswith("Literal["):
        return re.findall(r"'([^']*)'", declared)[0]
    if declared.startswith("Dict["):
        return {"documented": "value"}
    if declared.startswith("Union["):
        return value(name, _split(declared[len("Union[") : -1])[0])
    return {
        "str": f"the-{name.replace('_', '-')}",
        "int": 7,
        "float": 1.5,
        "bool": True,
        "datetime": TIMESTAMP,
    }.get(declared, {"documented": "value"})


@dataclass(frozen=True)
class Documented:
    mode: str
    attribute: str
    verb: str
    template: str
    signature: str
    parameters: dict[str, str]
    placement: dict[str, dict[str, str]]
    page: str | None

    @property
    def id(self) -> str:
        return f"{self.mode}.{self.attribute}"

    @property
    def arguments(self) -> dict[str, Any]:
        return {name: value(name, annotation) for name, annotation in self.parameters.items()}


def _parse(mode: str, match: re.Match[str]) -> Documented:
    attribute, verb, template, signature, notes = match.groups()
    arguments = signature[signature.index("(") + 1 : signature.rindex(") ->")]
    parameters = {}
    for item in _split(arguments):
        declaration = item.split(" = ")[0]
        name, annotation = declaration.split(": ", 1)
        parameters[name] = annotation
    placement: dict[str, dict[str, str]] = {section: {} for section in SECTIONS.values()}
    page = None
    for line in notes.splitlines():
        label, _, rest = line.partition("：")
        if label in SECTIONS:
            placement[SECTIONS[label]] = {name: wire or name for name, wire in FIELDS.findall(rest)}
        elif label == "分页协议":
            page = rest.split("`")[1]
    return Documented(mode, attribute, verb, template, signature, parameters, placement, page)


def documented() -> list[Documented]:
    found = []
    for mode in ("forward", "managed"):
        text = (DOCS / f"{mode}-api.md").read_text()
        found.extend(_parse(mode, match) for match in BLOCK.finditer(text))
    return sorted(found, key=lambda entry: entry.id)


DOCUMENTED = documented()


def documented_id(entry: Documented) -> str:
    return entry.id
