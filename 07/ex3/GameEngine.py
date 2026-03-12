from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    """Game orchestrator"""
    def configure_engine(self: "GameEngine", factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy
        self.hand = []
        self.battelfield = []
        self.turns_simulated = 0
        self.log = []

    def simulate_turn(self: "GameEngine") -> dict:
        self.turns_simulated += 1
        actions = self.strategy.execute_turn(self.hand, self.battelfield)
        self.log.append(actions)
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": actions.get("damage_dealt", 0),
            "cards_created": len(self.hand)
        }

    def get_engine_status(self: "GameEngine") -> dict:
        return {
            "Factory": self.factory.__class__.__name__,
            "Strategy": self.strategy.get_strategy_name()
        }
