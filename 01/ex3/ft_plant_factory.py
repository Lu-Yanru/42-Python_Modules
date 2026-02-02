class Plant:
    def __init__(self, name: str, height: int, age: int):
        """Method to create an empty object."""
        self.name = name
        self.height = height
        self.age = age

    def init_info(self):
        """Prints out info of newly created plant."""
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


def create_plant(name: str, height: int, age: int) -> Plant:
    plant = Plant(name, height, age)
    plant.init_info()
    return plant


def main() -> None:
    """Displays plant growth info."""
    print("=== Plant Factory Output ===")
    factory: list = [None] * 5
    factory[0] = create_plant("Rose", 25, 30)
    factory[1] = create_plant("Oak", 200, 365)
    factory[2] = create_plant("Cactus", 5, 90)
    factory[3] = create_plant("Sunflower", 80, 45)
    factory[4] = create_plant("Fern", 15, 120)
    print("")
    print(f"Total plants created: {len(factory)}")


if __name__ == "__main__":
    main()
