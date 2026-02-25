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
    """
    Prints the contents of the dictionary with percentage
    sorted from the most abundant to the least.
    """
    total = total_items(inventory)
    sorted_dict = dict(sorted(inventory.items(), key=lambda item: item[1],
                       reverse=True))
    for item, number in sorted_dict.items():
        percentage = number / total * 100
        if number > 1:
            print(f"{item}: {number} units ({percentage:.1f}%)")
        else:
            print(f"{item}: {number} unit ({percentage:.1f}%)")


def find_most_abundant(inventory: dict) -> None:
    """Find and print out the most abundant item in the invenotry."""
    maxn = max(inventory.values())
    for key, num in inventory.items():
        if num == maxn:
            break
    if maxn > 1:
        print(f"Most abundant: {key} ({maxn} units)")
    else:
        print(f"Most abundant: {key} ({maxn} unit)")


def find_least_abundant(inventory: dict) -> None:
    """Find and print out the least abundant item in the invenotry."""
    minn = min(inventory.values())
    for key, num in inventory.items():
        if num == minn:
            break
    if minn > 1:
        print(f"Most abundant: {key} ({minn} units)")
    else:
        print(f"Most abundant: {key} ({minn} unit)")


def print_categories(inventory: dict) -> None:
    """Print out items based on their rarity categories."""
    moderate = ["potion", "arrow"]
    scarce = ["sword", "shield", "armor", "helmet"]
    rarity_dict: dict = {
        "moderate": {},
        "scarce": {}
    }
    for item in moderate:
        try:
            rarity_dict["moderate"].update({item: inventory[item]})
        except KeyError:
            continue
    for item in scarce:
        try:
            rarity_dict["scarce"].update({item: inventory[item]})
        except KeyError:
            continue
    print(f"Moderate: {rarity_dict["moderate"]}")
    print(f"Scarce: {rarity_dict["scarce"]}")


def formate_list(lst: list) -> str:
    """Formate list items into a string separated by comma."""
    res = ""
    length = len(lst)
    for item in lst:
        res += str(item)
        if length > 1:
            res += ", "
        length -= 1
    return res


def print_suggestions(inventory: dict) -> None:
    """
    Check the inventory for items with less than 2 pieces left
    and print out a message to restock these items.
    """
    restock = []
    for item, num in inventory.items():
        if num < 2:
            restock += [item]
    print(f"Restock needed: {formate_list(restock)}")


def dict_demo(inventory: dict) -> None:
    """Print dict demo info."""
    keys = []
    values = []
    for key, value in inventory.items():
        keys += [key]
        values += [value]
    print(f"Dictionary keys: {formate_list(keys)}")
    print(f"Dictionary values: {formate_list(values)}")


def sample_lookup(inventory: dict, key: str) -> None:
    """
    Look up a key in the dictionary.
    Prints out a message whether it exists.
    """
    try:
        inventory[key]
        print(f"Sample lookup - '{key}' in inventory: True")
    except KeyError:
        print(f"Sample lookup - '{key}' in inventory: False")


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

    print("")
    print("=== Management Suggestions ===")
    print_suggestions(inventory)

    print("")
    print("=== Dictionary Properties Demo ===")
    dict_demo(inventory)
    sample_lookup(inventory, "sword")
    sample_lookup(inventory, "arrow")


if __name__ == "__main__":
    main()
