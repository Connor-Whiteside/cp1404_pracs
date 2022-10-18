"""
emails.py
Estimate: 30 min 12:10
Actual: 30 min 12:40
"""


def main():
    """Creates a dictionary of emails to names."""
    email_to_name = {}
    email = input("Enter Email: ")
    while email != "":
        name = get_name_from_email(email)
        # print(email)
        check = input(f"Is this your name {name}? (Y/n) ")
        if check.upper() != "Y" and check != "":
            name = input("Name: ")
        email_to_name[email] = name
        # print(name)
        email = input("Enter Email: ")

    for email, name in email_to_name.items():
        print(f"{name} | ({email})")
    print("PORGRAM DONE")


def get_name_from_email(email):
    """Extract expected name from email address."""
    prefix = email.split('@')[0]  # Splits name from the email address
    parts = prefix.split(".")  # Splits around '.'
    name = " ".join(parts).title()  # Sets name
    return name


main()
