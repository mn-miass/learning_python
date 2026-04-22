from collections.abc import Callable


def spell(target: str, power: int) -> str:
    return f"{target} has power: {power}"


def heal(target: str, power: int) -> str:
    return f"Heal restores {power} for {target} HP"


def base_spell(target: str, power: int) -> str:
    return f"Original: {target}, Amplifier: {power}"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combine(target: str, power: int) -> str:
        spell_1 = spell1(target, power)
        spell_2 = spell2(target, power)
        return spell_1 + ", " + spell_2
    return combine


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifier(target: str, power: int) -> Callable:
        return base_spell(target, power*multiplier)
    return amplifier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(target: str, power: int) -> Callable | str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return caster


def conditions(target: str, power: int) -> bool:
    if isinstance(target, str) and isinstance(power, int):
        return True
    return False


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> Callable:
        spells_list = []
        for spell in spells:
            spells_list.append(spell(target, power))
        return spells_list
    return sequence


if __name__ == "__main__":
    test_values = [19, 20, 11, 12]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']
    spells = [spell, heal]

    print("Testing spell combiner...")
    combine = spell_combiner(spell, heal)
    for i in range(len(test_values)):
        output = combine(test_targets[i], test_values[i])
        print(output)

    amplify = power_amplifier(base_spell, 3)
    print("\nTesting amplifier...")
    for element in test_values:
        output = amplify(element, element)
        print(output)

    print("\nTesting conditional...")
    conditional = conditional_caster(conditions, spell)
    for i in range(len(test_values)):
        output = conditional(test_targets[i], test_values[i])
        print(output)

    print("\n\nTesting sequence...")
    sequence = spell_sequence(spells)
    for i in range(len(test_targets)):
        output = sequence(test_targets[i], test_values[i])
        for j in range(len(output)):
            print(output[j])
        print()
