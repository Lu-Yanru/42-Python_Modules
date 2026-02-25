import sys


def parse_input() -> dict:
    """Parse the input and store them in a dictionary."""
    inventory = {}
    item = ""
    number = ""
    for arg in sys.argv[1:]:
        for c in arg:
            if c == ":":
                for c in arg:
                    number += c
                break
            item += c
        number = number[len(item) + 1:]
        try:
            inventory[item] = int(number)
        except ValueError:
            print(f"Invalid input, {number} is not a number.")
            exit()
        item = ""
        number = ""
    return inventory


def total_items(inventory: dict) -> int:
    """Caclulates the total number of items in the inventory."""
    return sum(inventory.values())


def print_inventory(inventory: dict) -> None:
    """Prints the contents of the dictionary with percentage."""
    total = total_items(inventory)
    for item, number in inventory.items():
        percentage = number / total * 100
        if number > 1:
            print(f"{item}: {number} units ({percentage:.1f}%)")
        else:
            print(f"{item}: {number} unit ({percentage:.1f}%)")


def find_most_abundant(inventory: dict) -> None:
    """Find and print out the most abundant item in the invenotry."""
    max = 0
    for key, num in inventory.items():
        if num > max:
            max = num
            item = key
    if max > 1:
        print(f"Most abundant: {item} ({max} units)")
    else:
        print(f"Most abundant: {item} ({max} unit)")


def find_least_abundant(inventory: dict) -> None:
    """Find and print out the least abundant item in the invenotry."""
    min = sys.maxsize
    for key, num in inventory.items():
        if num < min:
            min = num
            item = key
    if min > 1:
        print(f"Most abundant: {item} ({min} units)")
    else:
        print(f"Most abundant: {item} ({min} unit)")


def print_categories(inventory: dict) -> None:
    """Print out items based on their rarity categories."""
    moderate = ["potion"]
    scarce = ["sword", "shield", "armor", "helmet"]
    rarity_dict = {
        "moderate": {},
        "scarce":
    }


def main() -> None:
    if len(sys.argv) < 2:
        print("No input. "
              "Usage: python3 ft_inventory_system.py item:number ...")
        return

    print("=== Inventory System Analysis ===")
    inventory = parse_input()
    print(f"Total item in inventory: {total_items(inventory)}")
    print(f"Unique item types: {len(inventory)}")

    print("")
    print("=== Current inventory ===")
    print_inventory(inventory)

    print("")
    print("=== Inventory Statistics ===")
    find_most_abundant(inventory)
    find_least_abundant(inventory)

    print("")
    print("=== Item Categories ===")
    print_categories(inventory)


if __name__ == "__main__":
    main()
