#!/usr/bin/env python3
from typing import Iterator, Tuple

def element_lenth(lst: int) -> Iterator:
    return Tuple[(i, len(i)) for i in lst]

