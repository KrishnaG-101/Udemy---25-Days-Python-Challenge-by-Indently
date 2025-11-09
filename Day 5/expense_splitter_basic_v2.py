# This is version 2.0 of expense splitter program which  can be used to split expense/bill between number of people
# Changes from previous version:
# Added functionality for even split
# Added a little more guiding text inspired by step procedure implemented in the course video
# Added functionality to allow 0% split on entering blank

import sys

def delete_last_line() -> None:
    """Use this function to delete the last line in the STDOUT"""

    # move cursor up one line
    sys.stdout.write('\x1b[1A')

    # delete last line
    sys.stdout.write('\x1b[2K')


# Welcome Display
print("\nWelcome to Split Calculator, easily split the total expense / bill between your friends.\n")
print("=" * 50)


# User Inputs
# Step 1. Taking input for bill amount
total_bill_amount : float = float(input("\n1. Enter the total bill amount to be split: "))
split_participants : list[str] = list()
counter : int = 1          # Used to print and keep track of number of split participants.

# Step 2. Taking input for participants to split among
print("\n2. Enter the names of split participants (press blank enter to end): ")

while True:
    participant_name : str = input(f"Name ({counter}): ")
    
    if participant_name == "":
        counter -= 1       # To match the length of split_participants.
        delete_last_line()
        break
    
    elif participant_name in split_participants:
        print(f"\n{participant_name} is already entered. Enter another name.\n")
    
    else:
        split_participants.append(participant_name)
        counter += 1

split_divisions : dict[str, float] = dict()  # Will be used to store split share for participant.

# Step 3. Taking input for each participant's share percentage for the expense
print("\n3. Enter percentage of expense each individual has to bear (Enter \"even\" to split evenly):")

for participant in split_participants:
    split_division_perc : str = input(f"Enter the split percentage for {participant:8}: ")
    
    # Adding functionality to divide the expense evenly directly using one word.
    if split_division_perc.strip() == "even":
        # Utilizing list comprehension technique and update function to add key-value pairs to dictionary.
        split_divisions.update([(participant, (total_bill_amount/counter)) for participant in split_participants])
        break
    
    # Using shorthand if-else to check if the percentage entered for a participant is correct and numeric then adding the calculated share.
    split_divisions.setdefault(participant, (float(split_division_perc) * total_bill_amount / 100) if split_division_perc.strip().isnumeric() else 0)


# Calculation and Display
print("\n" + "=" * 50 + "\n")

print(f"Total Amount: {total_bill_amount}")
print("Split between participants:")

for participant, split_share in split_divisions.items():
    print(f"{participant:12}:      \u20B9{split_share:.2f}")

print("\n" + "=" * 50 + "\n")