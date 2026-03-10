class GardenError(Exception):
    def __init__(self, msg: str) -> None:
        Exception.__init__(self, msg)


class EmptyError(GardenError):
    def __init__(self, name: str) -> None:
        if name == "":
            GardenError.__init__(self, msg="Error "
                                 "adding plant: Plant name cannot be empty!")
        elif name is None:
            GardenError.__init__(self, msg="Error "
                                 "adding plant: Plant name cannot be None!")


class WaterError(GardenError):
    def __init__(self, value: int) -> None:
        if value > 10:
            GardenError.__init__(self, msg="Error checking lettuce: Water "
                                 f"level {value}"
                                 " is too high (max 10)")
        elif value < 1:
            GardenError.__init__(self, msg="Error checking lettuce: "
                                 f"Water level {value}"
                                 " is too low (min 1)")


class SunlightError(GardenError):
    def __init__(self, value: int) -> None:
        if value > 12:
            GardenError.__init__(self, msg=f"Error: Sunlight hours {value}"
                                 " is too low (min 2)")
        elif value < 2:
            GardenError.__init__(self, msg=f"Error: Sunlight hours {value}"
                                 " is too high (max 12)")


class PlantManager():
    def __init__(self, name: str, water: int, sun: int) -> None:
        self.name = name
        self.water = water
        self.sun = sun


class GardenManager():
    def __init__(self) -> None:
        self.list = []

    def add_plants(self, plants: list) -> None:
        print("Adding plants to garden...\n")
        try:
            for plant in plants:
                if plant.name == "" or plant.name is None:
                    raise EmptyError(plant.name)
                self.add_plant(plant)
        except EmptyError as e:
            print(f"{e}")
        print()

    def add_plant(self, plant: "PlantManager") -> None:
        self.list.append(plant)
        print(f"Added {plant.name} successfuly")

    def water_plant(self) -> None:
        print("Watering plants...")
        print("Opening watering system")
        for plant in self.list:
            print(f"Watering {plant.name} - success")
        print("Closing watering system (cleanup)\n")

    def check_plant_health(self) -> None:
        print("Checking plant health...")
        try:
            for plant in self.list:
                if plant.water > 10 or plant.water < 1:
                    raise WaterError(plant.water)
                if plant.sun > 12 or plant.sun < 2:
                    raise WaterError(plant.sun)
                print(f"{plant.name}: healthy "
                      f"(water: {plant.water}), sun: {plant.sun}")
        except WaterError as e:
            print(f"{e}")
        print()


def test_garden_management() -> None:
    tomato = PlantManager("tomato", 5, 8)
    lettuce = PlantManager("lettuce", 15, 10)
    empty = PlantManager("", 3, 7)

    print("=== Garden Management System ===\n")
    plants = GardenManager()
    plants.add_plants([tomato, lettuce, empty])
    plants.water_plant()
    plants.check_plant_health()

    print("Testing error recovery")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("System recovered and continuing...")
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
