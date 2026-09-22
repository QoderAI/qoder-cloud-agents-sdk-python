"""让 Agent 调用自定义工具，在本地 Python 函数中执行，再把结果回传给 Agent 得到最终回答。

运行：python -m examples.managed.custom_tools
"""

from __future__ import annotations

import json

from examples.common.live import Run, choose_model, marker, name, run_cli
from qca import Managed

from ._cleanup import finish_session


def _lookup_order(call: object, data: dict[str, str]) -> tuple[str, bool]:
    """业务代码边界：只有显式注册的工具会执行。返回 (回传内容, is_error)。"""
    if getattr(call, "name", None) != "lookup_order":
        return "unknown tool; use lookup_order", True
    order_id = (getattr(call, "input", None) or {}).get("order_id")
    if not isinstance(order_id, str) or not order_id:
        return "order_id must be a non-empty string", True
    if order_id != data["order_id"]:
        return "order not found", True
    return json.dumps(data, ensure_ascii=False), False


def _read_tool_turn(client: Managed, context: Run, session_id: str, after: str):
    """读取一段执行流：返回 (待执行的工具调用列表或 None, 断点游标)。

    收到 requires_action 表示 Agent 暂停等待工具结果；否则本轮已给出最终回答。
    """
    calls: dict = {}
    cursor = after
    with client.sessions.events.stream(
        session_id,
        extra_headers={"Last-Event-ID": after},
        timeout=context.remaining(),
    ) as stream:
        for event in stream:
            context.remaining()
            if event.id:
                cursor = event.id
            if event.type == "agent.custom_tool_use":
                calls[event.id] = event
                context.output("tool_call", event.name)
            elif event.type == "agent.message":
                context.output("assistant", event.to_json())
            elif event.type in ("session.error", "session.status_terminated"):
                raise RuntimeError(f"Session stopped: {event.type}")
            elif event.type == "session.status_idle":
                reason = event.stop_reason.type if event.stop_reason else None
                if reason == "requires_action":
                    ids = event.stop_reason.event_ids or []
                    return [calls[i] for i in ids if i in calls], cursor
                return None, cursor
    raise RuntimeError("Stream ended before a final answer or tool-result request")


def run(client: Managed, context: Run) -> None:
    environment = client.environments.create(name=name("env"), config={"type": "cloud"})
    environment_id = context.track("environment", environment.id, lambda: client.environments.archive(environment.id))

    model = choose_model(client.models.list(), context.config.model)
    context.output("selected_model", model)
    agent = client.agents.create(
        name=name("agent"),
        model={"id": model},
        system="查询订单时必须调用 lookup_order。拿到工具返回后，用中文回答订单状态和完整运单号，不得编造。",
        tools=[
            {
                "type": "custom",
                "name": "lookup_order",
                "description": "根据订单 ID 查询订单状态和运单号。",
                "input_schema": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string", "description": "待查询的订单 ID"}},
                    "required": ["order_id"],
                },
            }
        ],
    )
    agent_id = context.track("agent", agent.id, lambda: client.agents.archive(agent.id))

    session = client.sessions.create(environment_id=environment_id, agent=agent_id)
    session_id = context.track("session", session.id, lambda: finish_session(client, context, session.id))

    # 运单号只存在于本进程，不在模型提示词里；Agent 必须调用本地工具才能拿到。
    data = {"order_id": "order-" + marker(), "status": "已发货", "tracking_number": "track-" + marker()}
    prompt = f"请查询订单 {data['order_id']}，告诉我订单状态和完整运单号。"
    context.output("user", prompt)
    sent = client.sessions.events.send(
        session_id,
        events=[{"type": "user.message", "content": [{"type": "text", "text": prompt}]}],
        extra_headers={"Idempotency-Key": name("event")},
    )
    if not sent.data or not sent.data[0].id:
        raise RuntimeError("Send returned no user event")

    after = sent.data[0].id
    for _ in range(8):
        pending, after = _read_tool_turn(client, context, session_id, after)
        if pending is None:
            return
        results = []
        for call in pending:
            text, is_error = _lookup_order(call, data)
            context.output("tool_result", f"{call.name} is_error={is_error}")
            results.append(
                {
                    "type": "user.custom_tool_result",
                    "custom_tool_use_id": call.id,
                    "is_error": is_error,
                    "content": [{"type": "text", "text": text}],
                }
            )
        # 在 idle 事件之后续订，快速到来的最终回复不会被跳过。
        response = client.sessions.events.send(
            session_id,
            events=results,
            extra_headers={"Idempotency-Key": name("tool-results")},
        )
        if not response.data:
            raise RuntimeError("Server did not acknowledge tool results")
    raise RuntimeError("Custom tool loop exceeded eight rounds")


if __name__ == "__main__":
    run_cli("managed", Managed, {"custom_tools": run})
