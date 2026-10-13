"""Forward Realtime text or raw PCM16. Uses the existing PAT/SA example configuration.

python -m examples.forward.realtime --identity-id ID --template-id ID --text 'Hello'
python -m examples.forward.realtime --conversation-id ID --history-only
python -m examples.forward.realtime --identity-id ID --template-id ID --pcm input.pcm

Realtime must already be enabled on the Template. Conversations persist after close.
This example doesn't play output audio or resample/decode WAV files.
SA mode requires a Forward-issued, bound SAT in QODER_ACCESS_TOKEN, with
QODER_AUTH_MODE=sa and QODER_SA_KEY unset. Platform SATs lack that binding.
"""

from __future__ import annotations

import argparse
import asyncio
import time
from pathlib import Path
from uuid import uuid4

from examples.common.live import Config, safe_error
from qca import AsyncForward, Forward


def parser():
    value = argparse.ArgumentParser(description=__doc__)
    value.add_argument("--identity-id")
    value.add_argument("--template-id")
    value.add_argument("--conversation-id")
    value.add_argument("--history-only", action="store_true")
    group = value.add_mutually_exclusive_group()
    group.add_argument("--text", default="Please say hello briefly.")
    group.add_argument("--pcm", type=Path, help="16 kHz mono little-endian signed PCM16, without WAV header")
    value.add_argument("--async", dest="use_async", action="store_true")
    value.add_argument("--env-file", default=".env.live")
    value.add_argument("--region", choices=("cn", "global"))
    value.add_argument("--timeout", type=float, default=120)
    return value


def validate(args):
    if args.history_only and not args.conversation_id:
        raise ValueError("--history-only requires --conversation-id")
    if not args.conversation_id and not (args.identity_id and args.template_id):
        raise ValueError("Provide --conversation-id or both --identity-id and --template-id")
    if args.pcm:
        if not args.pcm.is_file() or args.pcm.stat().st_size == 0 or args.pcm.stat().st_size % 2:
            raise ValueError("PCM input must be a non-empty file of complete PCM16 samples")
        with args.pcm.open("rb") as stream:
            head = stream.read(12)
            if head[:4] == b"RIFF" and head[8:12] == b"WAVE":
                raise ValueError("Decode WAV to raw PCM16 before running this example")


def sync_main(args, config):
    with config.open_client(Forward) as client:
        conversation_id = (
            args.conversation_id
            or client.realtime.conversations.create(
                identity_id=args.identity_id,
                template_id=args.template_id,
                idempotency_key=uuid4().hex,
                title="SDK Realtime example",
            ).id
        )
        print("conversation_id:", conversation_id)
        if not args.history_only:
            with client.realtime.connect(conversation_id=conversation_id) as connection:
                deadline = time.monotonic() + args.timeout
                if args.pcm:
                    with args.pcm.open("rb") as stream:
                        while chunk := stream.read(640):
                            if time.monotonic() >= deadline:
                                raise TimeoutError("PCM transmission exceeded the example deadline")
                            connection.append_audio(chunk)
                            time.sleep(0.02)
                else:
                    connection.send_text(args.text)
                while time.monotonic() < deadline:
                    event = connection.recv(timeout=max(0.001, deadline - time.monotonic()))
                    print("event:", event.type)
                    if event.type == "audio.delta":
                        event.audio_bytes()
                    if event.type == "audio.done":
                        # No audio device is playing this response; report actual cancellation.
                        connection.playback_cancelled(work_id=event.work_id, announcement_id=event.announcement_id)
                        break
                else:
                    raise TimeoutError("No complete audio response before the deadline")
                print("close outcome:", connection.close_gracefully())
        page = client.realtime.conversations.history(conversation_id, limit=10)
        for _ in range(5):
            print("history:", [(event.id, event.type) for event in page.events])
            if not page.has_next_page():
                break
            page = page.get_next_page()


async def async_main(args, config):
    async with config.open_async_client(AsyncForward) as client:
        conversation_id = (
            args.conversation_id
            or (
                await client.realtime.conversations.create(
                    identity_id=args.identity_id,
                    template_id=args.template_id,
                    idempotency_key=uuid4().hex,
                    title="SDK Realtime example",
                )
            ).id
        )
        print("conversation_id:", conversation_id)
        if not args.history_only:
            async with await client.realtime.connect(conversation_id=conversation_id) as connection:
                deadline = time.monotonic() + args.timeout
                if args.pcm:
                    with args.pcm.open("rb") as stream:
                        while chunk := stream.read(640):
                            if time.monotonic() >= deadline:
                                raise TimeoutError("PCM transmission exceeded the example deadline")
                            await connection.append_audio(chunk)
                            await asyncio.sleep(0.02)
                else:
                    await connection.send_text(args.text)
                while time.monotonic() < deadline:
                    event = await connection.recv(timeout=max(0.001, deadline - time.monotonic()))
                    print("event:", event.type)
                    if event.type == "audio.delta":
                        event.audio_bytes()
                    if event.type == "audio.done":
                        await connection.playback_cancelled(
                            work_id=event.work_id, announcement_id=event.announcement_id
                        )
                        break
                else:
                    raise TimeoutError("No complete audio response before the deadline")
                print("close outcome:", await connection.close_gracefully())
        page = await client.realtime.conversations.history(conversation_id, limit=10)
        for _ in range(5):
            print("history:", [(event.id, event.type) for event in page.events])
            if not page.has_next_page():
                break
            page = await page.get_next_page()


def main():
    args = parser().parse_args()
    try:
        validate(args)
        config = Config.load("forward", env_file=args.env_file, region=args.region, timeout=args.timeout)
        if args.use_async:
            asyncio.run(async_main(args, config))
        else:
            sync_main(args, config)
    except Exception as error:
        print(safe_error(error))
        raise SystemExit(1) from None


if __name__ == "__main__":
    main()
