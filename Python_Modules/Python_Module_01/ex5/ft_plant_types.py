class Plant():
    def __init__(self,
                 name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self,
                 name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!\n")

    def get_value(self) -> None:
        print(f"\n{self.name} (Flower): "
              f"{self.height}cm, {self.age} days, {self.color} color")
        self.bloom()


class Tree(Plant):
    def __init__(self, name: str, height: int,
                 age: int, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        radius = self.trunk_diameter / 10
        shade = radius * radius * 3.14
        print(f"{self.name} provides {shade:.0f} square meters of shade\n")

    def get_value(self) -> None:
        print(f"\n{self.name} (Tree): {self.height}cm, "
              f"{self.age} days, {self.trunk_diameter}cm diameter")
        self.produce_shade()


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def nutritional(self) -> None:
        print(f"{self.name} is rich in {self.nutritional_value}\n")

    def get_value(self) -> None:
        print(f"\n{self.name} (Vegetable): {self.height}cm, "
              f"{self.age} days, {self.harvest_season} harvest")
        self.nutritional()


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 25, 30, "red")
    sunflower = Flower("Sunflower", 150, 60, "yellow")

    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 1200, 3650, 35)

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 30, 75, "autumn", "vitamin A")

    rose.get_value()
    sunflower.get_value()

    oak.get_value()
    pine.get_value()

    tomato.get_value()
    carrot.get_value()
