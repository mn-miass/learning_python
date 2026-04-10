from ex0 import FlameFactory, AquaFactory
from typing import List


def create(Factories: List[FlameFactory | AquaFactory]) -> None:
    try:
        for factory in Factories:
            print("Testing factory")
            base = factory.create_base()
            print(f"{base.describe()}")
            print(f"{base.attack()}")
            evolve = factory.create_evolved()
            print(f"{evolve.describe()}")
            print(f"{evolve.attack()}")
            print()

        print("Testing battle")
        for i in range(len(Factories)):
            base = Factories[i].create_base()
            print(f"{base.describe()}")
            if i != len(Factories) - 1:
                print("vs.")

        print("fight!")
        for factory in Factories:
            base = factory.create_base()
            print(base.attack())
    except BaseException:
        print("")


if __name__ == "__main__":
    flame = FlameFactory()
    aqua = AquaFactory()

    factory = [flame, aqua]
    create(factory)
