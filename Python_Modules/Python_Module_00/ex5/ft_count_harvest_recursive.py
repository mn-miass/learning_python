def print_day(value):
    if value <= 0:
        return
    print_day(value - 1)
    print(f"Day {value}")


def ft_count_harvest_recursive():
    value = int(input("Days until harvest: "))
    print_day(value)
    print("Harvest time!")
