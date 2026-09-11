"""Forward 示例中重复使用的会话清理。"""

from examples.common.live import Run
from qca import Forward


def finish_session(client: Forward, context: Run, session_id: str) -> None:
    session = client.sessions.retrieve(session_id)
    if session.status not in ("idle", "terminated"):
        client.sessions.cancel(session_id)
        while client.sessions.retrieve(session_id).status not in ("idle", "terminated"):
            context.pause()
    client.sessions.archive(session_id)
