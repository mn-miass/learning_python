class NoneError(Exception):
    def __init__(self, msg: str = "Error: Cannot water None"
                 " - invalid plant!") -> None:
        Exception.__init__(self, msg)


def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise NoneError()
            print(f"watering {plant}")
    except NoneError as e:
        print(f"{e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    plant_a = ["tomato", "lettuce", "carrots"]
    plant_b = ["tomato", None, "carrot"]

    print("Testing normal watering...")
    water_plants(plant_a)
    print("Watering completed successfully!")
    print()

    print("Testing with error...")
    water_plants(plant_b)
    print()


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
    print("Cleanup always happens, even with errors!")
