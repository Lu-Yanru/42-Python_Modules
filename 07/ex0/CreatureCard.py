from ex0.Card import Card


class CreatureCard(Card):
    """Concrete implementation of Card, Creature type."""
    def __init__(self: "CreatureCard",  name: str, cost: int,
                 rarity: str, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        if attack < 0:
            raise ValueError("ValueError: Attack cannot be negative.")
        else:
            self.attack = attack
        if health < 0:
            raise ValueError("ValueError: Health cannot be negative.")
        else:
            self.health = health

    def play(self: "CreatureCard", game_state: dict) -> dict:
        """Concrete way to play creature card."""
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }

    def attack_target(self: "CreatureCard", target: Card) -> dict:
        """Special method for attacking."""
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }
