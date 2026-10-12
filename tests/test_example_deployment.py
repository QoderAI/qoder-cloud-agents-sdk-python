from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from examples.managed.deployment import run


def deployment_fixture():
    client = Mock()
    client.environments.create.return_value.id = "env_example"
    client.models.list.return_value.data = [SimpleNamespace(id="auto", is_enabled=True)]
    client.agents.create.return_value.id = "agent_example"
    client.deployments.create.return_value.id = "dep_example"
    client.deployments.run.return_value.session_id = "sess_example"
    context = Mock()
    context.config.model = "auto"
    context.track.side_effect = lambda kind, resource_id, cleanup: resource_id
    return client, context


def event(event_id, event_type):
    return SimpleNamespace(id=event_id, type=event_type, to_json=lambda: event_id)


def test_deployment_waits_for_reply_and_completion_after_acknowledgement():
    client, context = deployment_fixture()
    initial_idle = event("initial_idle", "session.status_idle")
    reply = event("reply", "agent.message")
    completed = event("completed", "session.status_idle")
    client.sessions.events.list.side_effect = [
        [initial_idle],
        [initial_idle, reply],
        [initial_idle, reply, completed],
    ]

    run(client, context)

    assert context.pause.call_count == 2
    assert [call.args for call in context.output.call_args_list if call.args[0] == "assistant"] == [
        ("assistant", "reply")
    ]
    client.sessions.delete.assert_not_called()


def test_deployment_does_not_report_success_without_session():
    client, context = deployment_fixture()
    client.deployments.run.return_value.session_id = None
    with pytest.raises(RuntimeError, match="returned no session"):
        run(client, context)


def test_deployment_does_not_report_success_on_execution_error():
    client, context = deployment_fixture()
    client.sessions.events.list.return_value = [event("failed", "session.error")]
    with pytest.raises(RuntimeError, match="session.error"):
        run(client, context)
