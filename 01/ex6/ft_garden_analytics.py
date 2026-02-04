class Plant:
    """Define Plant class with name, height in cm, age in days."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Method to create an empty object."""
        self.name = name
        self.height = height
        self.age = age

    def grow(self, growth: int = 1) -> int:
        """Displays plant growth in height."""
        self.height += growth
        print(f"{self.name} grew {growth}cm")
        return growth

    def display_info(self) -> None:
        """Displays plant info."""
        print(f"- {self.name}: {self.height}cm")

    @classmethod
    def get_class_name(cls) -> str:
        """Get the name of the class."""
        return cls.__name__


class FloweringPlant(Plant):
    """
    Subclass of the plant class.
    Represents a flowering plant with color and can bloom.
    """
    def __init__(self, name: str, height: int, age: int, color: str,
                 blooming: bool) -> None:
        """Create flower object."""
        super().__init__(name, height, age)
        self.color = color
        self.blooming = blooming

    def display_info(self) -> None:
        """Displays info about plant."""
        if self.blooming is True:
            print(f"- {self.name}: "
                  f"{self.height}cm, {self.color} flowers (blooming)")
        else:
            print(f"- {self.name}: "
                  f"{self.height}cm, {self.color} flowers (not blooming)")


class PrizeFlower(FloweringPlant):
    """
    Subclass of flowering plant.
    Represnts a prized flowering plant with a prize value.
    """
    def __init__(self, name: str, height: int, age: int, color: str,
                 blooming: bool, prize: int) -> None:
        """Create prize flower object."""
        super().__init__(name, height, age, color, blooming)
        self.prize = prize

    def display_info(self) -> None:
        """Displays info about plant."""
        if self.blooming is True:
            print(f"- {self.name}: "
                  f"{self.height}cm, {self.color} flowers (blooming), "
                  f"Prize points: {self.prize}")
        else:
            print(f"- {self.name}: "
                  f"{self.height}cm, {self.color} flowers (not blooming), "
                  f"Prize points: {self.prize}")


class Garden:
    """
    Represents one garden with a owner and a list of plants.
    """
    def __init__(self, owner: str) -> None:
        """Create new garden."""
        self.owner = owner
        self.plants: list = []
        self.total_plants = 0
        self.total_growth = 0
        self.regular = 0
        self.flower = 0
        self.prizeflower = 0

    def add_plant(self, plant) -> None:
        """Add a plant to the garden."""
        self.plants.append(plant)
        self.total_plants += 1
        print(f"Added {plant.name} to {self.owner}'s garden.")

    def grow_all(self, growth: int = 1) -> None:
        """Grow all plants in the garden."""
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            cm = plant.grow(growth)
            self.total_growth += cm


class GardenManager:
    """Class used to manage info of multiple gardens."""
    def __init__(self) -> None:
        """Create a garden manager."""
        self.gardens: list = []
        self.count = 0

    def add_garden(self, new: Garden) -> None:
        """Add a new garden to the GardenManager."""
        self.gardens.append(new)
        self.count += 1

    def count_garden(self) -> None:
        """Displays how many gardens we are managing."""
        print(f"Total gardens managed: {self.count}")

    def create_garden_network(self, *gardens: Garden) -> None:
        for garden in gardens:
            self.add_garden(garden)

    def garden_scores(self) -> None:
        """Display garden scores."""
        print("Garden scores - ", end="")
        i = 0
        while i < self.count:
            score = GardenManager.calc_score(self.gardens[i])
            print(f"{self.gardens[i].owner}: {score}", end="")
            if i != self.count - 1:
                print(", ", end="")
            i += 1
        print("")

    @staticmethod
    def calc_score(garden: Garden) -> int:
        score = 0
        for plant in garden.plants:
            plant_class = plant.get_class_name()
            if plant_class == "PrizeFlower":
                score += plant.prize
            else:
                score += 1
        return score

    class GardenStats:
        """Class used to calculate and display statistics of a garden."""
        def __init__(self, garden: Garden) -> None:
            """Create garden stats."""
            self.garden = garden

        def report(self) -> None:
            """Displays garden stats."""
            print(f"=== {self.garden.owner}'s Garden Report===")
            print("Plants in garden:")
            for plant in self.garden.plants:
                plant.display_info()
                plant_class = plant.get_class_name()
                if plant_class == "FloweringPlant":
                    self.garden.flower += 1
                elif plant_class == "PrizeFlower":
                    self.garden.prizeflower += 1
                else:
                    self.garden.regular += 1

            print(f"\nPlants added: {self.garden.total_plants}, "
                  f"Total growth: {self.garden.total_growth}cm")
            print(f"Plant types: {self.garden.regular} regular, "
                  f"{self.garden.flower} flowering, "
                  f"{self.garden.prizeflower} prize flowers")

        def height_validation(self) -> None:
            """Validate height."""
            res = True
            for plant in self.garden.plants:
                h = plant.height
                if not GardenManager.GardenStats.validate_height(h):
                    res = False
            print(f"Height validation test: {res}")

        @staticmethod
        def validate_height(h: int) -> bool:
            return h >= 0


def main() -> None:
    """Displays garden network info."""
    print("=== Garden Management System Demo ===\n")
    alice = Garden("Alice")
    bob = Garden("Bob")

    manager = GardenManager()
    manager.create_garden_network(alice, bob)

    oak = Plant("Oak Tree", 100, 1825)
    rose = FloweringPlant("Rose", 25, 30, "red", True)
    sunflower = PrizeFlower("Sunflower", 50, 80, "yellow", True, 10)

    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)

    print("")
    alice.grow_all()

    print("")
    alice_stats = manager.GardenStats(alice)
    alice_stats.report()

    print("")
    alice_stats.height_validation()
    manager.garden_scores()
    manager.count_garden()


if __name__ == "__main__":
    main()
