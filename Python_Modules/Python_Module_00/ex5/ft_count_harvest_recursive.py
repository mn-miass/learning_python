def print_day(value):
    if value == 0:
        return
    print_day(value - 1)
    print(f"Day {value}")


def ft_count_harvest_recursive():
    print_day(5)
    print("Harvest time!")
