from functools import wraps
from timeit import default_timer as timer
from typing import Callable


def spell_timer(func: Callable) -> Callable:
    """
    A decorator that measures function execution time.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = timer()
        res = func(*args, **kwargs)
        end = timer()
        print(f"Spell completed in {end - start:.3f} seconds")
        return res

    return wrapper


def power_validator(min_power: int) -> Callable:
    """
    A decorator factory that validates power levels.
    Check if the first argument is >= min_power.
    If valid, execute the function.
    If invalid, return error message.
    """
    def validator(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args, **kwargs):
            if args[0] >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"

        return wrapper
    return validator


def retry_spell(max_attempts: int) -> Callable:
    """
    A decorator that retries functions when they raise an exception,
    up to max_attempt times.
    If attempt fails, prints out error message.
    If successful, return the result normally.
    """
    def retry(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args, **kwargs):
            i = 0
            while i < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print("Spell failed, retrying... "
                          f"(attempt {i}/{max_attempts})")
                    i += 1
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper
    return retry


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        for letter in name:
            if not letter.isalpha() and letter != " ":
                return False
        return True

    def cast_spell(self, spell_name: str, power: int) -> str:

        @power_validator(10)
        def validate_power(power: int) -> str:
            return f"Successfull cast {spell_name} with power {power}"

        return validate_power(power)


@spell_timer
def fireball() -> str:
    return "Fireball cast!"


@retry_spell(3)
def unstable_spell(power: int) -> str:
    if power <= 0:
        raise ValueError("Spell failed!")
    return "Spell succeeded!"


if __name__ == "__main__":
    print("Testing spell timer...")
    print(f"Result: {fireball()}")

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("42"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Fireball", 5))

    print("\nTesting retry spell...")
    print(unstable_spell(5))
    print(unstable_spell(-1))
