from __future__ import annotations

from typing import Protocol


class Credential(Protocol):
    def get_token(self) -> str:
        """Return the current access token. Called for each HTTP attempt."""
        ...


class AsyncCredential(Protocol):
    async def get_token(self) -> str: ...
