import alchemy


if __name__ == "__main__":
    print("=== Sacred Scroll Mastery ===\n")

    print("Testing direct module access:")
    print("alchemy.elements.create_fire(): "
          f"{alchemy.elements.create_fire()}")
    print("alchemy.elements.create_water(): "
          f"{alchemy.elements.create_water()}")
    print("alchemy.elements.create_earth(): "
          f"{alchemy.elements.create_earth()}")
    print("alchemy.elements.create_air(): "
          f"{alchemy.elements.create_air()}")

    print("\nTesting package-level access (controlled by __init__.py):")
    print("alchemy.create_fire(): "
          f"{alchemy.create_fire()}")
    print("alchemy.create_water(): "
          f"{alchemy.create_water()}")

    print("alchemy.create_earth(): ", end="")
    try:
        print(f"{alchemy.create_earth()}")
    except AttributeError:
        print("AttributeError - not exposed")

    print("alchemy.create_air(): ", end="")
    try:
        print(f"{alchemy.create_air()}")
    except AttributeError:
        print("AttributeError - not exposed")

    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")
