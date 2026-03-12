import random


from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    """Concrete factory."""
    def __init__(self: "FantasyCardFactory") -> None:
        self.cards = []
        self.creatures = ["dragon", "goblin"]
        self.spells = ["fireball"]
        self.artifacts = ["mana_ring"]

    def create_creature(self: "FantasyCardFactory",
                        name_or_power: str | int | None = None) -> Card:
        return CreatureCard(name_or_power, 3, "Common", 3, 5)  # type: ignore

    def create_spell(self: "FantasyCardFactory",
                     name_or_power: str | int | None = None) -> Card:
        return SpellCard(name_or_power, 2, "Common", "damage")  # type: ignore

    def create_artifact(self: "FantasyCardFactory",
                        name_or_power: str | int | None = None) -> Card:
        return ArtifactCard(name_or_power, 2,  # type: ignore
                            "Common", 3, "+1 mana per turn")

    def create_themed_deck(self: "FantasyCardFactory",
                           size: int) -> dict:
        for i in range(size):
            self.cards.append(self.create_creature(
                random.choice(self.creatures)
            ))
            self.cards.append(self.create_spell(
                random.choice(self.spells)
            ))
            self.cards.append(self.create_artifact(
                random.choice(self.artifacts)
            ))
        return {"deck": self.cards}

    def get_supported_types(self: "FantasyCardFactory") -> dict:
        return {
            "creatures": self.creatures,
            "spells": self.spells,
            "artifacts": self.artifacts
        }
