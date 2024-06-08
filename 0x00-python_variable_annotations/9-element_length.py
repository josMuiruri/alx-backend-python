#!/usr/bin/env python3
from typing import Iterator
def element_lenth(lst: int) -> Iterator:
    return [(i, len(i)) for i in lst]

