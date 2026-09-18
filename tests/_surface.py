"""Introspection over the public client surface.

Every resource method declares its HTTP verb and path template on the first line
of its docstring, and its inputs in its signature. These helpers read both so the
suite can exercise all endpoints without checked-in snapshots.
"""

from __future__ import annotations

import inspect
import json
import re
from dataclasses import dataclass
from functools import cached_property
from importlib import import_module
from typing import Any, Callable, Iterator

import httpx

from qca import AsyncForward, AsyncManaged, Forward, Managed
from qca.common._response import AsyncBinaryAPIResponse, BinaryAPIResponse
from qca.common._streaming import AsyncStream, Stream
from qca.common.pagination import AsyncPage, SyncPage

DECLARATION = re.compile(r"^(GET|POST|PUT|PATCH|DELETE) (/[^\s.]*)\.")
CONTROL_PARAMS = ("extra_headers", "extra_query", "extra_body", "timeout")
HANDWRITTEN_RESOURCE_METHODS = {"sessions.events.resumable_stream"}
CLIENTS = {
    ("forward", False): Forward,
    ("forward", True): AsyncForward,
    ("managed", False): Managed,
    ("managed", True): AsyncManaged,
}
CONTAINERS = {
    ("page", False): SyncPage,
    ("page", True): AsyncPage,
    ("stream", False): Stream,
    ("stream", True): AsyncStream,
    ("binary", False): BinaryAPIResponse,
    ("binary", True): AsyncBinaryAPIResponse,
}
BASE_URL = "https://api.test/api/v1"
DOWNLOAD_URL = "https://storage.test/blob?signature=example"
TOKEN = "surface-token"
UPLOAD = ("skill/SKILL.md", b"surface upload")


def _value(name: str, annotation: str) -> Any:
    """A syntactically valid argument for a required parameter."""
    if annotation in ("FileTypes", "List[FileTypes]"):
        return [UPLOAD] if annotation.startswith("List[") else UPLOAD
    if annotation.startswith("List["):
        return []
    if annotation.startswith("Literal["):
        return re.findall(r"'([^']*)'", annotation)[0]
    if annotation == "str" or annotation.startswith("Union[str"):
        return f"the-{name.replace('_', '-')}"
    return {}


@dataclass(frozen=True)
class Endpoint:
    mode: str
    attribute: str
    verb: str
    template: str
    returns: str
    arguments: dict[str, Any]
    path_params: tuple[str, ...]

    @property
    def id(self) -> str:
        return f"{self.mode}.{self.attribute}"

    @property
    def kind(self) -> str:
        for marker, kind in (("Page[", "page"), ("Paginator[", "page"), ("Stream[", "stream")):
            if marker in self.returns:
                return kind
        if "BinaryAPIResponse" in self.returns:
            return "binary"
        return "empty" if self.returns == "None" else "model"

    @property
    def path(self) -> str:
        """The template with every placeholder replaced by its argument."""
        path = self.template
        for name in self.path_params:
            path = path.replace("{" + name + "}", self.arguments[name])
        return path

    @property
    def inputs(self) -> dict[str, Any]:
        """Required arguments that are not consumed by the path."""
        return {k: v for k, v in self.arguments.items() if k not in self.path_params}

    @property
    def nullable(self) -> bool:
        return self.returns.startswith("Optional[")

    def response_type(self, async_: bool) -> Any:
        if self.kind == "empty":
            return type(None)
        if self.kind != "model":
            return CONTAINERS[self.kind, async_]
        name = self.returns.removeprefix("Optional[").removesuffix("]")
        return getattr(import_module(f"qca.{self.mode}.types"), name)

    def resource(self, client: Any) -> Any:
        resource = client
        for name in self.attribute.split(".")[:-1]:
            resource = getattr(resource, name)
        return resource


def _methods(resource: Any, prefix: str = "") -> Iterator[tuple[str, Any]]:
    for name, value in vars(type(resource)).items():
        if name.startswith("_"):
            continue
        attribute = f"{prefix}.{name}" if prefix else name
        if isinstance(value, cached_property):
            yield from _methods(getattr(resource, name), attribute)
        elif prefix and inspect.isfunction(value):
            yield attribute, value


def method_names(client: Any) -> set[str]:
    return {attribute for attribute, _ in _methods(client)}


def _endpoint(mode: str, attribute: str, function: Any) -> Endpoint:
    summary = (function.__doc__ or "").strip()
    declaration = DECLARATION.match(summary)
    assert declaration, f"{mode}.{attribute} must document its route on the first docstring line: {summary!r}"
    verb, template = declaration.groups()
    signature = inspect.signature(function)
    arguments = {
        name: _value(name, str(parameter.annotation))
        for name, parameter in signature.parameters.items()
        if name not in ("self", *CONTROL_PARAMS) and parameter.default is inspect.Parameter.empty
    }
    placeholders = tuple(re.findall(r"\{(\w+)\}", template))
    missing = [name for name in placeholders if name not in arguments]
    assert not missing, f"{mode}.{attribute} does not accept path parameters {missing}"
    return Endpoint(
        mode=mode,
        attribute=attribute,
        verb=verb,
        template=template,
        returns=str(signature.return_annotation),
        arguments=arguments,
        path_params=placeholders,
    )


def endpoints() -> list[Endpoint]:
    found = []
    for mode in ("forward", "managed"):
        client = CLIENTS[mode, False](pat=TOKEN)
        found.extend(
            _endpoint(mode, attribute, function)
            for attribute, function in _methods(client)
            if attribute not in HANDWRITTEN_RESOURCE_METHODS
        )
        client.close()
    return sorted(found, key=lambda endpoint: endpoint.id)


ENDPOINTS = endpoints()


def endpoint_id(endpoint: Endpoint) -> str:
    return endpoint.id


def responder(
    recorded: list[httpx.Request], endpoint: Endpoint | None = None, status: int = 200
) -> Callable[[httpx.Request], httpx.Response]:
    """Answer one endpoint. Bodies stay minimal; the tests assert on requests."""
    payload: dict[str, Any] = {}
    if endpoint is not None and endpoint.kind == "page":
        payload = {"data": [], "has_more": False}
    elif endpoint is not None and endpoint.kind == "binary":
        payload = {"url": DOWNLOAD_URL}

    def handle(request: httpx.Request) -> httpx.Response:
        recorded.append(request)
        if request.url.host == "storage.test":
            return httpx.Response(200, content=b"blob")
        if status != 200:
            return httpx.Response(
                status,
                json={"error": {"type": "not_found_error", "code": "missing", "message": "missing resource"}},
                headers={"x-request-id": "req-surface"},
            )
        return httpx.Response(200, json=payload, headers={"x-request-id": "req-surface"})

    return handle


def client_for(endpoint: Endpoint, async_: bool, handle: Callable[[httpx.Request], httpx.Response], **kwargs: Any):
    transport = httpx.MockTransport(handle)
    http_client = httpx.AsyncClient(transport=transport) if async_ else httpx.Client(transport=transport)
    return CLIENTS[endpoint.mode, async_](
        pat=TOKEN,
        base_url=f"{BASE_URL}/{endpoint.mode}",
        max_retries=0,
        http_client=http_client,
        **kwargs,
    )


def plain_client(mode: str, async_: bool) -> Any:
    """A client for tests that only introspect the resource tree."""
    return CLIENTS[mode, async_](pat=TOKEN)


async def call(endpoint: Endpoint, client: Any, *, raw: bool = False, **overrides: Any) -> Any:
    resource = endpoint.resource(client)
    if raw:
        resource = resource.with_raw_response
    result = getattr(resource, endpoint.attribute.rsplit(".", 1)[-1])(**{**endpoint.arguments, **overrides})
    return await result if hasattr(result, "__await__") else result


async def release(result: Any, async_: bool) -> None:
    close = getattr(result, "close", None)
    if close is None:
        return
    if async_:
        await close()
    else:
        close()


async def close_client(client: Any, async_: bool) -> None:
    if async_:
        await client.close()
    else:
        client.close()


def multipart_values(request: httpx.Request) -> dict[str, list[Any]]:
    from email.parser import BytesParser
    from email.policy import default

    if "multipart" not in request.headers.get("content-type", ""):
        return {}
    message = BytesParser(policy=default).parsebytes(
        b"Content-Type: " + request.headers["content-type"].encode() + b"\r\n\r\n" + request.content
    )
    values: dict[str, list[Any]] = {}
    for part in message.iter_parts():
        content = part.get_payload(decode=True).decode()
        if part.get_filename():
            content = {"filename": part.get_filename(), "content": content}
        values.setdefault(part.get_param("name", header="content-disposition"), []).append(content)
    return values


def body_keys(request: httpx.Request) -> set[str]:
    if "json" not in request.headers.get("content-type", "") or not request.content:
        return set()
    return set(json.loads(request.content))


def carriers(request: httpx.Request, name: str, value: Any) -> set[str]:
    """Where a request carries an argument. Headers are renamed on the wire, so match values."""
    found = set()
    if name in request.url.params:
        found.add("query")
    if isinstance(value, str) and value in request.headers.values():
        found.add("header")
    if name in body_keys(request):
        found.add("body")
    if name in multipart_values(request):
        found.add("multipart")
    return found
