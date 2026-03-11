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
             raise ValueError("ValueError: Attack, defend and health cannot be negative.")
        self.health = health
        self.att = attack
        self.defd = defend
        self.mana = mana

    def play(self, game_state: dict) -> dict
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

def cast_spell(self: "Magical", spell_name: str, targets: list) -> dict:
        """Abstract cast spell method."""
        pass

    @abstractmethod
    def channel_mana(self: "Magical", amount: int) -> dict:
        """Abstract channel mana method."""
        pass

    @abstractmethod
    def get_magic_stats(self: "Magical") -> dict:
        """Abstract get magic stats method."""
        pass
