"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

state_code_to_state_name = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory",
                            "WA": "Western Australia",
                            "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(state_code_to_state_name)

is_valid_input = False
while not is_valid_input:
    try:
        state = input("Enter short state: ").upper()
        print(state, "is", state_code_to_state_name[state])
        is_valid_input = True
    except KeyError:
        print("Invalid short state")

for state, full_name in state_code_to_state_name.items():
    print(f"{state:3} is {full_name}")
