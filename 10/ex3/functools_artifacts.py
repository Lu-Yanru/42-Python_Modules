from functools import reduce, partial, wraps
import operator
from typing import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    """
    Reduce/Fold spell powers using the specified operation.
    Support operations: add, multiply, max, min.
    """
    ops: dict[str, Callable] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    if operation not in ops.keys():
        raise ValueError(f"Unsupported operation: {operation}")
    return reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    """
    A partial application that takes a base_enchantment that takes
    power, element and target as arguments, and returns a dict with keys:
    fire_enchant, ice_encahnt and lightning_enchant.
    """
    return {
        "fire_enchant": partial(base_enchantment, power=50, element="fire"),
        "ice_enchant": partial(base_enchantment, power=50, element="ice"),
        "lightning_enchant": partial(base_enchantment, power=50,
                                     element="lightning"),
    }


# def memoized_fibonacci(n: int) -> int
# def spell_dispatcher() -> Callable


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{element} spell of {power} power hits {target}"


if __name__ == "__main__":
    print("Testing spell reduce...")
    spells = [50, 33, 17, 19, 18, 47]
    try:
        print(f"Sum: {spell_reducer(spells, "add")}")
        print(f"Product: {spell_reducer(spells, "multiply")}")
        print(f"Max: {spell_reducer(spells, "max")}")
        print(f"Min: {spell_reducer(spells, "min")}")
        print(f"Invalid: {spell_reducer(spells, "unknown")}")
    except ValueError as e:
        print(e)

    enchants = partial_enchanter(base_enchantment)
    print("\nTesting partial enchanter...")
    print(enchants["fire_enchant"](target="Dragon"))
    print(enchants["ice_enchant"](target="Goblin"))
    print(enchants["lightning_enchant"](target="Orc"))

    fibonacci_tests = [8, 19, 20]
