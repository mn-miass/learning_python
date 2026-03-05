class Plant():
    def __init__(self, name: str, height: int, ages: int) -> None:
        self.name = name
        self.height = height
        self.ages = ages

    def grow(self, value: int) -> None:
        self.height += value

    def age(self, value: int) -> None:
        self.ages += value

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.ages} days old")

    def simulation(self, value: int) -> None:
        print(f"=== Day {1} ===")
        self.get_info()
        for i in range(2, 8):
            self.grow(value)
            self.age(1)
        print(f"=== Day {7} ===")
        self.get_info()
        print(f"Growth this week: +{value * 6}cm")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    rose.simulation(1)
