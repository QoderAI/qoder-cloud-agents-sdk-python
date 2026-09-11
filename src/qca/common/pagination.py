from __future__ import annotations

from collections.abc import AsyncIterator, Awaitable, Callable, Iterator
from typing import Any, Generic, TypeVar

from pydantic import Field, PrivateAttr

from ._models import BaseModel

T = TypeVar("T")


class BasePage(BaseModel, Generic[T]):
    data: list[T] = Field(default_factory=list)
    has_more: bool | None = None
    first_id: str | None = None
    last_id: str | None = None
    next_page: str | None = None
    _query: dict[str, Any] = PrivateAttr(default_factory=dict)
    _style: str = PrivateAttr(default="Page")
    _fetch: Any = PrivateAttr(default=None)

    def _next_query(self) -> dict[str, Any] | None:
        if self.has_more is False:
            return None
        query = dict(self._query)
        if self._style in ("PageCursor", "BidirectionalPageCursor", "TokenPage"):
            key = "page_token" if self._style == "TokenPage" else "page"
            cursor = self.next_page
        else:
            if not self.data:
                return None
            key = "before_id" if query.get("before_id") else "after_id"
            cursor = self.first_id if key == "before_id" else self.last_id
        if not cursor:
            return None
        if query.get(key) == cursor:
            raise RuntimeError("Pagination cursor did not advance")
        for other in ("after_id", "before_id", "page", "page_token"):
            if other != key:
                query[other] = None
        query[key] = cursor
        return query

    def has_next_page(self) -> bool:
        return self._next_query() is not None


class SyncPage(BasePage[T]):
    def get_next_page(self) -> SyncPage[T]:
        query = self._next_query()
        if query is None:
            raise RuntimeError("No more pages")
        if self._fetch is None:
            raise RuntimeError("Page is not attached to a client request")
        return self._fetch(query)

    def iter_pages(self) -> Iterator[SyncPage[T]]:
        page = self
        seen: set[str] = set()
        while True:
            yield page
            query = page._next_query()
            if query is None:
                break
            fingerprint = repr(query)
            if fingerprint in seen:
                raise RuntimeError("Pagination cursor cycle detected")
            seen.add(fingerprint)
            page = page.get_next_page()

    def __iter__(self) -> Iterator[T]:  # type: ignore[override]
        for page in self.iter_pages():
            yield from page.data


class AsyncPage(BasePage[T]):
    async def get_next_page(self) -> AsyncPage[T]:
        query = self._next_query()
        if query is None:
            raise RuntimeError("No more pages")
        if self._fetch is None:
            raise RuntimeError("Page is not attached to a client request")
        return await self._fetch(query)

    async def iter_pages(self) -> AsyncIterator[AsyncPage[T]]:
        page = self
        seen: set[str] = set()
        while True:
            yield page
            query = page._next_query()
            if query is None:
                break
            fingerprint = repr(query)
            if fingerprint in seen:
                raise RuntimeError("Pagination cursor cycle detected")
            seen.add(fingerprint)
            page = await page.get_next_page()

    async def __aiter__(self) -> AsyncIterator[T]:
        async for page in self.iter_pages():
            for item in page.data:
                yield item


class AsyncPaginator(Generic[T]):
    """Await the first page, or iterate items directly with async for."""

    def __init__(self, fetch: Callable[[], Awaitable[AsyncPage[T]]]) -> None:
        self._fetch = fetch

    def __await__(self) -> Any:
        return self._fetch().__await__()

    async def __aiter__(self) -> AsyncIterator[T]:
        page = await self._fetch()
        async for item in page:
            yield item
