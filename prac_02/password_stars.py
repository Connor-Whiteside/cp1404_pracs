MINIMUM_PASSWORD_LENGTH = 8
password = input("Password: ")
while len(password) < MINIMUM_PASSWORD_LENGTH:
    print("Password too short")
    password = input("Password: ")
print("*" * len(password))