#!/usr/bin/env python3
"""asynchronous generator that yields random numbers"""

import asyncio
import random

async def async_generator():
    """ coroutine yield random number btn 0 & 10, ten times,each time waiting 1 second asynchronously """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

