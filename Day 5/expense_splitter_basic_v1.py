# This is version one of expense splitter program which  can be used to split expense/bill between number of people
import sys

def delete_last_line() -> None:
    "Use this function to delete the last line in the STDOUT"

    # move cursor up one line
    sys.stdout.write('\x1b[1A')

    # delete last line
    sys.stdout.write('\x1b[2K')


# Welcome Display
print("\nWelcome to Split Calculator, easily split the total expense / bill between your friends.\n\n" + "=" * 50)


# User Inputs
total_bill_amount : float = float(input("\nEnter the total bill amount to be split: "))
split_participants : list[str] = list()
counter : int = 1

print("\nEnter the names of split participants (press blank enter to end): ")
while True:
    user_input : str = input(f"Name ({counter}): ")
    if user_input == "":
        delete_last_line()
        print("")
        break
    
    elif user_input in split_participants:
        print(f"\n{user_input} is already entered. Enter another name.\n")
    
    else:
        split_participants.append(user_input)
        counter += 1

split_divisions : dict[str, float] = dict()

for participant in split_participants:
    split_division_perc_input : float = float(input(f"Enter the split percentage for {participant:8}: "))
    split_divisions.setdefault(participant, split_division_perc_input)


# Calculation and Display
print("\n" + "=" * 50 + "\n")
print(f"Total Amount: {total_bill_amount}")
print("Split between participants:")

for participant, split_division_perc in split_divisions.items():
    print(f"{participant:12}({split_division_perc:.1f}%):    \u20B9{(split_division_perc * total_bill_amount / 100)}")

print("\n" + "=" * 50 + "\n")