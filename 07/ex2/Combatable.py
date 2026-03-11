from abc import ABC, abstractmethod

from ex0.Card import Card


class Combatable(ABC):
    """Abstract combat interface."""

    @abstractmethod
    def attack(self: "Combatable", target: Card) -> dict:
        """Abstract attack method"""
        pass

    @abstractmethod
    def defend(self: "Combatable", incoming_damage: int) -> dict:
        """Abstract defend method."""
        pass

    @abstractmethod
    def get_combat_stats(self: "Combatable") -> dict:
        """Abstract get combat stats method."""
        pass
