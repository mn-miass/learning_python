from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capability import TransformCapability, HealCapability
from ex1.factory import CreatureFactory
from typing import List, cast


def testing(Factories: List[CreatureFactory]) -> None:
    try:
        for factory in Factories:
            if isinstance(factory, HealingCreatureFactory):
                print("Testing Creature with healing capability")
                print("base")
                base = factory.create_base()
                hb = cast(HealCapability, base)
                print(base.describe())
                print(base.attack())
                print(hb.heal())
                print("evolved:")
                evolve = factory.create_evolved()
                print(evolve.describe())
                print(evolve.attack())
                print(hb.heal())
                print()

            elif isinstance(factory, TransformCreatureFactory):
                print("Testing Creature with Transfom capability")
                print("base")
                t_base = factory.create_base()
                tb = cast(TransformCapability, base)
                print(t_base.describe())
                print(t_base.attack())
                print(tb.transform())
                print(t_base.attack())
                print(tb.revert())
                print("evolved:")
                t_evolve = factory.create_evolved()
                print(t_evolve.describe())
                print(t_evolve.attack())
                print(tb.transform())
                print(t_evolve.attack())
                print(tb.revert())
    except BaseException:
        print("Error happend")


if __name__ == "__main__":
    heal = HealingCreatureFactory()
    transform = TransformCreatureFactory()

    factory = [heal, transform]
    testing(factory)
