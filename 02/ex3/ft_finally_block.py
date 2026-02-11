def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if not isinstance(plant, str):
                raise TypeError(f"Error: cannot water {plant} "
                                "- invalid plant!")
            print(f"Watering {plant}")
    except TypeError as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    plant_list1 = ["tomato", "lettuce", "carrots"]
    plant_list2 = ["tomato", None, "carrots"]

    print("=== Garden Watering System ===")

    print("")
    print("Testing normal watering...")
    water_plants(plant_list1)
    print("Watering completed successfully!")

    print("")
    print("Testing with error...")
    water_plants(plant_list2)

    print("")
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
