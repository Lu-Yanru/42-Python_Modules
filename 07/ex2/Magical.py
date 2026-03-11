from abc import ABC, abstractmethod


class Magical(ABC):
    """Abstract magic interface."""

    @abstractmethod
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
