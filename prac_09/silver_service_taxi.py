"""CP1404 Silver Service Taxi | Prac 09."""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness: float):
        """Initialise a Silver Service Taxi instance, based on class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi, with fanciness."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Get the current fare."""
        return super().get_fare() + self.flagfall
