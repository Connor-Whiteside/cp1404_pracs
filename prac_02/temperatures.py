"""
CP1404/CP5632 - Practical
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()


def calculate_celsius_to_fahrenheit():
    return celsius * 9.0 / 5 + 32


def calculate_fahrenheit_to_celsius():
    return 5 / 9 * (fahrenheit - 32)


while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = calculate_celsius_to_fahrenheit()
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = calculate_fahrenheit_to_celsius()
        print(f"Result: {celsius:.2f} F")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
