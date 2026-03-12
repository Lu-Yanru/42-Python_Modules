from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """Enhanced card class with combat and rank."""
    def __init__(self: "TournamentCard", name: str, cost: int,
                 rarity: str, health: int, att: int, defd: int,
                 rating: int = 1200) -> None:
        super().__init__(name, cost, rarity)
        if att < 0 or defd < 0 or health < 0:
            raise ValueError("ValueError: Attack, defend and health "
                             "cannot be negative.")
        self.health = health
        self.att = att
        self.defd = defd
        self.wins = 0
        self.losses = 0
        self.rating = rating

    def play(self: "TournamentCard", game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Tournament started."
        }

    def attack(self: "TournamentCard", target: Card) -> dict:
        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self.att,
            "combate_type": "melee"
        }

    def defend(self: "TournamentCard", incoming_damage: int) -> dict:
        damage_taken = max(0, incoming_damage - self.defd)
        self.health -= damage_taken
        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": min(incoming_damage, self.defd),
            "still_alive": self.health > 0
        }

    def get_combat_stats(self: "TournamentCard") -> dict:
        return {
            "card_played": self.name,
            "attack": self.att,
            "defend": self.defd,
            "health": self.health
        }

    def calculate_rating(self: "TournamentCard") -> int:
        return self.rating

    def update_wins(self: "TournamentCard", wins: int) -> None:
        self.wins += wins
        self.rating += 16 * wins

    def update_losses(self: "TournamentCard", losses: int) -> None:
        self.losses += losses
        self.rating -= 16 * losses

    def get_rank_info(self: "TournamentCard") -> dict:
        return {
            "card": self.name,
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}"
        }

    def get_tournament_stats(self: "TournamentCard") -> dict:
        return {
            "card": self.name,
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }
