"""Continue an existing session with native async I/O and an SSE stream.

QODER_SESSION_ID=sess_... python -m examples.managed.async_session
"""

import asyncio
import os
from uuid import uuid4

from qca import AsyncManaged


async def main() -> None:
    session_id = os.environ["QODER_SESSION_ID"]
    async with AsyncManaged() as client:
        sent = await client.sessions.events.send(
            session_id,
            events=[{"type": "user.message", "content": [{"type": "text", "text": "Hello!"}]}],
            extra_headers={"Idempotency-Key": uuid4().hex},
        )
        if len(sent.data) != 1 or not sent.data[0].id:
            raise RuntimeError("Expected one accepted user event")
        async with await client.sessions.events.stream(
            session_id, extra_headers={"Last-Event-ID": sent.data[0].id}
        ) as stream:
            async for event in stream:
                if event.type == "agent.message":
                    print(event.to_json())
                elif event.type == "session.status_idle":
                    return
                elif event.type in ("session.error", "session.status_terminated"):
                    raise RuntimeError(f"Session stopped: {event.type}")
        raise RuntimeError(f"Stream ended before idle; last_event_id={stream.last_event_id}")


if __name__ == "__main__":
    asyncio.run(main())
