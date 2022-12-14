"""
CP1404/CP5632 - Practical
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def calculate_celsius_to_fahrenheit(celsius):
    """Calculates celsius to fahrenheit."""
    return celsius * 9.0 / 5 + 32


def calculate_fahrenheit_to_celsius(fahrenheit):
    """Calculates fahrenheit to celsius."""
    return 5 / 9 * (fahrenheit - 32)


def main():
    """Temperature program."""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = calculate_celsius_to_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = calculate_fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} F")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


main()
