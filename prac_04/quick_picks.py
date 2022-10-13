import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45

number_of_quick_pick = int(input("How many quick picks? "))


while number_of_quick_pick < 0:
    print("Invalid number. Needs to be greater then 0.")
    number_of_quick_pick = int(input("How many quick picks? "))

for i in range(number_of_quick_pick):
    quick_pick = []
    for j in range(NUMBERS_PER_LINE):
        number = random.randint(MINIMUM, MAXIMUM)
        while number in quick_pick:
            number = random.randint(MINIMUM, MAXIMUM)
        quick_pick.append(number)
    quick_pick.sort()
    print(f" ".join("{:2}".format(number) for number in quick_pick))
# print(quick_pick)