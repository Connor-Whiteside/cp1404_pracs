"""Week 3: Files.py."""
# 1.
name = input("Name: ")
out_file = open("name.txt", 'w')
print(name, file=out_file)
out_file.close()
# 2.
in_file = open("name.txt", 'r')
for line in in_file:
    print(f"Your name is {line}")
in_file.close()

# 3.
in_file = open("numbers.txt", 'r')
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(f"Total is {number1 + number2}")

# 4.
total = 0

with open("numbers.txt", "r") as in_file:
    for line in in_file:
        total += int(line)
print(f"Total is {total}")
