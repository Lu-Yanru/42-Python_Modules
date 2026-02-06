def garden_operations(error: str) -> None:
    try:
        num = int(string)
    except ValueError:
        raise ValueError("Caught ValueError: invalid literal for int()")
    try:
        res = num / 0
    except ZeroDivisionError:
        raise ZeroDivisionError("Caught ZeroDivisionError: division by zero")
    try:
        open(string)
    except FileNotFoundError:
        raise FileNotFoundError(f"Caught FileNotFoundError: No such file ")

def test_error_types(error: str) -> None:
    print(f"Testing {error}...")
    try:
        garden_operations(error)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")

    test_error_types("ValueError")

    print("")
    test_error_types("abc")

    print("")
    test_error_types("100")

    print("")
    test_error_types("-50")

    print("")
    print("All tests completed - program didn't crash!")
