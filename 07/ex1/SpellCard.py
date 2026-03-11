from ex0.Card import Card
from ex0.CreatureCard import CreatureCard


class SpellCard(Card):
    """Concrete implementation of Card of type spell."""
    def __init__(self: "SpellCard", name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        if effect_type not in ["damage", "heal", "buff", "debuf"]:
            raise ValueError("ValueError: Invalid spell effect type.")
        self.effect_type = effect_type

    def play(self: "SpellCard", game_state: dict) -> dict:
        """Specific way to play spell card."""
        return {"card_played": self.name,
                "mana_used": self.cost,
                "effect": f"Deal {self.cost} {self.effect_type} to target"}

    def resolve_effect(self: "SpellCard", targets: list[CreatureCard]) -> dict:
        """Method to resolve spell effect."""
        for target in targets:
            if self.effect_type == "damage":
                target.health -= self.cost
            elif self.effect_type == "heal":
                target.health += self.cost
            elif self.effect_type == "buff":
                target.attack += self.cost
            elif self.effect_type == "debuff":
                target.attack -= self.cost
        return {"card_name": self.name,
                "effect_type": self.effect_type,
                "targets": [t.name for t in targets]}
