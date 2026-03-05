def rejected_message(name: str, value: int) -> None:
    print(f"\nInvalid operation attempted: {name} {value}cm [REJECTED]")
    print(f"Security: Negative {name} rejected\n")


class SecurePlants():
    def __init__(self,
                 name: str, height: int, age: int) -> None:

        if height >= 0 and age >= 0:
            self.__name = name
            self.__height = height
            self.__age = age
            print(f"Plant created: {self.__name}")
        else:
            if height < 0:
                self.__name = name
                self.__age = age
                self.__height = 0
                rejected_message("height", height)
            if age < 0:
                self.__name = name
                self.__age = 0
                if self.__height != 0:
                    self.__height = height
                rejected_message("age", age)

    def set_height(self, value: int) -> None:
        if value >= 0:
            self.__height = value
            print(f"Height updated: {self.__height}cm [OK]")
        else:
            rejected_message("height", value)

    def set_age(self, value: int) -> None:
        if value >= 0:
            self.__age = value
            print(f"Age updated: {self.__age} days [OK]")
        else:
            rejected_message("age", value)

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def get_info(self) -> None:
        print(f"Current plant: {self.__name} ({self.get_height()}cm"
              f", {self.get_age()} days)")


if __name__ == "__main__":
    rose = SecurePlants("Rose", 25, 30)
    rose.set_height(-5)
    rose.get_info()
