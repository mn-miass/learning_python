import alchemy.grimoire

if __name__ == "__main__":
    print("\n=== Circular Curse Breaking ===\n")

    print("Testing ingredient validation:")
    try:
        print("validate_ingredients(\"fire air\"): ", end="")
        print(alchemy.grimoire.validate_ingredients("fire air"))
    except AttributeError:
        print("AttributeError - not exposed")

    try:
        print("validate_ingredients(\"fire air\"): ", end="")
        print(alchemy.grimoire.validate_ingredients("shadow"))
    except AttributeError:
        print("AttributeError - not exposed")

    print("\nTesting spell recording with validation:")
    try:
        print("record_spell(\"Lightning\", \"air\"): ", end="")
        print(alchemy.grimoire.record_spell("Lightning", "air"))
    except AttributeError:
        print("AttributeError - not exposed")

    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")