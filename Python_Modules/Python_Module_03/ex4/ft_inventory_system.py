import sys


def parse_dic(args: list) -> dict | None:
    inventory = {}
    for arg in args[1:]:
        try:
            key, value = arg.split(":")
            inventory[key] = int(value)
        except ValueError as e:
            print(f"{e}\n")
    if len(inventory):
        return inventory
    return None


def total_items(inventory: dict) -> int:
    sum_value = 0
    for value in inventory.values():
        sum_value += value
    return sum_value


def print_ratio(inventory: dict, total: int) -> None:
    for item in inventory.keys():
        ratio = inventory[item] / total * 100
        print(f"{item}: {inventory[item]} units ({ratio:.1f}%)")
    print()


def categorys(inventory: dict) -> None:
    moderate = {}
    scarce = {}
    for item, quantity in inventory.items():
        if quantity >= 5:
            moderate[item] = quantity
        else:
            scarce[item] = quantity
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}\n")


def get_min(inventory: dict) -> None | int:
    min_value = None
    for value in inventory.values():
        if min_value is None or min_value > value:
            min_value = value
    return min_value


def suggestion(inventory: dict) -> None:
    print("Restock needed: ", end="")
    min_value = get_min(inventory)
    for item, value in inventory.items():
        if value == min_value:
            print(f"{item} ", end="")
    print()


def print_keys(inventory: dict) -> None:
    print("Dictionary keys: ", end="")
    for key in inventory.keys():
        print(f"{key} ", end="")
    print()


def print_values(inventory: dict) -> None:
    print("Dictionary values: ", end="")
    for value in inventory.values():
        print(f"{value} ", end="")
    print()


def print_look(inventory: dict, name: str) -> None:
    for value in inventory.keys():
        if value == name:
            print(f"Sample lookup - '{name}' in inventory: True")
            return
    print(f"Sample lookup - '{name}' in inventory: False")


if __name__ == "__main__":

    inventory = parse_dic(sys.argv)

    if inventory is not None:
        print("=== Inventory System analyzeis ===\n")
        total = total_items(inventory)

        print(f"Total items in inventory: {total}")
        print(f"Unique item types: {len(inventory)}\n")

        print("=== Current Inventory ===")
        print_ratio(inventory, total)

        print("=== Item categorys ===")
        categorys(inventory)

        print("=== Management Suggestions ===")
        suggestion(inventory)
        print()

        print("=== Dictionary Properties Demo ===")
        print_keys(inventory)
        print_values(inventory)
        print_look(inventory, "sword")

    else:
        print("No valid argument was given")
