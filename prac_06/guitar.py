CURRENT_YEAR = 2022
VINTAGE_AGE = 50


class Guitar:
    """Represents a Guitar object."""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Returns a string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def __repr__(self):
        return str(self)

    def get_age(self):
        """Get the current age of a guitar based on the CURRENT_YEAR."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a Guitar is considered vintage or not based on age."""
        return self.get_age() >= VINTAGE_AGE
