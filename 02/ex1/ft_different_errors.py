def garden_operations(string: str = "1", num: int = 1,
                      file: str = "ft_different_error.py",
                      key: str = "height") -> int:
    try:
        res = int(string)
    except ValueError:
        raise ValueError("Caught ValueError: invalid literal for int()")

    try:
        res = res // num
    except ZeroDivisionError:
        raise ZeroDivisionError("Caught ZeroDivisionError: \
                                division by zero")

    try:
        open(file, "r")
    except FileNotFoundError:
        raise FileNotFoundError(f"Caught FileNotFoundError: \
                                No such file '{file}'")

    try:
        dictionary = {"height": 30, "age": 25}
        print(dictionary[key])
    except KeyError:
        raise KeyError(f"Caught KeyError: '{key}'")

    return res


def test_error_types() -> None:
    print("Testing ValueError...")
    try:
        garden_operations(string="abc")
    except ValueError as e:
        print(e)

    print("Testing ZeroDivisionError...")
    try:
        garden_operations(num=0)
    except ValueError as e:
        print(e)

    print("Testing ZeroDivisionError...")
    try:
        garden_operations(num=0)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")

    test_error_types()

    print("")
    print("All tests completed - program didn't crash!")
