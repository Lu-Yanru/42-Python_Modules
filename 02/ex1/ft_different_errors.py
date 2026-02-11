def garden_operations(string: str = "1", num: int = 1,
                      file: str = "ft_different_errors.py",
                      key: str = "height") -> int:
    try:
        res = int(string)
    except ValueError:
        raise ValueError("Caught ValueError: invalid literal for int()\n")

    try:
        res = res // num
    except ZeroDivisionError:
        raise ZeroDivisionError("Caught ZeroDivisionError: division by zero\n")

    try:
        open(file)
    except FileNotFoundError:
        raise FileNotFoundError("Caught FileNotFoundError: "
                                f"No such file '{file}'\n")

    try:
        dictionary = {"height": 30, "age": 25}
        print(dictionary[key])
    except KeyError:
        raise KeyError(f"Caught KeyError: '{key}'\n")

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
    except ZeroDivisionError as e:
        print(e)

    print("Testing FileNotFoundError...")
    try:
        garden_operations(file="missing.txt")
    except FileNotFoundError as e:
        print(e)

    print("Testing KeyError...")
    try:
        garden_operations(key="missing_plant")
    except KeyError as e:
        print(str(e.args[0]))

    print("Testing multiple errors together...")
    try:
        garden_operations("abc", 0, "missing.txt", "missing_plant")
    except Exception:
        print("Caught an error, but program continues!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")

    test_error_types()

    print("")
    print("All tests completed - program didn't crash!")
