"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

STATE_CODE_TO_STATE_FULL_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory",
                            "WA": "Western Australia",
                            "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(STATE_CODE_TO_STATE_FULL_NAME)

is_valid_input = False
while not is_valid_input:
    try:
        state_code = input("Enter short state: ").upper()
        while state_code != "":
            print(state_code, "is", STATE_CODE_TO_STATE_FULL_NAME[state_code])
            state_code = input("Enter short state: ").upper()
        is_valid_input = True
    except KeyError:
        print("Invalid short state")
print("PROGRAM END")

for state_code, full_name in STATE_CODE_TO_STATE_FULL_NAME.items():
    print(f"{state_code:3} is {full_name}")
