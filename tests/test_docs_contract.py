"""The reference docs and the client, checked against each other.

docs/forward-api.md and docs/managed-api.md are the published contract: they name
every endpoint's route, signature, argument placement and pagination protocol.
These tests replay those statements, so a client change that the docs do not
describe — or a doc claim the client does not honour — fails here.
"""

import inspect
import json

import pytest

from ._docs import DOCUMENTED, documented_id
from ._surface import (
    CONTROL_PARAMS,
    ENDPOINTS,
    body_keys,
    call,
    client_for,
    close_client,
    multipart_values,
    plain_client,
    release,
    responder,
)

MODES = ("forward", "managed")
SDK = {endpoint.id: endpoint for endpoint in ENDPOINTS}
SHA = "0" * 64
# PreconditionParam is a tagged dict; its reference section spells out the one form.
ARGUMENTS = {
    "managed.memory_stores.memories.update": {
        "content_sha256": SHA,
        "precondition": {"type": "content_sha256", "content_sha256": SHA},
    }
}
# Two endpoints rewrite their body as their reference sections describe. The
# rewrites themselves are asserted by the last two tests in this file.
BODY = {
    "forward.schedules.archive_many": {"schedule_ids", "scope"},
    "managed.memory_stores.memories.update": {"content_sha256", "metadata", "content", "path"},
}


def _method(entry, client):
    return getattr(type(SDK[entry.id].resource(client)), entry.attribute.rsplit(".", 1)[-1])


@pytest.mark.parametrize("mode", MODES)
def test_docs_and_client_describe_the_same_endpoints(mode):
    assert {entry.attribute for entry in DOCUMENTED if entry.mode == mode} == {
        endpoint.attribute for endpoint in ENDPOINTS if endpoint.mode == mode
    }


@pytest.mark.parametrize("entry", DOCUMENTED, ids=documented_id)
async def test_documented_signature_matches_the_client(entry):
    client = plain_client(entry.mode, False)
    try:
        signature = inspect.signature(_method(entry, client))
        assert {
            name: str(parameter.annotation)
            for name, parameter in signature.parameters.items()
            if name not in ("self", *CONTROL_PARAMS)
        } == entry.parameters
        assert entry.signature.endswith(f") -> {signature.return_annotation}: ...")
    finally:
        await close_client(client, False)


@pytest.mark.parametrize("entry", DOCUMENTED, ids=documented_id)
def test_documented_route_matches_the_client(entry):
    endpoint = SDK[entry.id]
    assert (entry.verb, entry.template) == (endpoint.verb, endpoint.template)


@pytest.mark.parametrize("entry", DOCUMENTED, ids=documented_id)
def test_every_documented_parameter_is_given_a_place(entry):
    placed = [name for fields in entry.placement.values() for name in fields]
    assert sorted(placed) == sorted(entry.parameters)
    assert len(placed) == len(set(placed)), "a parameter is listed under two sections"


@pytest.mark.parametrize("entry", DOCUMENTED, ids=documented_id)
@pytest.mark.parametrize("async_", [False, True], ids=["sync", "async"])
async def test_documented_arguments_travel_where_the_docs_say(entry, async_):
    """Send every documented argument at once and locate each one on the wire."""
    endpoint, recorded = SDK[entry.id], []
    arguments = {**entry.arguments, **ARGUMENTS.get(entry.id, {})}
    client = client_for(endpoint, async_, responder(recorded, endpoint))
    try:
        await release(await call(endpoint, client, raw=True, **arguments), async_)
    finally:
        await close_client(client, async_)

    request = recorded[0]
    for name, wire in entry.placement["path"].items():
        assert "{" + wire + "}" in entry.template, f"{name} is not a placeholder in {entry.template}"
        assert arguments[name] in request.url.path
    for name, wire in entry.placement["query"].items():
        assert wire in request.url.params, f"{name} is missing from the query string"
    for name, wire in entry.placement["header"].items():
        assert wire in request.headers, f"{name} is missing from the request headers"
    expected = BODY.get(entry.id, set(entry.placement["body"].values()))
    assert body_keys(request) | set(multipart_values(request)) == expected


@pytest.mark.parametrize("entry", DOCUMENTED, ids=documented_id)
async def test_documented_pagination_protocol_matches_the_client(entry):
    endpoint = SDK[entry.id]
    if entry.page is None:
        assert endpoint.kind != "page", f"{entry.id} paginates but documents no protocol"
        return
    client = client_for(endpoint, False, responder([], endpoint))
    try:
        page = await call(endpoint, client)
        assert page._style == entry.page
    finally:
        await close_client(client, False)


def test_archive_many_sends_the_documented_scope():
    endpoint, recorded = SDK["forward.schedules.archive_many"], []
    with client_for(endpoint, False, responder(recorded, endpoint)) as client:
        client.schedules.with_raw_response.archive_many(schedule_ids=["sched_one", "sched_two"])
    assert json.loads(recorded[0].content) == {"scope": "by_schedule_ids", "schedule_ids": ["sched_one", "sched_two"]}


def test_memory_precondition_folds_into_content_sha256():
    endpoint, recorded = SDK["managed.memory_stores.memories.update"], []
    with client_for(endpoint, False, responder(recorded, endpoint)) as client:
        memories = client.memory_stores.memories
        memories.with_raw_response.update(
            "mem", memory_store_id="store", precondition={"type": "content_sha256", "content_sha256": SHA}
        )
        with pytest.raises(ValueError, match="Conflicting memory content hashes"):
            memories.update(
                "mem",
                memory_store_id="store",
                content_sha256=SHA,
                precondition={"type": "content_sha256", "content_sha256": "f" * 64},
            )
        with pytest.raises(ValueError, match="precondition"):
            memories.update("mem", memory_store_id="store", precondition={"type": "version"})
    assert json.loads(recorded[0].content) == {"content_sha256": SHA}
    assert len(recorded) == 1
