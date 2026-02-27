class Plants():
    def __init__(self, name, height, age):
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def print_plant(self):
        print(f"Created: {self.name} ({self.height}, {self.age} days)")

if __name__ == "__main__":
    rose = Plants("rose", 25, 30)
    oak = Plants("Oak", 200, 365)
    cactus = Plants("cactus", 5, 90)
    sunflower = Plants("sunflower", 80, 45)
    fern = Plants("fern", 15, 120)
    count = 0
    plant_list = [rose, oak, cactus, sunflower, fern]
    print("=== Plant Factory Output ===")
    for plant in plant_list:
        count += 1
        plant.print_plant()
    print(f"Total plants created: {count}")
