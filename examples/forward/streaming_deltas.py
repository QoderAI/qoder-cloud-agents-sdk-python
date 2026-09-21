"""订阅 agent.message 文本增量，逐步更新消息预览，再用最终完整消息替换预览。

运行：python -m examples.forward.streaming_deltas
"""

from __future__ import annotations

from examples.common.live import Run, choose_model, marker, name, run_cli
from qca import Forward

from ._cleanup import finish_session


def _delta_text(event: object) -> str:
    """从一条文本增量事件中取出片段文本；不是文本增量时返回空串。"""
    delta = event.to_dict().get("delta") or {}
    if not isinstance(delta, dict) or delta.get("type") != "content_delta":
        return ""
    content = delta.get("content") or {}
    if not isinstance(content, dict) or content.get("type") != "text":
        return ""
    return content.get("text") or ""


def run(client: Forward, context: Run) -> None:
    environment = client.environments.create(name=name("env"), config={"type": "cloud"})
    environment_id = context.track("environment", environment.id, lambda: client.environments.archive(environment.id))

    identity = client.identities.create(external_id=name("identity"), name="SDK 示例用户")
    identity_id = context.track("identity", identity.id, lambda: client.identities.delete(identity.id))

    model = choose_model(client.models.list(), context.config.model)
    context.output("selected_model", model)
    template = client.templates.create(
        name=name("template"),
        environment_id=environment_id,
        model=model,
        system="你是一个 SDK 示例助手。必要时调用工具，只使用可实际读取的数据回答问题。",
        tools=[{"type": "agent_toolset_20260401"}],
    )
    template_id = context.track("template", template.id, lambda: client.templates.archive(template.id))

    session = client.sessions.create(identity_id=identity_id, template_id=template_id)
    session_id = context.track("session", session.id, lambda: finish_session(client, context, session.id))

    marker_value = marker()
    prompt = "请分三句话解释为什么多轮对话要复用 Session ID，最后原样附上：" + marker_value
    # 预览增量不写入历史：先订阅、开启 agent.message 增量，再发送消息。
    with client.sessions.events.stream(
        session_id,
        event_deltas=["agent.message"],
        timeout=context.remaining(),
    ) as stream:
        context.output("user", prompt)
        sent = client.sessions.events.send(
            session_id,
            events=[{"type": "user.message", "content": [{"type": "text", "text": prompt}]}],
            extra_headers={"Idempotency-Key": name("event")},
        )
        if not sent.data or not sent.data[0].id:
            raise RuntimeError("Send returned no user event")

        previews: dict[str, str] = {}
        deltas = 0
        for event in stream:
            context.remaining()
            if event.type == "event_delta":
                text = _delta_text(event)
                if text and event.event_id:
                    deltas += 1
                    # 同一条消息的多个片段按 event_id 累加，逐步刷新该消息的预览。
                    previews[event.event_id] = previews.get(event.event_id, "") + text
                    context.output("preview", f"{event.event_id}: {previews[event.event_id]}")
            elif event.type == "agent.message":
                context.output("assistant", event.to_json())
            elif event.type in ("session.error", "session.status_terminated"):
                raise RuntimeError(f"Session stopped: {event.type}")
            elif event.type == "session.status_idle":
                break
        context.output("deltas", deltas)


if __name__ == "__main__":
    run_cli("forward", Forward, {"streaming_deltas": run})
