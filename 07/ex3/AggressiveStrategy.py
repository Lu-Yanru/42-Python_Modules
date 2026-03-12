from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """Concrete strategy."""
    def execute_turn(self: "AggressiveStrategy",
                     hand: list, battlefield: list) -> dict:
        """
        Play low-cost creatures first.
        Prioritize attacking and dealing damage.
        """
        if len(hand) <= 0:
            raise ValueError("ValueError: The hand is empty.")
        cards_played = []
        # Sort hand by the creature with the lowest cost
        sorted_creatures = sorted(hand,
                                  key=lambda card:
                                  (
                                   0 if isinstance(card, CreatureCard) else 1,
                                   card.cost
                                  ))
        card1 = sorted_creatures[0]
        cards_played.append(card1)
        hand.remove(card1)

        # Play max 2 cards per turn, 1st creature, 2nd spell
        if len(hand) > 1:
            sorted_spells = sorted(hand,
                                   key=lambda card:
                                   (
                                    0 if isinstance(card, SpellCard) else 1,
                                    card.cost
                                   ))
            cards_played.append(sorted_spells[0])
            hand.remove(sorted_spells[0])

        # attack targets
        if len(battlefield) > 0:
            targets = self.prioritize_targets(battlefield)
            if hasattr(card1, "attack"):
                card1.attack_target(targets[0])

        return {
            "cards_played": [card.name for card in cards_played],
            "mana_used": sum([card.cost for card in cards_played]),
            "targets_attacked": [targets[0].name] if len(targets) > 0 else [],
            "damage_dealt": (card1.attack
                             if isinstance(card1, CreatureCard)
                             else 0)
        }

    def get_strategy_name(self: "AggressiveStrategy") -> str:
        return self.__class__.__name__

    def prioritize_targets(self: "AggressiveStrategy",
                           available_targets: list) -> list:
        """Prioritze enemy creatures and player directly."""
        res = sorted(available_targets,
                     key=lambda card: 0
                     if isinstance(card, CreatureCard) else 1)
        return res
