from functools import wraps
from timeit import default_timer as timer
from typing import Callable


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = timer()
        res = func(*args, **kwargs)
        end = timer()
        print(f"Spell completed in {end - start:.3f} seconds")
        return res

    return wrapper


# def power_validator(min_power: int) -> callable
# def retry_spell(max_attempts: int) -> callable
# class MageGuild:
#     @staticmethod
#     def validate_mage_name(name: str) -> bool
#     def cast_spell(self, spell_name: str, power: int) -> str


@spell_timer
def fireball() -> str:
    return "Fireball cast!"


if __name__ == "__main__":
    print("Testing spell timer...")
    print(f"Result: {fireball()}")
