from prac_06.guitar import Guitar


def main():
    guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    my_guitar = Guitar("Guitar", 2013, 10)
    # print(guitar)
    print(f"{guitar.name} get_age() - Expected 100. Got {guitar.get_age()}")
    print(f"{my_guitar.name} get_age() - Expected 9. Got {my_guitar.get_age()}")
    print(f"{my_guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")
    print(f"{my_guitar.name} is_vintage() - Expected False. Got {my_guitar.is_vintage()}")


main()
