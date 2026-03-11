from random import shuffle

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard


class Deck:
    """Deck management class."""
    def __init__(self: "Deck") -> None:
        self.deck: list[Card] = []

    def add_card(self: "Deck", card: Card) -> None:
        """Add a card to the deck."""
        if not isinstance(card, Card):
            raise TypeError(f"TypeError: {card} is not a card.")
        self.deck.append(card)

    def remove_card(self: "Deck", card_name: str) -> bool:
        """
        Remove a card from the deck.

        Returns
            True if successfully removes.
            False if not.
        """
        for card in self.deck:
            if card.name == card_name:
                self.deck.remove(card)
                return True
        return False

    def shuffle(self: "Deck") -> None:
        """Shuffle the deck."""
        shuffle(self.deck)

    def draw_card(self: "Deck") -> Card:
        """Draw a card from the top of the deck."""
        if not len(self.deck) == 0:
            return self.deck.pop(0)
        else:
            return None  # type: ignore

    def get_deck_stats(self: "Deck") -> dict:
        """Get stats about the deck."""
        total = len(self.deck)
        total_cost = 0
        creatures = 0
        spells = 0
        artifacts = 0
        for card in self.deck:
            if isinstance(card, CreatureCard):
                creatures += 1
            elif isinstance(card, SpellCard):
                spells += 1
            elif isinstance(card, ArtifactCard):
                artifacts += 1
            total_cost += card.cost
        avg_cost = total_cost / total
        return {"total_cards": total,
                "creatures": creatures,
                "spells": spells,
                "artifacts": artifacts,
                "avg_cost": round(avg_cost, 1)}
