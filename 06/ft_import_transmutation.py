def full_module() -> None:
    import alchemy.elements

    print("Method 1 - Full module import:")
    print("alchemy.elements.create_fire(): "
          f"{alchemy.elements.create_fire()}")


def spec_function() -> None:
    from alchemy.elements import create_water

    print("Method 2 - Specific function import:")
    print("create_water(): "
          f"{create_water()}")


def aliased_import() -> None:
    from alchemy.potions import healing_potion as heal

    print("Method 3 - Aliased import:")
    print("heal(): "
          f"{heal()}")


def multiple_imports() -> None:
    from alchemy.elements import create_fire, create_earth
    from alchemy.potions import strength_potion

    print("Method 4 - Multiple imports:")
    print(f"create_earth(): {create_earth()}")
    print(f"create_fire(): {create_fire()}")
    print(f"strength_potion(): {strength_potion()}")


if __name__ == "__main__":
    print("=== Import Transmutation Mastery ===\n")
    full_module()
    print("")
    spec_function()
    print("")
    aliased_import()
    print("")
    multiple_imports()

    print("\nAll import transmutation methods mastered!")
