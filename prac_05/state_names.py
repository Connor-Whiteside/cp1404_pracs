"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

state_to_state_name = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(state_to_state_name)

state = input("Enter short state: ").upper()
while state != "":
    if state in state_to_state_name:
        print(state, "is", state_to_state_name[state])
    else:
        print("Invalid short state")
    state = input("Enter short state: ").upper()
