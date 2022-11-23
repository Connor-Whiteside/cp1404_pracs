"""CP1404 Unreliable Car Test Prac 09."""
from prac_09.unreliable_car import UnreliableCar


def main():
    """Testing for the unreliable car class."""

    good_car = UnreliableCar("Good Car", 100, 90)
    bad_car = UnreliableCar("Bad Car", 100, 10)

    for i in range(1, 10):
        print(f"Attempting to drive {i}km:")
        print(f"{good_car.name:12} drove {good_car.drive(i):2}km")
        print(f"{bad_car.name:12} drove {bad_car.drive(i):2}km")
        print()

    print(good_car)
    print(bad_car)


main()
