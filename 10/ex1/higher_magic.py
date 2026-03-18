#!/usr/bin/python3


from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """
    Combines 2 spells into one. Returns a function that calls both spells
    with the same arguments, and returns a tuple of their results.
    """
    print("Testing spell combiner...")

    def combined(*args, **kwargs) -> tuple:
        res1 = spell1(*args, **kwargs)
        res2 = spell2(*args, **kwargs)
        return (res1, res2)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """
    Amplify the result of a spell by a multiplier.
    Returns a function that calls the base_spell and multiplies its result
    with the multiplier.
    Assumes the base_spell returns a numeric value.
    """
    print("Testing power amplifier...")

    def amplified(*args, **kwargs) -> int:
        return base_spell(*args, **kwargs) * multiplier

    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """
    Cast spell conditionally.
    Only cast spell if condition is met.
    If condition fails, return "Spell fizzled".
    """
    print("Testing conditional caster...")

    def caster(*args, **kwargs) -> str:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        else:
            return "Spell fizzled"

    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    """
    Create spell sequence. Returns a function
    that casts all spells in a list in order
    and returns a list of all spell results.
    """
    print("Testing spell_sequence...")

    def sequence(*args, **kwargs) -> list:
        return [spell(*args, **kwargs) for spell in spells]

    return sequence


def fireball(target: str) -> str:
    return f"Fireball hits {target}"


def heal(target: str) -> str:
    return f"Heals {target}"


def lightning(target: str) -> str:
    return f"Lightning strikes {target}"


def base_spell(power: int) -> int:
    return power


def condition(target: str) -> bool:
    return target.lower() in ["dragon", "goblin", "orc"]


if __name__ == "__main__":
    combined = spell_combiner(fireball, heal)
    res_combined = combined("Dragon")
    print(f"Combined spell result: {", ".join(res_combined)}\n")

    power = 10
    amplified = power_amplifier(base_spell, 5)
    res_amplified = amplified(power)
    print(f"Original: {power}, Amplified: {res_amplified}\n")

    enemy = "Dragon"
    non_enemy = "Knight"
    caster = conditional_caster(condition, fireball)
    res_enemy = caster(enemy)
    res_non_enemy = caster(non_enemy)
    print(f"Casting spell on {enemy}: {res_enemy}\n"
          f"Casting spell on {non_enemy}: {res_non_enemy}\n")

    sequence = spell_sequence([fireball, heal, lightning])
    res_sequence = sequence("Dragon")
    print(f"Casting a sequence of spells: {res_sequence}")
