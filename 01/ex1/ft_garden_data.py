class Plant:
    """Define Plant class with name, height in cm, age in days."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Method to create an empty object."""
        self.name = name
        self.height = height
        self.age = age


def main() -> None:
    """Displays plants info."""
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    print(f"{plant1.name}: {plant1.height}cm, {plant1.age} days old")
    print(f"{plant2.name}: {plant2.height}cm, {plant2.age} days old")
    print(f"{plant3.name}: {plant3.height}cm, {plant3.age} days old")


if __name__ == "__main__":
    main()
