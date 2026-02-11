class GardenError(Exception):
    """A basic error for garden problems."""
    pass


class PlantError(GardenError):
    """For problems with plants."""
    pass


class WaterError(GardenError):
    """For problems with watering."""
    pass


def test_plant_error(plant: str, wilting: bool) -> None:
    if wilting is False:
        print(f"The {plant} plant is growing well.")
    else:
        raise PlantError(f"The {plant} plant is wilting!")


def test_water_error(water: int) -> None:
    if water > 5:
        print("There is enough water in the tank.")
    else:
        raise WaterError("Not enough water in the tank!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")

    print("")
    print("Testing PlantError...")
    try:
        test_plant_error("tomato", True)
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("")
    print("Testing WaterError...")
    try:
        test_water_error(1)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("")
    print("Testing catching all garden errors...")
    try:
        test_plant_error("tomato", True)
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        test_water_error(1)
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print("")
    print("All custom error types work correctly!")
