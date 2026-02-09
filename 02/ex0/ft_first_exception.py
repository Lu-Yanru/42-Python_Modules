def check_temperature(temp_str: str) -> int:
    """
    A function that checks the temperature given as argument.
    It converts the argument given as a string to an integer.
    Returns the given temperature if it is betwenn 0 and 40,
    None otherwise and prints out an error message.
    """
    try:
        temp = int(temp_str)
    except ValueError:
        raise ValueError(f"Error: {temp_str} is not a valid number")
    if temp < 0:
        raise ValueError(f"Error: {temp}°C is too cold for plants (min 0°C)")
    elif temp > 40:
        raise ValueError(f"Error: {temp}°C is too hot for plants (max 40°C)")
    else:
        print(f"Temperature {temp}°C is perfect for plants!")
        return temp


def test_temperature_input(temp_str: str) -> None:
    """
    A function that tests various input for
    the check_temperature() function.
    """
    print(f"Testing temperature: {temp_str}")
    try:
        check_temperature(temp_str)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")

    test_temperature_input("25")

    print("")
    test_temperature_input("abc")

    print("")
    test_temperature_input("100")

    print("")
    test_temperature_input("-50")

    print("")
    print("All tests completed - program didn't crash!")
