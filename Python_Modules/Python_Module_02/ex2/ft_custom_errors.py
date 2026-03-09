def testing_msg(name: str) -> None:
    print(f"Testing {name}...")


class GardenError(Exception):
    def __init__(self, msg: str) -> None:
        Exception.__init__(self, msg)


class PlantError(GardenError):
    def __init__(self, msg: str = "The tomato plant is wilting!") -> None:
        GardenError.__init__(self, msg)


class WaterError(GardenError):
    def __init__(self, msg: str = "Not enough water in the tank!") -> None:
        GardenError.__init__(self, msg)


def test_errors() -> None:
    testing_msg("PlantError")
    try:
        raise PlantError()
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")
    print()
    testing_msg("WaterError")
    try:
        raise WaterError()
    except WaterError as e:
        print(f"Caught a WaterError: {e}")
    print()
    testing_msg("all garden errors")
    for error in [PlantError(), WaterError()]:
        try:
            raise error
        except GardenError as e:
            print(f"Caught a garden error: {e}")
    print()


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    test_errors()
    print("All custom error types work correctly!")
