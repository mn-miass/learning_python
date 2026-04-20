from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    power = initial_power

    def acumulation(added_power):
        nonlocal power
        power += added_power
        return power
    return acumulation


def enchantment_factory(enchantment_type: str) -> Callable:
    def enhantement(name):
        return enchantment_type + " " + name
    return enhantement


def memory_vault() -> dict[str, Callable]:
    vault = {}

    def store(key, value):
        vault[key] = value

    def recall(key):
        try:
            return vault[key]
        except KeyError:
            return "Memory not found"
    return {'store': store, 'recall': recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_a call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    accumulator = spell_accumulator(100)
    print(f"Base 100, add 20: {accumulator(20)}")
    print(f"Base 100, add 30: {accumulator(30)}")

    print("\nTesting enchantment factory...")
    flame = enchantment_factory("Flaming")
    froze = enchantment_factory("Frozen")
    print(f"{flame("Sword")}")
    print(f"{froze("Shield")}")

    print("\nTesting memory vault...")
    memory = memory_vault()
    print("Store 'secret' = 42")
    memory['store']("secret", 42)
    print(f"Recall 'secret': {memory['recall']('secret')}")
    print(f"Recall 'unknown': {memory['recall']('unknown')}")
