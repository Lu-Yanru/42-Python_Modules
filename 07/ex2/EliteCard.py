from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """Implements multiple inheritance."""
    def __init__(self: "EliteCard", name: str,
                 cost: int, rarity: str,
                 health: int, attack: int,
                 defend: int, mana: int) -> None:
        super().__init__(name, cost, rarity)
        if attack < 0 or defend < 0 or health < 0:
            raise ValueError("ValueError: Attack, defend and health "
                             "cannot be negative.")
        self.health = health
        self.att = attack
        self.defd = defend
        self.mana = mana

    def play(self: "EliteCard", game_state: dict) -> dict:
        """Specific way to play elite card."""
        return {"card_played": self.name,
                "mana_used": self.cost,
                "effect": "Elite summoned with combat and magic abilities."}

    def attack(self: "EliteCard", target: Card) -> dict:
        """Elite attack method"""
        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self.att,
            "combate_type": "melee"
        }

    def defend(self: "EliteCard", incoming_damage: int) -> dict:
        """Elite defend method."""
        damage_taken = max(0, incoming_damage - self.defd)
        self.health -= damage_taken
        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": min(incoming_damage, self.defd),
            "still_alive": self.health > 0
        }

    def get_combat_stats(self: "EliteCard") -> dict:
        """Elite get combat stats method."""
        return {
            "card_played": self.name,
            "attack": self.att,
            "defend": self.defd,
            "health": self.health
        }

    def cast_spell(self: "EliteCard", spell_name: str,
                   targets: list[Card]) -> dict:
        """Elite cast spell method."""
        self.mana -= self.cost
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": [t.name for t in targets],
            "mana_used": self.cost
        }

    def channel_mana(self: "EliteCard", amount: int) -> dict:
        """Elite channel mana method."""
        if amount < 0:
            raise ValueError("ValueError: "
                             "Cannot channel negative amount of mana.")
        self.mana += amount
        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_magic_stats(self: "EliteCard") -> dict:
        """Elite get magic stats method."""
        return {
            "card_played": self.name,
            "cost": self.cost,
            "mana": self.mana
        }
