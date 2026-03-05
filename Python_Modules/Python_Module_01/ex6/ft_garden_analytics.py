class GardenManager():
    gardens = []

    def __init__(self, name: str) -> None:
        self.name = name
        self.plants = []
        self.total_grow = 0
        self.total_plants = 0
        self.regular = 0
        self.flowering = 0
        self.prize = 0
        self.score = 0
        GardenManager.gardens.append(self)

    @classmethod
    def create_garden_network(cls, name: str) -> "GardenManager":
        return cls(name)

    @classmethod
    def extract_garden(cls, name: str) -> "GardenManager | None":
        for garden in cls.gardens:
            if garden.name == name:
                return garden

    @classmethod
    def grow_all_display(cls, name: str) -> None:
        print()
        garden = cls.extract_garden(name)
        print(f"{garden.name} is helping all plants grow...")
        for plant in garden.plants:
            plant.grow_display()
            garden.total_grow += 1
            garden.score += 10
        print()

    @classmethod
    def grow_all_no_display(cls, name: str) -> None:
        garden = cls.extract_garden(name)
        for plant in garden.plants:
            plant.grow_no_display()
            garden.total_grow += 1
            garden.score += 10

    @classmethod
    def add_plants_display(cls, name: str, plants: list) -> None:
        garden = cls.extract_garden(name)
        print()
        for plant in plants:
            garden.plants.append(plant)
            print(f"Added {plant.name} to {garden.name}'s garden")
            garden.total_plants += 1
            if plant.flag == 0:
                garden.regular += 1
            elif plant.flag == 1:
                garden.flowering += 1
            else:
                garden.prize += 1

        print()

    @classmethod
    def add_plants_no_display(cls, name: str, plants: list) -> None:
        garden = cls.extract_garden(name)
        for plant in plants:
            garden.plants.append(plant)
            garden.total_plants += 1
            if plant.flag == 0:
                garden.regular += 1
            elif plant.flag == 1:
                garden.flowering += 1
            else:
                garden.prize += 1

    class GardenStats():

        @staticmethod
        def display_all(name: str) -> None:
            garden = GardenManager.extract_garden(name)
            for plant in garden.plants:
                plant.display()
            print()

        @staticmethod
        def display_grow(name: str) -> None:
            garden = GardenManager.extract_garden(name)
            print(f"Plants added: {garden.total_plants}, "
                  f"Total growth: {garden.total_grow}")

        @staticmethod
        def display_types(name: str) -> None:
            garden = GardenManager.extract_garden(name)
            print(f"Plant types: {garden.regular} regular, "
                  f"{garden.flowering} flowering, "
                  f"{garden.prize} prize flowers")

        @staticmethod
        def get_garden_number() -> int:
            count = 0
            for plant in GardenManager.gardens:
                count += 1
            return count

        @staticmethod
        def display_garden_number() -> None:
            count = GardenManager.GardenStats.get_garden_number()
            print(f"Total gardens managed: {count}")

        @staticmethod
        def height_validation() -> None:
            print("Height validation test: ", end="")
            for garden in GardenManager.gardens:
                for plant in garden.plants:
                    if plant.height < 0:
                        print("False")
                        return
            print("True")

        @staticmethod
        def garden_score() -> None:
            score = 0
            num = GardenManager.GardenStats.get_garden_number()
            print("Garden scores - ", end="")
            for garden in GardenManager.gardens:
                score += garden.score
                print(f"{garden.name}", end="")
                for plant in garden.plants:
                    score += plant.height
                    if plant.flag == 2:
                        score += plant.prize
                print(f": {score}", end="")
                if num > 1:
                    print(", ", end="")
                num -= 1
                score = 0
            print()

        @staticmethod
        def garden_report(name: str) -> None:
            garden = GardenManager.extract_garden(name)
            print()
            print(f"=== {garden.name}'s Garden Report ===")
            garden.GardenStats.display_all(garden.name)
            garden.GardenStats.display_grow(garden.name)
            garden.GardenStats.display_types(garden.name)
            print()

        @staticmethod
        def get_status() -> None:
            GardenManager.GardenStats.height_validation()
            GardenManager.GardenStats.garden_score()
            GardenManager.GardenStats.display_garden_number()


class Plant():
    flag = 0

    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def display(self) -> None:
        print(f"- {self.name}: {self.height}cm")

    def grow_display(self) -> None:
        self.height += 1
        print(f"{self.name} grew 1 cm")

    def grow_no_display(self) -> None:
        self.height += 1


class FloweringPlant(Plant):
    flag = 1

    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color

    def display(self) -> None:
        print(f"- {self.name}: {self.height}cm, "
              f"{self.color} flowers (blooming)")


class PrizeFlower(FloweringPlant):
    flag = 2

    def __init__(self, name: str, height: int, color: str, prize: int) -> None:
        super().__init__(name, height, color)
        self.prize = prize

    def display(self) -> None:
        print(f"- {self.name}: {self.height}cm, {self.color} "
              f"flowers (blooming), Prize points: {self.prize}")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")

    gardens = GardenManager
    alice = gardens.create_garden_network("Alice")
    bob = gardens.create_garden_network("Bob")

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    cactus = Plant("Cactus", 30)
    tulip = FloweringPlant("Tulip", 10, "pink")
    orchid = PrizeFlower("Orchid", 15, "purple", 4)

    gardens.add_plants_display("Alice", [oak, rose, sunflower])
    gardens.grow_all_display("Alice")

    gardens.add_plants_no_display("Bob", [cactus, tulip, orchid])
    gardens.grow_all_no_display("Bob")

    gardens.GardenStats.garden_report("Alice")
    gardens.GardenStats.get_status()
