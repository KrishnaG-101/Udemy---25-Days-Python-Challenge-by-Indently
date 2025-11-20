# This file contains program for grocery list project, which allows users to create a grocery list temporarily in terminal.

grocery_list_database : dict[str, int] = dict()

def announcement(message : str) -> None:
    # Just prints the given message with the preceeding word "System" in order to give system output to user or prompt the user.
    print(f"\nSystem: {message}")

def take_grocery_input() -> str:
    grocery_item_input : str = input("Enter an item: ").lower().strip()
    
    if grocery_item_input == "":
        announcement("Please enter a value for item name, it cannot be empty.\n")
        return take_grocery_input()
    
    return grocery_item_input

def take_quantity_input() -> int:
    try:
        quantity_input : int = int(input("Enter a quantity: "))
        return quantity_input
    except ValueError:
        announcement("Please enter a valid value for quantity.\n")
        return take_quantity_input()

def add_item(grocery_item : str, quantity : int) -> None:
    if grocery_list_database.get(grocery_item):
        announcement("The item already exists in the grocery list, kindly use the update option if you want to update the quantity.")
    else:
        grocery_list_database.setdefault(grocery_item, quantity)
        announcement(f"Item {grocery_item.capitalize()} x {quantity} successfully added to the list")

def remove_item(grocery_item : str) -> None:
    try:
        grocery_list_database.pop(grocery_item)
        announcement(f"Item {grocery_item.capitalize()} successfully removed from the list.")
    except KeyError:
        announcement(f"The entered item: {grocery_item.capitalize()}, is not found in the list.")

def update_item(grocery_item : str, quantity : int) -> None:
    if grocery_list_database.get(grocery_item) != None:
        grocery_list_database[grocery_item] = quantity
        announcement(f"Item {grocery_item.capitalize()} x {quantity} successfully updated in the list.")
    else:
        announcement(f"The entered item: {grocery_item.capitalize()}, is not found in the list, kindly use the add option if you want to add an item.")

def read_list() -> None:
    if grocery_list_database:
        announcement("")
        print("-"*20)
        for grocery_item, quantity in grocery_list_database.items():
            print(f"{grocery_item.capitalize()} x {quantity}")
        print("-"*20)
    else:
        announcement("The grocery list is empty, there are no items to display.")

def display_options() -> None:
    print("\nOptions:")
    print("0 - Display options")
    print("1 - Read the grocery list")
    print("2 - Add an item to grocery list")
    print("3 - Remove an item from grocery list")
    print("4 - Update an item in the grocery list")
    print("5 - Exit Program")
    print("-")

def main() -> None:
    display_options()
    while True:
        try:
            option_chosen : int = int(input("\nYou: "))
            match option_chosen:
                case 0:
                    display_options()
                case 1:
                    read_list()
                case 2:
                    grocery_input : str = take_grocery_input()
                    quantity_input : int = take_quantity_input()
                    add_item(grocery_item=grocery_input, quantity=quantity_input)
                case 3:
                    grocery_input : str = take_grocery_input()
                    remove_item(grocery_item=grocery_input)
                case 4:
                    grocery_input : str = take_grocery_input()
                    quantity_input : int = take_quantity_input() 
                    update_item(grocery_item=grocery_input, quantity=quantity_input)
                case 5:
                    announcement("Thank you for using the program.\n")
                    return None
                case _:
                    raise ValueError("Input is out of range")
        except ValueError as error:
            announcement(f"{error}. Please enter a valid input for options")


if __name__ == "__main__":
    main()
    
# Annotations and Doc Strings are to be added.
# Use file io to save the list in file when exiting and open when program starts.