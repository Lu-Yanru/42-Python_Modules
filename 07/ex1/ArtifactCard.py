from ex0.Card import Card


class ArtifactCard(Card):
    """Specific type of Card of type artifact."""
    def __init__(self: "ArtifactCard", name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        if durability < 0:
            raise ValueError("ValueError: Durability cannot be negative.")
        self.durability = durability
        self.effect = effect

    def play(self: "ArtifactCard", game_state: dict) -> dict:
        """Specific way to play artifact card."""
        return {"card_played": self.name,
                "mana_used": self.cost,
                "effect": self.effect}

    def activate_ability(self: "ArtifactCard") -> dict:
        """Method to activate effect of artifact card."""
        return {"card_played": self.name,
                "mana_used": self.cost,
                "effect": self.effect}
