from typing import Any, Callable


def mage_counter() -> Callable:
    """
    Return a function that counts how many times it's been called.
    Each call returns the current count.
    """
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    """
    Return a function that accumulates power over time.
    Each call add the given amount to the total power,
    and returns the new total power.
    """
    total_power = initial_power

    def accumulator(amount: int) -> int:
        nonlocal total_power
        total_power += amount
        return total_power

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    """
    Return a function that applies the specified enchantment
    (takes an item name and returns enchanted description).
    """
    def enchanter(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchanter


def memory_vault() -> dict[str, Callable]:
    """
    Create a memory management system.
    Return a dict with store and recall functions.
    store funtion takes (key, value) and stores the memory.
    recall function takes (key) and returns stored value
    or 'Memory not found'.
    """
    vault: dict = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        return vault.get(key, "Memory not found")

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter = mage_counter()
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")

    print("\nTesting power accumulator...")
    accumulator = spell_accumulator(10)
    print(f"Accumulation 1: {accumulator(5)}")
    print(f"Accumulation 2: {accumulator(10)}")
    print(f"Accumulation 3: {accumulator(20)}")

    print("\nTesting enchantment factory...")
    fire = enchantment_factory("Flaming")
    ice = enchantment_factory("Frozen")
    print(fire("Sword"))
    print(ice("Sword"))
    print(fire("Shield"))
    print(ice("Shield"))

    print("\nTesting memory vault...")
    funcs = memory_vault()
    funcs["store"]("spell", "fireball")
    funcs["store"]("artifact", "magical orb")
    print(funcs["recall"]("spell"))
    print(funcs["recall"]("artifact"))
    print(funcs["recall"]("unknown"))
