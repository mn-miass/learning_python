def error_message(variable, value):
    if variable == "height":
        print(f"\nInvalid operation attempted: {variable} {value}cm [Rjected]")
    elif variable == "age":
        print(f"Invalid operation attempted: {variable} {value}day [Rjected]")
    print(f"Security: Negative {variable} rejected\n")


class SecurePlant():
    def __init__(self, height, age, name):
        if height < 0:
            error_message("height", height)
        elif age < 0:
            error_message("age", age)
        else:
            self.__height = height
            self.__age = age
            self.__name = name
            print(f"Plant created: {self.__name.capitalize()}")

    def set_height(self, value):
        if value < 0:
            error_message("height", value)
        else:
            self.__height = value
            print(f"Height updated: {self.__height} cm [OK]")

    def set_age(self, value):
        if value < 0:
            error_message("age", value)
        else:
            self.__age = value
            print(f"Age updated: {self.__age} days [OK]")
            
    
    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

def print_plant(plant):
     print(f"Current plant: {plant.get_name().capitalize()} ({plant.get_height()}cm, {plant.get_age()}days)")

if __name__ == "__main__":
    rose = SecurePlant(25, 30, "rose")
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-5)
    print_plant(rose)
    
