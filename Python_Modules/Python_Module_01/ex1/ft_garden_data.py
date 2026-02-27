class Plants():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def print_plant(self):
        print(f"{self.name.capitalize()}: {self.height}cm, {self.age} days old")

if __name__ == "__main__":
    rose = Plants("rose", 25, 30)
    sunflower = Plants("sunflower", 80, 45)
    cactus = Plants("cactus", 15, 120)
    list_of_plants = [rose, sunflower, cactus]
    for i in list_of_plants:
        i.print_plant()

