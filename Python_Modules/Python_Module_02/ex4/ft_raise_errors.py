def testing_msg(name: str) -> None:
    print(f"Testing {name}...")


def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    if (plant_name == ""):
        raise ValueError("Error: Plant name cannot be empty!\n")

    if (water_level > 10):
        raise ValueError(f"Error: Water level {water_level} "
                         "is too high (max_value 10)")

    if (water_level < 1):
        raise ValueError(f"Error: Water level {water_level} "
                         "is too low (min 1)")

    if (sunlight_hours > 12):
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                         "is too low (min 2)")

    if (sunlight_hours < 2):
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                         "is too high (min 12)")

    print("Plant 'tomato' is healthy!\n")


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===\n")

    try:
        testing_msg("good values")
        check_plant_health("tomato", 9, 10)
    except ValueError as e:
        print(f"{e}\n")

    try:
        testing_msg("empty plant name")
        check_plant_health("", 9, 10)
    except ValueError as e:
        print(f"{e}\n")

    try:
        testing_msg("bad water level")
        check_plant_health("Rose", 15, 10)
    except ValueError as e:
        print(f"{e}\n")

    try:
        testing_msg(" bad sunlight hours")
        check_plant_health("Rose", 9, 0)
    except ValueError as e:
        print(f"{e}\n")

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
