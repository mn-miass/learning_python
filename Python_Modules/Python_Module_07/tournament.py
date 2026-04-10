from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, DefensiveStrategy, AggressiveStrategy
from typing import List, Tuple


def battle(tornament: List[Tuple]) -> None:
    try:
        print("*** Tournament ***")
        print(f"{len(tornament)} oponents involved\n")
        for i in range(len(tornament)):
            creature_f, strategy_f = tornament[i]
            creature_f = creature_f.create_base()
            for j in range(i+1, len(tornament)):
                creature_o, strategy_o = tornament[j]
                creature_o = creature_o.create_base()
                print("* Battle *")
                print(creature_f.describe())
                print("vs.")
                print(creature_o.describe())
                print("now fight!")
                try:
                    for action in strategy_f.act(creature_f):
                        print(action)
                    for action in strategy_o.act(creature_o):
                        print(action)
                except ValueError as e:
                    print(f"Battle error, aborting tournament: {e}")
                    return
                print()
    except BaseException:
        print("Error happend")


if __name__ == "__main__":
    tornament = 0

    flame = FlameFactory()
    aqua = AquaFactory()
    heal = HealingCreatureFactory()
    tranform = TransformCreatureFactory()

    normal = NormalStrategy()
    defense = DefensiveStrategy()
    aggressive = AggressiveStrategy()

    tornament_0 = [(flame, normal),
                   (heal, defense)]

    tornament_1 = [(flame, aggressive),
                   (heal, defense)]

    tornament_2 = [(aqua, normal),
                   (heal, defense),
                   (tranform, aggressive)]

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle(tornament_0)

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle(tornament_1)

    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle(tornament_2)
