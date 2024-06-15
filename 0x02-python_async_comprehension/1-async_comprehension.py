#!/usr/bin/env python3

"""
asynchronous comprehension coroutine that collects random numbers form an async_generator

"""


import asyncio
from typing import List
from 0_async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    coroutine that collects 10 random numbers using an async comprehension over
    async_genetator, then returns the 10 random numbers

    Returns:
        List[float]: list of 10 random floats nums collected from async_generator.
    """
    return [number async for number in async_generator()]
