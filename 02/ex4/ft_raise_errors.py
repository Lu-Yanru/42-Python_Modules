class PlantError(Exception):
    """A basic error for plants."""
    pass


class WaterError(PlantError):
    """For problems with watering."""
    pass


class SunlightError(PlantError):
    """For problems with sunlight."""
    pass


def check_plant_health(plant_name: str,
                       water_level: int,
                       sunlight_hours: int) -> None:
    """
    A function that:
    checks if the plant name is valid (not empty),
    checks if water level is reasonable (between 1 and 10),
    checks if sunlight hours are reasonable (between 2 and 12),
    raises error when an attribute is not valid,
    returns a success message if everything is ok.
    """
    if plant_name == "":
        raise PlantError("Error: Plant name cannot be empty!")
    if water_level < 1:
        raise WaterError(f"Error: Water level {water_level} is too low"
                         " (min 1)")
    if water_level > 10:
        raise WaterError(f"Error: Water level {water_level} is too high"
                         " (max 10)")
    if sunlight_hours < 2:
        raise SunlightError(f"Error: Sunlight hours {sunlight_hours} "
                            "is too low (min 2)")
    if sunlight_hours > 12:
        raise SunlightError(f"Error: Sunlight hours {sunlight_hours} "
                            "is too high (max 10)")
    print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===")

    print("")
    print("Testing good values...")
    try:
        check_plant_health("tomato", 2, 3)
    except PlantError as e:
        print(e)

    print("")
    print("Testing empty plant name...")
    try:
        check_plant_health("", 2, 3)
    except PlantError as e:
        print(e)

    print("")
    print("Testing bad water level...")
    try:
        check_plant_health("tomato", 15, 3)
    except WaterError as e:
        print(e)

    print("")
    print("Testing bad sunlight hours...")
    try:
        check_plant_health("tomato", 2, 0)
    except SunlightError as e:
        print(e)

    print("")
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
