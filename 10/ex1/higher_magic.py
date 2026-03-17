#!/usr/bin/python3


from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    print("Testing spell combiner...")

    def combined(*args, **kwargs):
        res1 = spell1(*args, **kwargs)
        res2 = spell2(*args, **kwargs)
        return (res1, res2)
    return combined


#def power_amplifier(base_spell: callable, multiplier: int) -> callable
#def conditional_caster(condition: callable, spell: callable) -> callable
#def spell_sequence(spells: list[callable]) -> callable


def fireball(target: str) -> str:
    return f"Fireball hits {target}"


def heal(target: str) -> str:
    return f"Heals {target}"


if __name__ == "__main__":
    test_values = [7, 11, 12]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    combined = spell_combiner(fireball, heal)
    res = combined("Dragon")
    print(f"Combined spell result: {", ".join(res)}\n")
