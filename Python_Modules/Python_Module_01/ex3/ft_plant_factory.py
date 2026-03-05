class Plant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.age = age
        self.height = height

    def get_info(self) -> None:
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


if __name__ == "__main__":
    count = 0

    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)

    plants = [rose, oak, cactus, sunflower, fern]

    print("=== Plant Factory Output ===")
    for plant in plants:
        plant.get_info()
        count += 1

    print(f"\nTotal plants created: {count}")
