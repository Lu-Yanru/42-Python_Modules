class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        """Method to create an empty object."""
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Create flower object."""
        super().__init__(name, height, age)
        self.color = color
        print(f"{self.name} (Flower): "
              f"{self.height}cm, {self.age} days, {self.color} color")

    def bloom(self, status: bool) -> None:
        """Display if flower is blooming or not."""
        if status is True:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} is not blooming.")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """Create tree object."""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        print(f"{self.name} (Tree): "
              f"{self.height}cm, {self.age} days, "
              f"{self.trunk_diameter}cm diameter")

    def produce_shade(self, shade: int) -> None:
        """Display how much shade the tree produces."""
        self.shade = shade
        print(f"{self.name} provides {self.shade} sqaure meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, season: str) -> None:
        """Create vegetable object."""
        super().__init__(name, height, age)
        self.season = season
        print(f"{self.name} (Vegetable): "
              f"{self.height}cm, {self.age} days, {self.season} harvest")

    def nutritional_value(self, nutrition: str) -> None:
        """Display vegetable's nutritional value."""
        self.nutrition = nutrition
        print(f"{self.name} is rich in {self.nutrition}")


def main() -> None:
    """Displays garden plant types info."""
    print("=== Garden Plant Types ===\n")
    flower1 = Flower("Rose", 25, 30, "red")
    flower1.bloom(True)
    flower2 = Flower("Sunflower", 80, 45, "yellow")
    flower2.bloom(False)
    print("")
    tree1 = Tree("Oak", 500, 1825, 50)
    tree1.produce_shade(78)
    tree2 = Tree("Pine", 700, 1500, 40)
    tree2.produce_shade(75)
    print("")
    vegi1 = Vegetable("Tomato", 80, 90, "summer")
    vegi1.nutritional_value("vitamin C")
    vegi2 = Vegetable("Carrot", 50, 45, "autumn")
    vegi2.nutritional_value("vitamin A")


if __name__ == "__main__":
    main()
