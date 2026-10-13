from __future__ import annotations

import base64
from typing import Any, Callable, Literal

from pydantic import PrivateAttr, SerializeAsAny
from typing_extensions import NotRequired, TypedDict

from qca.common._models import BaseModel


class RealtimeOutputAudioConfigParam(TypedDict):
    voice: NotRequired[Literal["longanqian", "longanlingxin", "longanlingxi", "longanxiaoxin", "longanlufeng"]]


class RealtimeAudioConfigParam(TypedDict):
    output: NotRequired[RealtimeOutputAudioConfigParam]


class RealtimeConfigParam(TypedDict):
    audio: NotRequired[RealtimeAudioConfigParam]


class RealtimeConversation(BaseModel):
    id: str
    type: Literal["voice.conversation"]
    status: str
    title: str | None
    metadata: dict[str, Any]
    config: dict[str, Any]
    created_at: str
    updated_at: str


class RealtimeConversationSummary(BaseModel):
    id: str
    title: str | None
    initialization_status: str
    metadata: dict[str, Any]
    created_at: str
    updated_at: str


class RealtimeHistoryEvent(BaseModel):
    id: str
    type: str
    status: str
    occurred_at: str
    role: str | None = None
    text: str | None = None
    work_id: str | None = None
    objective: str | None = None
    result: str | None = None
    error: dict[str, Any] | None = None
    turn_id: str | None = None
    user_message_event_id: str | None = None
    announcement_id: str | None = None
    milestone_type: str | None = None


class RealtimeHistoryPageInfo(BaseModel):
    next_before: str | None
    has_more: bool


class _RealtimeHistoryPage(BaseModel):
    conversation: RealtimeConversationSummary
    events: list[RealtimeHistoryEvent]
    page: RealtimeHistoryPageInfo
    _fetch_next: Callable[[str], Any] | None = PrivateAttr(default=None)
    _visited: frozenset[str] = PrivateAttr(default_factory=frozenset)

    def has_next_page(self) -> bool:
        return bool(self.page.has_more and self.page.next_before)

    def _next(self) -> Any:
        if not self.has_next_page():
            raise RuntimeError("No older history page; check has_next_page() first")
        if self.page.next_before in self._visited:
            raise RuntimeError("History returned a repeated pagination cursor")
        if self._fetch_next is None:
            raise RuntimeError("This history response is not bound to a client")
        return self._fetch_next(self.page.next_before or "")


class RealtimeHistoryPage(_RealtimeHistoryPage):
    def get_next_page(self) -> RealtimeHistoryPage:
        """Fetch the next page toward older history."""
        result = self._next()
        result._visited = self._visited | {self.page.next_before or ""}
        return result


class AsyncRealtimeHistoryPage(_RealtimeHistoryPage):
    async def get_next_page(self) -> AsyncRealtimeHistoryPage:
        """Fetch the next page toward older history."""
        result = await self._next()
        result._visited = self._visited | {self.page.next_before or ""}
        return result


class RealtimeAudioFormat(BaseModel):
    format: Literal["pcm16"]
    sample_rate: int
    channels: int


class RealtimeCapabilities(BaseModel):
    graceful_close: bool


class RealtimePayload(BaseModel):
    """Payload for unknown event types; extension fields remain accessible."""


class RealtimeReadyPayload(RealtimePayload):
    config: dict[str, Any]
    provider: str
    input_audio: RealtimeAudioFormat
    output_audio: RealtimeAudioFormat
    capabilities: RealtimeCapabilities


class RealtimeStatePayload(RealtimePayload):
    state: str


class RealtimeReasonPayload(RealtimePayload):
    reason: str


class RealtimeTranscriptPayload(RealtimePayload):
    role: str
    text: str
    item_id: str | None = None
    response_id: str | None = None


class RealtimeAudioPayload(RealtimePayload):
    audio: str


class RealtimeWorkAcceptedPayload(RealtimePayload):
    status: Literal["accepted"]
    objective: str


class RealtimeWorkRunningPayload(RealtimePayload):
    status: Literal["running"]


class RealtimeWorkProgressPayload(RealtimePayload):
    kind: str
    detail: str
    title: str | None = None
    is_error: bool | None = None
    event_id: str | None = None


class RealtimeWorkMilestonePayload(RealtimePayload):
    announcement_id: str
    milestone_type: str
    summary: str


class RealtimeWorkCompletedPayload(RealtimePayload):
    status: Literal["completed"]
    result: str
    event_id: str | None = None


class RealtimeWorkError(BaseModel):
    code: str


class RealtimeWorkFailedPayload(RealtimePayload):
    status: Literal["failed"]
    error: RealtimeWorkError
    event_id: str | None = None


class RealtimeClosedPayload(RealtimePayload):
    request_id: str
    outcome: str


class RealtimeErrorPayload(RealtimePayload):
    code: str
    message: str
    retryable: bool | None = None
    retry_after_ms: int | None = None


class RealtimeEvent(BaseModel):
    version: Literal["voice.realtime.v1"]
    type: str
    event_id: str
    sequence: int
    conversation_id: str
    timestamp: str
    payload: SerializeAsAny[RealtimePayload]
    work_id: str | None = None
    announcement_id: str | None = None

    def audio_bytes(self) -> bytes:
        """Decode an audio.delta event's raw PCM16 bytes (no WAV header)."""
        if self.type != "audio.delta" or not isinstance(self.payload, RealtimeAudioPayload):
            raise ValueError("audio_bytes() requires an audio.delta event")
        pcm = base64.b64decode(self.payload.audio, validate=True)
        if not pcm or len(pcm) % 2:
            raise ValueError("audio.delta must contain complete, non-empty PCM16 samples")
        return pcm
