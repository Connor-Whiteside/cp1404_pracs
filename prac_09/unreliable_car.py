"""
CP1404/CP5632 Practical
Unreliable Car class Prac 09
"""
from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability"""

    def __init__(self, name, fuel, reliability):
        """Initalises an UnreliableCar"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car, only sometimes, based on reliability."""

        if randint(1, 100) >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
