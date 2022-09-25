"""CP1404/CP5632 - Practical."""

import random


def main():
    """Score program."""
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)
    random_score = random.randint(0, 100)
    result = determine_result(random_score)
    print(f"Your random score is {random_score}")
    print(result)


def determine_result(score):
    """Determine a result then return a string based on score"""
    if score <= 0:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Pass"
    else:
        return "Excellent"


main()
