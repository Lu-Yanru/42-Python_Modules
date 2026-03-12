from abc import ABC, abstractmethod


class Card(ABC):
    """The abstract foundation class."""
    def __init__(self: "Card", name: str,
                 cost: int, rarity: str) -> None:
        """Constructor."""
        self.name = name
        if cost < 0:
            raise ValueError("ValueError: Cost cannot be negative.")
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self: "Card", game_state: dict) -> dict:
        """How to play the card."""
        pass

    def get_card_info(self: "Card") -> dict:
        """Get card info as a dict."""
        return {"name": self.name,
                "cost": self.cost,
                "rarity": self.rarity}

    def is_playable(self: "Card", available_mana: int) -> bool:
        """
        Check if a card is playable.

        Returns
            True if playable.
            False if not playable.
        """
        if available_mana >= self.cost:
            return True
        return False
