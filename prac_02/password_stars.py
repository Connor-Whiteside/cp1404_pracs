"""Password Program."""


def main():
    """Password program."""
    minimum_password_length = 8
    password = get_password(minimum_password_length)
    display_asterisks(password)


def display_asterisks(password):
    """Print a line of length asterisks."""
    print("*" * len(password))


def get_password(minimum_password_length):
    """Return a password based on a set length."""
    password = input("Password: ")
    while len(password) < minimum_password_length:
        print("Password too short")
        password = input("Password: ")
    return password


main()
