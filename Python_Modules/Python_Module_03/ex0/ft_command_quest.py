import sys


def print_arguments() -> None:
    i = 1
    for arg in sys.argv[1:]:
        print(f"Argument {i}: {arg}")
        i += 1


def program_name() -> None:
    print(f"Program name: {sys.argv[0]}")


def total_arguments() -> None:
    print(f"Total arguments: {len(sys.argv)}\n")


if __name__ == "__main__":

    print("=== Command Quest ===")

    if len(sys.argv) == 1:
        print("No arguments provided!")
        program_name()
        total_arguments()

    else:
        program_name()
        print(f"Arguments received: {len(sys.argv) - 1}")
        print_arguments()
        total_arguments()
