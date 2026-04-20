from collections.abc import Callable
from functools import reduce, partial
import operator
from typing import Any

def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    if operation == "add":
        return reduce(operator.add, spells)
    elif operation == "multiply":
        return reduce(operator.mul, spells)
    elif operation == "max":
        return reduce(lambda max, x: max if max > x else x, spells)
    elif operation == "min":
        return reduce(lambda min, x: min if min < x else x, spells)
    else:
        return "Error"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    pass


def memoized_fibonacci(n: int) -> int:
    pass


def spell_dispatcher() -> Callable[[Any], str]:
    pass

