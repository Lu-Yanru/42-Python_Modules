from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    """Platform management system."""
    def __init__(self: "TournamentPlatform") -> None:
        self.cards = {}
        self.matches_played = 0

    def register_card(self: "TournamentPlatform", card: TournamentCard) -> str:
        count = 1
        for value in self.cards.values():
            if value.name == card.name:
                count += 1
        id = f"{card.name.lower().replace(" ", "_")}_{count:03d}"
        self.cards[id] = card
        return id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        try:
            card1 = self.cards[card1_id]
            card2 = self.cards[card2_id]
        except KeyError:
            raise KeyError("KeyError: Card id is not registered.")

        if card1.att > card2.att:
            winner, loser = card1, card2
            winner_id, loser_id = card1_id, card2_id
        elif card1.att < card2.att:
            winner, loser = card2, card1
            winner_id, loser_id = card2_id, card1_id
        winner.update_wins(1)
        loser.update_losses(1)
        self.matches_played += 1

        return {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_leaderboard(self: "TournamentPlatform") -> list:
        res = sorted(self.cards.values(),
                     key=lambda card: card.rating,
                     reverse=True)
        return res

    def generate_tournament_report(self: "TournamentPlatform") -> dict:
        count = len(self.cards)
        total_rating = 0
        for card in self.cards.values():
            total_rating += card.rating
        avg_rating = total_rating // count
        return {
            "total_cards": count,
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active"
        }
