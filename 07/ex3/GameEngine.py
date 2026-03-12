from ex0.Card import Card
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    """Game orchestrator"""
    def configure_engine(self: "GameEngine", factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy
        self.cards_created = 0
        self.hand: list[Card] = []
        self.battlefield: list[Card] = []
        self.turns_simulated = 0
        self.log: list[dict] = []

    def simulate_turn(self: "GameEngine") -> dict:
        self.turns_simulated += 1
        actions = self.strategy.execute_turn(self.hand, self.battlefield)
        self.log.append(actions)
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": actions.get("damage_dealt", 0),
            "cards_created": self.cards_created
        }

    def get_engine_status(self: "GameEngine") -> dict:
        return {
            "Factory": self.factory.__class__.__name__,
            "Strategy": self.strategy.get_strategy_name()
        }
