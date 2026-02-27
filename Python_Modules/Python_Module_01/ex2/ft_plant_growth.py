class Plants():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age_day = age

    def print_plant(self):
        print(f"{self.name.capitalize()}: {self.height}cm, {self.age_day} days old")

    def age(self, grow_rate):
        self.age_day += grow_rate

    def grow(self, grow_rate):
        self.height += grow_rate

    def get_info(self, day):
        print(f"=== Day {day} ===")
        self.print_plant()
    
    def simulation(self, grow_rate):
        self.age(grow_rate)
        self.grow(grow_rate)
        self.grow_rate = grow_rate

if __name__ == "__main__":
    rose = Plants("rose", 25, 30)
    rose.get_info(1)
    rose.simulation(6)
    rose.get_info(7)
    print(f"Growth this week: +{rose.grow_rate}cm")