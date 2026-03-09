def test_msg(name: str) -> None:
    print(f"Testing {name}...")


def garden_operations(error_type: str) -> None:
    if (error_type == "ValueError"):
        try:
            int("abc")
            print("No ValueError was caught\n")
        except ValueError:
            print("Caught ValueError: invalid literal for int()\n")

    elif (error_type == "ZeroDivisionError"):
        try:
            5 / 0
            print("No ZeroDivisionError was caught\n")
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero\n")

    elif (error_type == "FileNotFoundError"):
        try:
            file = open("missing.txt")
            print("No FileNotFoundError was caught\n")
            file.close()
        except FileNotFoundError:
            print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    elif (error_type == "KeyError"):
        try:
            dic = {"plant1": "rose", "plant2": "sunflower"}
            print(dic["plant3"], end="")
            print("No KeyError was caught")
        except KeyError:
            print("Caught KeyError: 'missing\\_plant'\n")

    elif (error_type == "all"):
        try:
            5 / 0
            file = open("missing.txt")
            file.close()
            int("abc")
            dic = {"key1": 1}
            print(dic["key2"])
        except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
            print("Caught an error, but program continues!\n")


def test_error_types() -> None:
    test_msg("ValueError")
    garden_operations("ValueError")

    test_msg("ZeroDivisionError")
    garden_operations("ZeroDivisionError")

    test_msg("FileNotFoundError")
    garden_operations("FileNotFoundError")

    test_msg("KeyError")
    garden_operations("KeyError")

    test_msg("multiple errors together")
    garden_operations("all")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===\n")
    test_error_types()
    print("All error types tested successfully!")
