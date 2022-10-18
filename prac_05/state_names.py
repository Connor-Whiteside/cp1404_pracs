"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

STATE_TO_STATE_FULL_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory",
                            "WA": "Western Australia",
                            "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(STATE_TO_STATE_FULL_NAME)

is_valid_input = False
while not is_valid_input:
    try:
        state = input("Enter short state: ").upper()
        while state != "":
            print(state, "is", STATE_TO_STATE_FULL_NAME[state])
            state = input("Enter short state: ").upper()
        is_valid_input = True
    except KeyError:
        print("Invalid short state")
print("PROGRAM END")

for state, full_name in STATE_TO_STATE_FULL_NAME.items():
    print(f"{state:3} is {full_name}")
