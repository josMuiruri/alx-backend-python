#!/usr/bin/env python3
from collection.abc import Iterable
from typing import Tuple

def element_lenth(lst: int) -> Iterator:
    return [(i, len(i)) for i in lst]

