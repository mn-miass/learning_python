import math
import sys


def create_position(a: int, b: int, c: int) -> tuple:
    position = (a, b, c)
    return position


def distance(position_a: tuple, position_b: tuple) -> None:
    x1, y1, z1 = position_a
    x2, y2, z2 = position_b

    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f"Distance between {position_b} and {position_a}: {dist:.2f}\n")


def parse_position(arg: str) -> tuple | None:
    try:
        lst = arg.split(",")
        if len(lst) != 3:
            raise ValueError("You need 3 numbers")
        print(f"Parsing coordinates: \"{arg}\"")
        position = create_position(int(lst[0]), int(lst[1]), int(lst[2]))
        print(f"Parsed position: {position}\n")
        return position
    except ValueError as e:
        print(f"Parsing invalid coordinates: \"{arg}\"")
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: (\"{e}\")\n")


def base_cases() -> None:
    position_a = create_position(10, 20, 5)
    print(f"Position created: {position_a}")
    position_b = (0, 0, 0)
    distance(position_a, position_b)

    position_a = parse_position("3,4,0")
    if position_a is not None:
        distance(position_a, position_b)

    position_a = parse_position("abc,def,ghi")

    unpacking((10, 20, 3))


def unpacking(position: tuple) -> None:
    x, y, z = position
    print("Unpacking demonstration:")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}\n")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    if len(sys.argv) == 1:
        base_cases()
    else:
        position_a = parse_position(sys.argv[1])
        if len(sys.argv) > 2:
            position_b = parse_position(sys.argv[2])
        else:
            position_b = (0, 0, 0)
        if position_a is not None and position_b is not None:
            distance(position_a, position_b)
            unpacking(position_a)
            unpacking(position_b)
