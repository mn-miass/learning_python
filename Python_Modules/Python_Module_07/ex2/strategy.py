from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capability import TransformCapability, HealCapability
from typing import List


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> List[str]:
        pass

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, Creature):
            return True
        return False


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> List[str]:
        if self.is_valid(creature):
            return [creature.attack()]
        raise ValueError(f"Invalid Creature {creature.name}"
                         " for this normal strategy")

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, Creature):
            return True
        return False


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: TransformCapability) -> List[str]:
        if self.is_valid(creature):
            return [creature.transform(), creature.attack(), creature.revert()]
        raise ValueError(f"Invalid Creature {creature.name}"
                         "for this aggressive strategy")

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        return False


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> List[str]:
        if self.is_valid(creature):
            return [creature.attack(), creature.heal()]
        raise ValueError(f"Invalid Creature {creature.name}"
                         "for this aggressive strategy")

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, HealCapability):
            return True
        return False
