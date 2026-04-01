import alchemy.elements
from alchemy.elements import create_fire
from alchemy.potions import healing_potion as heal
from alchemy.elements import create_fire, create_water
from alchemy.potions import strength_potion

if __name__ == "__main__":
    print("\n=== Import Transmutation Mastery ===\n")
    print("Method 1 - Full module import:")
    try:
        print("alchemy.elements.create_fire(): ", end="")
        print(create_fire())
    except AttributeError:
        print("AttributeError - not exposed")

    print("\nMethod 2 - Specific function import:")
    try:
        print("create_water(): ", end="")
        print(create_water())
    except AttributeError:
        print("AttributeError - not exposed")

    print("\nMethod 3 - Aliased import:")
    try:
        print("heal(): ", end="")
        print(heal())
    except AttributeError:
        print("AttributeError - not exposed")

    print("\nMethod 4 - Multiple imports:")
    try:
        print("create_earth(): ", end="")
        print(alchemy.elements.create_earth())
    except AttributeError:
        print("AttributeError - not exposed")

    try:
        print("create_fire(): ", end="")
        print(create_fire())
    except AttributeError:
        print("AttributeError - not exposed")

    try:
        print("Strength_potion(): ", end="")
        print(strength_potion())
    except AttributeError:
        print("AttributeError - not exposed")

    print("\nAll import transmutation methods mastered!")

