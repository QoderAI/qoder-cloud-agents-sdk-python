"""Verify Forward delivery signatures before parsing the original request body."""

from __future__ import annotations

import base64
import binascii
import hashlib
import hmac
import time
from collections.abc import Mapping


class WebhookVerificationError(ValueError):
    """Missing, invalid, expired or mismatched delivery authentication."""


def verify_webhook_signature(payload: bytes, headers: Mapping[str, str], secret: str) -> None:
    """Accept any matching v1 signature within 300 seconds; raise on failure.

    Use original body bytes. After verification, deduplicate using Webhook-ID.
    """

    def invalid() -> WebhookVerificationError:
        return WebhookVerificationError("webhook signature verification failed")

    def header(name: str) -> str:
        values = [v for k, v in headers.items() if k.lower() == name]
        return values[0] if len(values) == 1 else ""

    if not isinstance(payload, bytes):
        raise invalid()
    event_id = header("webhook-id")
    timestamp = header("webhook-timestamp")
    if (
        not event_id
        or any(c in event_id for c in ".\r\n")
        or not timestamp
        or not timestamp.isascii()
        or not timestamp.isdecimal()
        or len(timestamp) > 19
        or not secret.startswith("whsec_")
    ):
        raise invalid()
    now = int(time.time())
    if not now - 300 <= int(timestamp) <= now + 300:
        raise invalid()
    try:
        key = base64.b64decode(secret[6:], validate=True)
    except (ValueError, binascii.Error):
        raise invalid() from None
    if not 24 <= len(key) <= 64 or base64.b64encode(key).decode("ascii") != secret[6:]:
        raise invalid()
    expected = hmac.new(key, (event_id + "." + timestamp + ".").encode("utf-8") + payload, hashlib.sha256).digest()
    for signature in header("webhook-signature").split():
        if not signature.startswith("v1,"):
            continue
        try:
            candidate = base64.b64decode(signature[3:], validate=True)
        except (ValueError, binascii.Error):
            continue
        if hmac.compare_digest(expected, candidate):
            return
    raise invalid()
