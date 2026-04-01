from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
from alchemy.transmutation.advanced import philosophers_stone, elixir_of_life
import alchemy

if __name__ == "__main__":
    print("\n=== Pathway Debate Mastery ===\n")

    print("Testing Absolute Imports (from basic.py):")
    try:
        print("lead_to_gold(): ", end="")
        print(lead_to_gold())
    except AttributeError:
        print("AttributeError - not exposed")

    try:
        print("stone_to_gem(): ", end="")
        print(stone_to_gem())
    except AttributeError:
        print("AttributeError - not exposed")

    print("\nTesting Relative Imports (from advanced.py):")
    try:
        print("philosophers_stone(): ", end="")
        print(philosophers_stone())
    except AttributeError:
        print("AttributeError - not exposed")

    try:
        print("elixir_of_life(): ", end="")
        print(elixir_of_life())
    except AttributeError:
        print("AttributeError - not exposed")

    print("\nTesting Package Access:")
    try:
        print("alchemy.transmutation.lead_to_gold(): ", end="")
        print(alchemy.transmutation.lead_to_gold())
    except AttributeError:
        print("AttributeError - not exposed")
    try:
        print("alchemy.transmutation.philosophers_stone(): ", end="")
        print(alchemy.transmutation.philosophers_stone())
    except AttributeError:
        print("AttributeError - not exposed")

    print("\nBoth pathways work! Absolute: clear, Relative: concise")