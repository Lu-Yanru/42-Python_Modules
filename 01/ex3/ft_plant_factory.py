class Plant:
    def __init__(self, name: str, height: int, age: int):
        """Method to create an empty object."""
        self.name = name
        self.height = height
        self.age = age

    def init_info(self):
        """Prints out info of newly created plant."""
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


def main() -> None:
    """Displays plant growth info."""
    plants = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    print("=== Plant Factory Output ===")
    count = 0
    factory: list = [Plant]
    for name, height, age in plants:
        plant = Plant(name, height, age)
        factory.append(plant)
        plant.init_info()
        count += 1

    print("")
    print(f"Total plants created: {count}")


if __name__ == "__main__":
    main()
