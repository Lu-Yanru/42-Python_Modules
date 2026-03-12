from abc import ABC, abstractmethod

from ex0.Card import Card


class CardFactory(ABC):
    """Abstract factory interface."""
    @abstractmethod
    def create_creature(self: "CardFactory",
                        name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_spell(self: "CardFactory",
                     name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_artifact(self: "CardFactory",
                        name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_themed_deck(self: "CardFactory",
                           size: int) -> dict:
        pass

    @abstractmethod
    def get_supported_types(self: "CardFactory") -> dict:
        pass
