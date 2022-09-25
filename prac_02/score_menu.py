"""CP1404 - Score menu program."""

"""
get a valid score (must be 0-100 inclusive) V
print result (copy or import your function from score.py) P
print stars (this should print as many stars as the score) S
quit Q
"""
MENU = """(V)aild score
(P)rint result
(S)tars
(Q)uit"""


def main():
    """Score menu program."""
    score = 0
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "v":
            score = get_valid_score()
        elif choice == "p":
            print(f"{determine_score(score)}")
        elif choice == "s":
            print(f"{display_star(score)}")
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").lower()
    print("Farewell")


def determine_score(score):
    """Determine a result then return a string based on score."""
    if score <= 0:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Pass"
    else:
        return "Excellent"


def get_valid_score():
    """Returns a valid score between 0 and 100."""
    score = int(input("Enter Score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter Score: "))
    return score


def display_star(score):
    """Display asterisks based on score."""
    return "*" * score


main()
