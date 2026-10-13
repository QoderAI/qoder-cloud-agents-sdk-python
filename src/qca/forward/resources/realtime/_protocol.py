from __future__ import annotations

import base64
import json
import re
from datetime import datetime
from typing import Any
from urllib.parse import urlencode

import httpx
from pydantic import ValidationError

from qca.common._exceptions import APIConnectionError
from qca.forward.types.realtime import (
    RealtimeAudioPayload,
    RealtimeClosedPayload,
    RealtimeErrorPayload,
    RealtimeEvent,
    RealtimePayload,
    RealtimeReadyPayload,
    RealtimeReasonPayload,
    RealtimeStatePayload,
    RealtimeTranscriptPayload,
    RealtimeWorkAcceptedPayload,
    RealtimeWorkCompletedPayload,
    RealtimeWorkFailedPayload,
    RealtimeWorkMilestonePayload,
    RealtimeWorkProgressPayload,
    RealtimeWorkRunningPayload,
)

PROTOCOL = "voice.realtime.v1"
MAX_CLIENT_MESSAGE_BYTES = 256 * 1024
TERMINAL_ERRORS = {
    "provider_initialization_failed",
    "context_restore_failed",
    "provider_unavailable",
    "service_restarting",
    "event_persistence_failed",
}
CLOSE_OUTCOMES = {"no_active_response", "no_content", "saved", "saved_interrupted"}
PAYLOADS: dict[str, type[RealtimePayload]] = {
    "voice.state": RealtimeStatePayload,
    "voice.ready": RealtimeReadyPayload,
    "voice.replaced": RealtimeReasonPayload,
    "transcript.delta": RealtimeTranscriptPayload,
    "transcript.final": RealtimeTranscriptPayload,
    "audio.delta": RealtimeAudioPayload,
    "playback.interrupt": RealtimeReasonPayload,
    "work.accepted": RealtimeWorkAcceptedPayload,
    "work.running": RealtimeWorkRunningPayload,
    "work.progress": RealtimeWorkProgressPayload,
    "work.milestone": RealtimeWorkMilestonePayload,
    "work.completed": RealtimeWorkCompletedPayload,
    "work.failed": RealtimeWorkFailedPayload,
    "connection.closed": RealtimeClosedPayload,
    "error": RealtimeErrorPayload,
}


class RealtimeError(APIConnectionError):
    """Realtime transport/protocol failure, without credentials or raw event text."""

    def __init__(
        self, message: str, *, conversation_id: str, close_code: int | None = None, close_reason: str | None = None
    ) -> None:
        super().__init__(request=httpx.Request("GET", "https://realtime.invalid/"), message=message)
        self.conversation_id = conversation_id
        self.close_code = close_code
        self.close_reason = close_reason


class RealtimeProtocolError(RealtimeError):
    pass


class RealtimeTimeoutError(RealtimeError):
    def __init__(self, stage: str, *, conversation_id: str) -> None:
        super().__init__(f"Realtime {stage} timed out", conversation_id=conversation_id)
        self.stage = stage


class RealtimeQueueOverflowError(RealtimeError):
    pass


class RealtimeServerError(RealtimeError):
    def __init__(self, event: RealtimeEvent) -> None:
        payload = event.payload
        assert isinstance(payload, RealtimeErrorPayload)
        super().__init__("Realtime server reported a terminal error", conversation_id=event.conversation_id)
        self.code = payload.code
        self.retryable = payload.retryable
        self.retry_after_ms = payload.retry_after_ms
        self.event = event


def websocket_url(base_url: httpx.URL, conversation_id: str) -> str:
    if (
        not isinstance(conversation_id, str)
        or not conversation_id
        or any(ord(c) < 32 or ord(c) == 127 for c in conversation_id)
    ):
        raise ValueError("conversation_id must be a non-empty string without control characters")
    return str(
        base_url.join("realtime").copy_with(
            scheme="wss" if base_url.scheme == "https" else "ws",
            query=urlencode({"conversation_id": conversation_id}).encode(),
        )
    )


def parse_event(message: str | bytes, conversation_id: str) -> RealtimeEvent:
    try:
        if not isinstance(message, str):
            raise ValueError("binary frames are not part of voice.realtime.v1")

        def invalid_constant(value: str) -> Any:
            raise ValueError("Non-JSON numeric constant")

        data = json.loads(message, parse_constant=invalid_constant)
        if not isinstance(data, dict) or not isinstance(data.get("payload"), dict):
            raise ValueError("invalid event envelope")
        for field in ("type", "event_id", "conversation_id", "timestamp"):
            if not isinstance(data.get(field), str) or not data[field]:
                raise ValueError("missing event field")
        if data["conversation_id"] != conversation_id or type(data.get("sequence")) is not int or data["sequence"] < 0:
            raise ValueError("invalid event identity or sequence")
        if not re.fullmatch(
            r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(?:\.[0-9]{1,9})?(?:Z|[+-][0-9]{2}:[0-9]{2})",
            data["timestamp"],
        ):
            raise ValueError("timestamp must be RFC3339 with a time zone")
        # Python 3.10 accepts only 3/6 fractional digits; validate a normalized copy.
        timestamp = re.sub(r"\.([0-9]{1,9})", lambda match: "." + match.group(1)[:6].ljust(6, "0"), data["timestamp"])
        datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
        payload = PAYLOADS.get(data["type"], RealtimePayload).model_validate(data["payload"], strict=True)
        event = RealtimeEvent.model_validate({**data, "payload": payload}, strict=True)
        if isinstance(payload, RealtimeReadyPayload):
            if not payload.provider:
                raise ValueError("ready provider must be non-empty")
            if (
                payload.input_audio.sample_rate,
                payload.output_audio.sample_rate,
                payload.input_audio.channels,
                payload.output_audio.channels,
            ) != (16000, 24000, 1, 1):
                raise ValueError("unsupported PCM audio format")
        if isinstance(payload, RealtimeAudioPayload):
            pcm = base64.b64decode(payload.audio, validate=True)
            if not pcm or len(pcm) % 2:
                raise ValueError("audio event must contain complete PCM16 samples")
        return event
    except (ValueError, TypeError, ValidationError) as exc:
        raise RealtimeProtocolError("Invalid voice.realtime.v1 server event", conversation_id=conversation_id) from exc


def encode_event(event_type: str, payload: dict[str, Any]) -> str:
    if not isinstance(event_type, str) or not event_type or not isinstance(payload, dict):
        raise ValueError("event type must be non-empty and payload must be an object")
    if event_type == "text.message":
        text = payload.get("text")
        text = text.strip() if isinstance(text, str) else text
        if not isinstance(text, str) or not text or len(text.encode("utf-8")) > 16 * 1024:
            raise ValueError("text must be non-empty and at most 16 KiB in UTF-8")
        payload = {**payload, "text": text}
    if event_type == "audio.append":
        audio = payload.get("audio")
        if not isinstance(audio, str) or not audio:
            raise ValueError("audio must contain non-empty Base64 PCM16")
        pcm = base64.b64decode(audio, validate=True)
        if not pcm or len(pcm) % 2:
            raise ValueError("audio must contain complete PCM16 samples")
    if event_type == "connection.close":
        request_id = payload.get("request_id")
        if (
            not isinstance(request_id, str)
            or not request_id
            or len(request_id.encode("utf-8")) > 128
            or request_id != request_id.strip()
            or any(ord(c) < 32 or ord(c) == 127 for c in request_id)
        ):
            raise ValueError("close request_id must be 1–128 UTF-8 bytes without surrounding whitespace or controls")
    if event_type.startswith("playback."):
        for name in ("work_id", "announcement_id"):
            if name in payload and (not isinstance(payload[name], str) or not payload[name]):
                raise ValueError(f"{name} must be a non-empty string when provided")
    encoded = json.dumps(
        {"version": PROTOCOL, "type": event_type, "payload": payload},
        ensure_ascii=False,
        separators=(",", ":"),
        allow_nan=False,
    )
    if len(encoded.encode("utf-8")) > MAX_CLIENT_MESSAGE_BYTES:
        raise ValueError("encoded client event exceeds the 256 KiB limit")
    return encoded


def pcm_payload(pcm_bytes: bytes) -> dict[str, Any]:
    if not isinstance(pcm_bytes, bytes) or not pcm_bytes or len(pcm_bytes) % 2:
        raise ValueError("audio must be non-empty, complete PCM16 bytes (no WAV header)")
    if len(pcm_bytes) >= 12 and pcm_bytes[:4] == b"RIFF" and pcm_bytes[8:12] == b"WAVE":
        raise ValueError("pass raw PCM16 samples without a WAV header")
    return {"audio": base64.b64encode(pcm_bytes).decode("ascii")}


def receipt_payload(work_id: str | None, announcement_id: str | None) -> dict[str, Any]:
    return {
        key: value for key, value in (("work_id", work_id), ("announcement_id", announcement_id)) if value is not None
    }
