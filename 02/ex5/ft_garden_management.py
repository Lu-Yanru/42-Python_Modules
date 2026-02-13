class GardenError(Exception):
    """A basic error for garden."""
    pass


class PlantError(GardenError):
    """For problem with plants."""
    pass


class WaterError(PlantError):
    """For problems with watering."""
    pass


class SunlightError(PlantError):
    """For problems with sunlight."""
    pass


class Plant:
    """A class that represents a plant."""
    def __init__(self, name: str, water: int, sun: int) -> None:
        self.name = name
        self.water = water
        self.sun = sun


class GardenManager:
    """
    The GardenManager class has methods to add plants,
    water plants and check plant health.
    """
    def __init__(self) -> None:
        """Initialize a GardenManager."""
        self.plants: list[Plant] = []
        self.tank = 1

    def add_plant(self, plant_list: list[Plant]) -> None:
        """
        A method to add plant.
        Raises an error if plant name is empty.
        """
        print("Adding plants to garden...")
        for plant in plant_list:
            if plant.name == "":
                raise PlantError("Error adding plant: "
                                 "Plant name cannot be empty!")
            self.plants.append(plant)
            print(f"Added {plant.name} successfully")

    def water_plants(self) -> None:
        """
        A funtion that waters a list of plants.
        For each plant, check whether it is a string.
        If yes, print a message.
        If not, raise an error.
        """
        print("Watering plants...")
        print("Opening watering system")
        try:
            for plant in self.plants:
                if plant.name == "":
                    raise PlantError(f"Error: cannot water {plant}: "
                                     "Plant name cannot be empty!")
                print(f"Watering {plant.name} - success")
        except PlantError as e:
            print(e)
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self) -> None:
        """
        A function that:
        checks if the plant name is valid (not empty),
        checks if water level is reasonable (between 1 and 10),
        checks if sunlight hours are reasonable (between 2 and 12),
        raises error when an attribute is not valid,
        returns a success message if everything is ok.
        """
        print("Checking plant health...")
        for plant in self.plants:
            if plant.name == "":
                raise PlantError("Error: Plant name cannot be empty!")
            if plant.water < 1:
                raise WaterError(f"Error checking {plant.name}: Water level "
                                 f"{plant.water} is too low (min 1)")
            if plant.water > 10:
                raise WaterError(f"Error checking {plant.name}: Water level "
                                 f"{plant.water} is too high (max 10)")
            if plant.sun < 2:
                raise SunlightError(f"Error checking {plant.name}: "
                                    f"Sunlight hours {plant.sun} "
                                    "is too low (min 2)")
            if plant.sun > 12:
                raise SunlightError(f"Error checking {plant.name}: "
                                    f"Sunlight hours {plant.sun} "
                                    "is too high (max 10)")
            print(f"{plant.name}: "
                  f"healthy (water: {plant.water}, "
                  f"sun: {plant.sun})")

    def check_tank_level(self) -> None:
        """
        If tank level is more than 5, print message,
        else raise error.
        """
        if self.tank > 5:
            print("There is enough water in the tank.")
        else:
            raise GardenError("Caught GardenError: Not enough water in tank")


def test_garden_management() -> None:
    print("=== Garden Management System ===")
    tomato = Plant("tomato", 5, 8)
    lettuce = Plant("lettuce", 15, 3)
    empty = Plant("", 2, 3)
    plants = [tomato, lettuce, empty]

    manager = GardenManager()

    print("")
    try:
        manager.add_plant(plants)
    except PlantError as e:
        print(e)

    print("")
    manager.water_plants()

    print("")
    try:
        manager.check_plant_health()
    except (PlantError, WaterError, SunlightError) as e:
        print(e)

    print("")
    print("Testing error recovery...")
    try:
        manager.check_tank_level()
    except GardenError as e:
        print(e)
    finally:
        print("System recovered and continuing...")

    print("")
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
