"""Opt-in service checks for the existing APIs aligned in 0.8.0."""

import uuid

import pytest

from tests.support.cleanup import finish_session_forward, finish_session_managed
from tests.support.harness import choose_model

pytestmark = pytest.mark.integration


@pytest.mark.parametrize("live_example", ["forward"], indirect=True)
def test_forward_contract_alignment_080(live_example):
    client, context = live_example
    prefix = "sdk-contract-080-" + uuid.uuid4().hex[:8]
    env = client.environments.create(name=prefix, config={"type": "cloud", "setup_script": "echo sdk-contract"})
    context.track("environment", env.id, lambda: client.environments.archive(env.id))
    assert client.environments.retrieve(env.id).config.setup_script == "echo sdk-contract"
    identity = client.identities.create(external_id=prefix, name=prefix)
    context.track("identity", identity.id, lambda: client.identities.delete(identity.id))
    template = client.templates.create(
        name=prefix,
        environment_id=env.id,
        model=choose_model(client.models.list(), context.config.model),
        max_tool_rounds=3,
    )
    context.track("template", template.id, lambda: client.templates.archive(template.id))
    assert template.max_tool_rounds == 3
    assert client.templates.update(template.id, description=prefix).max_tool_rounds == 3
    assert client.templates.update(template.id, max_tool_rounds=None).max_tool_rounds is None
    mount = {"identity_id": identity.id, "template_id": template.id, "access": "read_write"}
    store = client.memory_stores.create(name=prefix, mount=mount, idempotency_key=prefix)
    context.track("memory_store", store.id, lambda: client.memory_stores.delete(store.id))
    context.track(
        "mount",
        store.id,
        lambda: client.identities.memory_stores.detach(store.id, template_id=template.id, identity_id=identity.id),
    )
    assert client.memory_stores.create(name=prefix, mount=mount, idempotency_key=prefix).id == store.id
    mounts = client.identities.memory_stores.list(template.id, identity_id=identity.id)
    assert any(item.memory_store_id == store.id and item.access == "read_write" for item in mounts.data)
    session = client.sessions.create(identity_id=identity.id, template_id=template.id, title=prefix)
    context.track("session", session.id, lambda: finish_session_forward(client, context, session.id))
    assert client.sessions.retrieve(session.id).outcome_evaluations == []
    assert any(item.id == session.id for item in client.sessions.list(template_id=template.id, search=prefix).data)
    schedule = client.schedules.create(
        identity_id=identity.id,
        template_id=template.id,
        environment_id=env.id,
        name=prefix,
        trigger_policy={"type": "manual"},
        initial_events=[{"type": "user.message", "content": "Reply SDK-OK"}],
    )
    context.track("schedule", schedule.id, lambda: client.schedules.archive(schedule.id))
    assert schedule.source == "api" and schedule.source_session_id is None
    assert schedule.initial_events_version == 1
    updated = client.schedules.update(
        schedule.id, initial_events=[{"type": "user.message", "content": "Reply SDK-UPDATED"}]
    )
    assert updated.initial_events_version == 2


@pytest.mark.parametrize("live_example", ["managed"], indirect=True)
def test_managed_contract_alignment_080(live_example):
    client, context = live_example
    prefix = "sdk-contract-080-" + uuid.uuid4().hex[:8]
    hosted = client.environments.create(
        name=prefix + "-hosted", config={"type": "self_hosted", "setup_script": "echo sdk-contract"}
    )
    context.track("self_hosted_environment", hosted.id, lambda: client.environments.archive(hosted.id))
    assert client.environments.retrieve(hosted.id).config.setup_script == "echo sdk-contract"
    env = client.environments.create(name=prefix, config={"type": "cloud"})
    context.track("environment", env.id, lambda: client.environments.archive(env.id))
    agent = client.agents.create(name=prefix, model=choose_model(client.models.list(), context.config.model))
    context.track("agent", agent.id, lambda: client.agents.archive(agent.id))
    resources = [{"type": "git_repository", "url": "https://github.com/QoderAI/forward-quickstart.git"}]
    session = client.sessions.create(agent=agent.id, environment_id=env.id, resources=resources)
    context.track("session", session.id, lambda: finish_session_managed(client, context, session.id))
    actual = client.sessions.resources.list(session.id).data
    assert any(item.type == "git_repository" and item.url == resources[0]["url"] for item in actual)
    store = client.memory_stores.create(name=prefix)
    context.track("memory_store", store.id, lambda: client.memory_stores.delete(store.id))
    saved = client.memory_stores.retrieve(store.id)
    assert saved.status == "active"
    assert saved.entry_count == saved.total_size == 0
