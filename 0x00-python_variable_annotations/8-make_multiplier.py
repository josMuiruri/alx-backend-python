#!/usr/bin/env python3
from typing import Callable
def make_multiplier(multiplier: float) -> Callable[float]:
    return lambda x: multiplier*x
