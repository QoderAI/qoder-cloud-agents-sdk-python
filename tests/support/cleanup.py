"""场景复用的会话与 dream 清理。

forward 与 managed 的 finish_session 是两份不同实现（forward: cancel+archive；
managed: user.interrupt+delete），随各自 SCENARIOS 分别迁自 examples/{forward,managed}/_cleanup.py；
finish_dream 迁自 examples/managed/dream.py。场景侧以 `as finish_session` 别名保持调用点逐字不变。
"""

from __future__ import annotations

from qca import Forward, Managed
from tests.support.harness import Run


def finish_session_forward(client: Forward, context: Run, session_id: str) -> None:
    session = client.sessions.retrieve(session_id)
    if session.status not in ("idle", "terminated"):
        client.sessions.cancel(session_id)
        while client.sessions.retrieve(session_id).status not in ("idle", "terminated"):
            context.pause()
    client.sessions.archive(session_id)


def finish_session_managed(client: Managed, context: Run, session_id: str) -> None:
    session = client.sessions.retrieve(session_id)
    if session.status not in ("idle", "terminated"):
        client.sessions.events.send(session_id, events=[{"type": "user.interrupt"}])
        while client.sessions.retrieve(session_id).status not in ("idle", "terminated"):
            context.pause()
    client.sessions.delete(session_id)


def finish_dream(client: Managed, context: Run, dream_id: str, input_store_id: str) -> None:
    dream = client.dreams.retrieve(dream_id)
    if dream.status in ("pending", "running"):
        client.dreams.cancel(dream_id)
        while dream.status in ("pending", "running"):
            context.pause()
            dream = client.dreams.retrieve(dream_id)
    errors = []
    actions = []
    if dream.session_id:
        actions.append(lambda: finish_session_managed(client, context, dream.session_id))
    seen = {input_store_id}
    for output in dream.outputs or []:
        if output.memory_store_id and output.memory_store_id not in seen:
            seen.add(output.memory_store_id)
            actions.append(lambda store_id=output.memory_store_id: client.memory_stores.delete(store_id))
    actions.append(lambda: client.dreams.archive(dream_id))
    for action in actions:
        try:
            action()
        except Exception as error:
            errors.append(error)
    if errors:
        raise RuntimeError(f"Dream cleanup had {len(errors)} failures") from errors[0]
