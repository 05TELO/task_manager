from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

import httpx

from bot.config import API_BASE_URL


@asynccontextmanager
async def get_httpx_client(
    client_timeout: float = 30.0, max_connections: int = 10
) -> AsyncIterator[httpx.AsyncClient]:
    async with httpx.AsyncClient(
        base_url=API_BASE_URL,
        timeout=httpx.Timeout(client_timeout),
        limits=httpx.Limits(max_connections=max_connections),
    ) as client:
        yield client
