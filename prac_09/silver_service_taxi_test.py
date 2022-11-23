"""CP1404 Silver Service Taxi Testing Prac 09."""
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Testing for Silver Service Taxi."""
    s1 = SilverServiceTaxi("Gold Taxi", 100, 2)
    print(s1)
    s1.drive(18)
    print(f"Total Cost: ${s1.get_fare():.2f}")
    print(s1)


main()
