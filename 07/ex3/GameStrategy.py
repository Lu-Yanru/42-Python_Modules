from abc import ABC, abstractmethod


class GameStrategy(ABC):
    """Abstract strategy interface."""
    @abstractmethod
    def execute_turn(self: "GameStrategy", hand: list,
                     battlefield: list) -> dict:
        pass

    @abstractmethod
    def get_strategy_name(self: "GameStrategy") -> str:
        pass

    @abstractmethod
    def prioritize_targets(self: "GameStrategy",
                           available_targets: list) -> list:
        pass
