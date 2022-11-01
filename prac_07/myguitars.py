"""CP1404 Week 8 Practical Classes 2."""

from prac_06.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Opens file, appends data in file to a list then displays list."""
    guitars = []
    print(f"Reading {FILENAME} file")
    add_data_to_list_from_file(guitars)
    display_guitars(guitars)
    # input(">>> ")  # Testing
    guitars.sort()
    display_guitars(guitars)


def display_guitars(guitars):
    """Displays all guitars from a list."""
    for guitar in guitars:
        print(guitar)


def add_data_to_list_from_file(guitars):
    """Opens a file then adds data from file to list."""
    with open(FILENAME, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], parts[1], parts[2])
            guitars.append(guitar)


main()
