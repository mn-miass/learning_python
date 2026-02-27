class Plant():
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

class Flower(Plant):
    def __init__(self, name, age, height, color):
        super().__init__(name, age, height)
        self.color = color
    
    def to_blom(self):
        print(f"{self.name.capitalize()} is blooming beautifully!")
    
    def print_flower(self):
        print(f"{self.name.capitalize()} (Flower): {self.height}cm, {self.age} days, {self.color} color")
        self.to_blom()

class Tree(Plant):
    def __init__(self, name, age, height, trunk_diameter):
        super().__init__(name, age, height)
        self.trunk_diameter = trunk_diameter
    
    def produce_shade(self):
        print(f"{self.name.capitalize()} provide {self.trunk_diameter} square meters of shade")
    
    def print_tree(self):
        print(f"{self.name.capitalize()}: {self.height}cm, {self.age} days, {self.trunk_diameter}cm diameter")
        self.produce_shade()

class Vegetable(Plant):
    def __init__(self, name, age, height, harvest_season, nutritional_value):
        super().__init__(name, age, height)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
    
    def print_value(self):
        print(f"{self.name} is rich in {self.nutritional_value}")
    
    def print_vegetable(self):
        print(f"{self.name.capitalize()} (Vegetable): {self.height}cm, {self.age} days, {self.harvest_season} harvest")
        self.print_value()

    
if __name__ == "__main__":
    rose = Flower("rose", 30, 25, "red")
    oak = Tree("oak", 1825, 500, 50)
    tomato = Vegetable("tomato", 25, 90, "summer", "vitamin C")
    print("=== Garden Plant Types ===\n")
    rose.print_flower()
    oak.print_tree()
    tomato.print_vegetable()
