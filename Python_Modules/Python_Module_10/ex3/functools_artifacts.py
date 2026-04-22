from collections.abc import Callable
from functools import reduce, partial, lru_cache, singledispatch
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


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"Enchenting {target} with element {element} (power) {power}"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire = partial(base_enchantment, 50, "fire")
    ice = partial(base_enchantment, 50, "ice")
    water = partial(base_enchantment, 50, "water")
    return {"fire": fire, "ice": ice, "water": water}


@lru_cache(maxsize=128)
def memoized_fibonacci(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def cast_spell(spell) -> str:
        return "Unknown spell type"

    @cast_spell.register(int)
    def _int(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @cast_spell.register(str)
    def _str(spell: str) -> str:
        return f"Enchantment: {spell}"

    @cast_spell.register(list)
    def _list(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return cast_spell


if __name__ == "__main__":
    spell_powers = [15, 35, 45, 50, 26, 19]
    operations = ['add', 'multiply', 'max', 'min']
    fibonacci_tests = [12, 17, 18]

    print("Testing spell reducer")
    for element in operations:
        print(f"{element}: {spell_reducer(spell_powers, element)}")

    print("\nTesting memoized fibonacci...")
    for element in fibonacci_tests:
        print(f"Fib({element}): {memoized_fibonacci(element)}")

    print("\nTesting spell dispatcher...")
    spell = spell_dispatcher()
    print(spell(42))
    print(spell("Fireball"))
    print(spell(fibonacci_tests))
    print(spell({}))
