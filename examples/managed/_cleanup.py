"""Managed 示例中重复使用的会话清理。"""

from examples.common.live import Run
from qca import Managed


def finish_session(client: Managed, context: Run, session_id: str) -> None:
    session = client.sessions.retrieve(session_id)
    if session.status not in ("idle", "terminated"):
        client.sessions.events.send(session_id, events=[{"type": "user.interrupt"}])
        while client.sessions.retrieve(session_id).status not in ("idle", "terminated"):
            context.pause()
    client.sessions.delete(session_id)
