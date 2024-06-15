#!/usr/bin/env python3
"""asynchronous generator that yields random numbers"""


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    coroutine yield random number btn 0 & 10, ten times,each time waiting 1 second asynchronously.
    
    Returns:
        AsyncGenerator[float, None]: An asynchronous generator yielding float values.

    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

