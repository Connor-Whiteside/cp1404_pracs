"""CP1404 guitars program."""
from prac_06.guitar import Guitar


def main():
    """Run Guitars program using guitar class."""
    guitars = []
    print("My Guitars")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(f"{guitar_to_add} added.")
        # guitars.append(Guitar(name, year, cost))
        name = input("Name: ")

    # Testing
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    print(guitars)
    print("These are my Guitars:")
    # max_length = max([len(guitar) for guitar in guitars]
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    # print(guitars)


main()
