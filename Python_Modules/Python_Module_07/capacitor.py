from ex1 import HealingCreatureFactory, TransformCreatureFactory
from typing import List


def testing(Factories: List[HealingCreatureFactory |
                            TransformCreatureFactory]) -> None:
    for factory in Factories:
        if isinstance(factory, HealingCreatureFactory):
            print("Testing Creature with healing capability")
            print("base")
            base = factory.create_base()
            print(base.describe())
            print(base.attack())
            print(base.heal())
            print("evolved:")
            evolve = factory.create_evolved()
            print(evolve.describe())
            print(evolve.attack())
            print(evolve.heal())
            print()

        elif isinstance(factory, TransformCreatureFactory):
            print("Testing Creature with Transfom capability")
            print("base")
            base = factory.create_base()
            print(base.describe())
            print(base.attack())
            print(base.transform())
            print(base.attack())
            print(base.revert())
            print("evolved:")
            evolve = factory.create_evolved()
            print(evolve.describe())
            print(evolve.attack())
            print(evolve.transform())
            print(evolve.attack())
            print(evolve.revert())


if __name__ == "__main__":
    heal = HealingCreatureFactory()
    transform = TransformCreatureFactory()

    factory = [heal, transform]
    testing(factory)
