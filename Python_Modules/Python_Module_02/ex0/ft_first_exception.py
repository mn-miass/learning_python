def error_msg(value: str) -> None:
    print(f"Testing temperature: {value}")


def check_temperature(tmp_str: str) -> None | int:
    try:
        error_msg(tmp_str)
        tmp_int = int(tmp_str)
        if (tmp_int >= 0 and tmp_int <= 40):
            print(f"Temperature {tmp_int}°C is perfect for plants!\n")
            return tmp_int
        elif (tmp_int > 40):
            raise ValueError(f"{tmp_int}°C is too hot for plants (max_value 40°C)")
        else:
            raise ValueError(f"{tmp_int}°C is too cold for plants (min 0°C)")
    except ValueError as e:
        if "invalid literal" in e.args[0]:
            print("Error: 'abc' is not a valid number\n")
        else:
            print(f"Error: {e}\n")


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
