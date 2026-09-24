"""测试专用的断言层（TurnResult/wait_reply/turn）。

这是从 examples/common/live.py 净移出的断言层——examples 侧不再保留。
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from qca import APIError, Forward, Managed
from qca.common import BaseModel
from tests.support.harness import Run, name, safe_error


def assert_readonly_list_response(client: Forward | Managed, resource: str) -> None:
    # Forward's model catalog has no limit parameter; other lists inspect only the first page.
    options = {} if isinstance(client, Forward) and resource == "models" else {"limit": 1}
    try:
        result = getattr(client, resource).list(**options)
    except APIError as error:
        raise AssertionError(safe_error(error, client.pat or "")) from None
    assert isinstance(result, BaseModel), f"{resource} must return a response model"
    assert "data" in result.model_fields_set, f"{resource} response must include data"
    assert isinstance(result.data, list), f"{resource} data must be a list"
    for item in result.data:
        assert isinstance(item.id, str) and item.id, f"{resource} item must have a non-empty string id"


@dataclass
class TurnResult:
    text: str = ""
    last_id: str = ""
    tool_used: bool = False
    complete: bool = False

    def observe(self, event: Any) -> None:
        if hasattr(event, "to_dict"):
            event = event.to_dict(mode="json")
        kind = event.get("type")
        if event.get("id"):
            self.last_id = event["id"]
        if kind in ("session.error", "session.status_terminated"):
            raise AssertionError(f"Execution failed: {kind}, event_id={self.last_id}")
        if kind in ("agent.tool_use", "agent.mcp_tool_use"):
            self.tool_used = True
        elif kind == "agent.message":
            # Only the latest completed assistant message can satisfy assertions.
            self.text = "\n".join(
                block.get("text", "") for block in event.get("content", []) if block.get("type") == "text"
            )
        elif kind == "session.status_idle":
            reason = event.get("stop_reason")
            reason = reason.get("type") if isinstance(reason, dict) else reason
            if reason not in (None, "", "end_turn", "stop_sequence"):
                raise AssertionError(f"Execution stopped early: {reason}, event_id={self.last_id}")
            self.complete = bool(self.text)

    def verify(self, expected: list[str], require_tool: bool = False) -> None:
        if not self.complete:
            raise AssertionError(f"No idle state after assistant output; last_event_id={self.last_id}")
        if not all(value in self.text for value in expected):
            raise AssertionError(f"Assistant output is missing expected values; last_event_id={self.last_id}")
        if require_tool and not self.tool_used:
            raise AssertionError(f"No actual tool execution; last_event_id={self.last_id}")


def wait_reply(events: Any, run: Run, session_id: str, after: str = "") -> TurnResult:
    result = TurnResult(last_id=after)
    while not result.complete:
        run.remaining()
        page = events.list(
            session_id,
            order="asc",
            limit=100,
            extra_query={"after_id": result.last_id or None, "include_tool_calls": True},
            timeout=min(run.remaining(), 30),
        )
        for index, event in enumerate(page):
            if index >= 2000:
                raise AssertionError("Event polling exceeded 2000 events")
            result.observe(event)
            if result.complete:
                break
        if not result.complete:
            run.pause()
    run.output("assistant", result.text)
    return result


def turn(
    events: Any,
    run: Run,
    session_id: str,
    prompt: str,
    expected: list[str],
    *,
    require_tool: bool = False,
) -> TurnResult:
    run.output("user", prompt)
    result = events.send(
        session_id,
        events=[{"type": "user.message", "content": [{"type": "text", "text": prompt}]}],
        extra_headers={"Idempotency-Key": name("event")},
    )
    if len(result.data) != 1 or not result.data[0].id:
        raise AssertionError("Send must return exactly one user event ID")
    reply = wait_reply(events, run, session_id, result.data[0].id)
    reply.verify(expected, require_tool)
    return reply
