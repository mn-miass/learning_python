from functools import wraps
from collections.abc import Callable
from time import time
from typing import Any


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time()
        print(f"Casting function {func.__name__}")
        f = func(*args, **kwargs)
        start = time() - start
        print(f"Spell completed {start * 1000:0.3f}ms")
        return f
    return wrapper


def power_validator(min_power: int) -> Callable:
    def validator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str | Any:
            if args[1] >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return validator


def retry_spell(max_attempts: int) -> Callable:
    def validator(func: Callable) -> Callable:
        counter = 0

        @wraps(func)
        def wrapper(*argv: Any, **kwargs: Any) -> Callable:
            try:
                result = func(*argv, **kwargs)
                return result
            except Exception:
                nonlocal counter
                if counter < max_attempts:
                    counter += 1
                    print("Spell failed, retrying... "
                          f"({counter}/{max_attempts})")
                    return wrapper(*argv, **kwargs)
                else:
                    print("Spell casting failed after max_attempts attempts")
        return wrapper
    return validator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        for char in name:
            if not char.isalpha() and not char.isspace():
                return False
        return True

    @power_validator(10)
    def cast_spell(self, power: int, spell_name: str) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    return "Fireball cast!"


@retry_spell(3)
def retry() -> None:
    raise ValueError


if __name__ == "__main__":
    test_powers = [5, 24, 27, 29]
    spell_names = ['blizzard', 'heal', 'shield', 'darkness']
    mage_names = ['Ember', 'Ash', 'Zara', 'Kai', 'Riley', 'Casey']
    invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name']

    print("Testing spell timer...")
    print(f"Result: {fireball()}")
    print()

    print("Testing retrying spell...")
    retry()
    print()

    print("Testing MageGuild...")
    mage = MageGuild()
    for i in range(len(spell_names)):
        print(mage.cast_spell(test_powers[i], spell_names[i]))
