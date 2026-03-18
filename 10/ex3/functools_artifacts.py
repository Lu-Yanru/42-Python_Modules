from functools import reduce, partial, lru_cache, singledispatch
import operator
# from timeit import default_timer as timer
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


@lru_cache
def memoized_fibonacci(n: int) -> int:
    """
    Calculate fibonacci sequence while caching the result using the
    Least Recently Used (LRU) strategy
    to improve performance for repeated calls.
    Return the nth fibonacci number.
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    """
    Create a spell single dispatch system.
    Handle different types: int (damage spell),
    str (enchantment), list (multi-cast).
    Return the dispatcher function.
    """
    @singledispatch
    def spell(arg) -> str:
        return f"Unknown spell type: {type(arg).__name__}"

    @spell.register(int)
    def _1(arg: int) -> str:
        return f"Damage spell deals {arg} damage"

    @spell.register(str)
    def _2(arg: str) -> str:
        return f"Enchantment {arg} applied"

    @spell.register(list)
    def _3(arg: list) -> str:
        return f"Casting multiple spells: {arg}"

    return spell


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

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    # start = timer()
    print(f"Fib(15): {memoized_fibonacci(15)}")
    # end = timer()
    # print(end - start)

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("flaming"))
    print(dispatcher(["fireball", "lightning", "heal"]))
    print(dispatcher({"key": "value"}))
