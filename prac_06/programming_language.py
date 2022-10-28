class ProgrammingLanguage:
    """Represents a Programming Language object."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a programming language instance."""

        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Returns a string representation of a ProgrammingLanguage."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"
