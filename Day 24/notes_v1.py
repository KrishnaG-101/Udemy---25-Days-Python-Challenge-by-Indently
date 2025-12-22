def add_note() -> None:
    note_input : str = input("\nEnter your note:\n")
    
    with open("./Day 24/notes_app.txt", "a") as file:
        file.write(f"{note_input}\n")
    print("\nNote added successfully.")
    
    return None

def view_notes() -> None:
    try:
        with open("./Day 24/notes_app.txt", "r") as file:
            notes : list[str] = file.readlines()
        
        if notes:
            print()
            for index, note in enumerate(notes, start=1):
                print(f"{index} : {note.strip()}")
        else:
            print("\nNo notes found.")

    except FileNotFoundError:
        print("\nNo notes found.")
    
    return None

def delete_note() -> None:
    view_notes()
    
    try:
        with open("./Day 24/notes_app.txt", "r") as file:
            notes : list[str] = file.readlines()
            
        if notes:
            note_id_input : int = int(input("\nEnter note id for note you want to delete: "))
            
            if 1 <= note_id_input <= len(notes):
                notes.pop(note_id_input-1)
                
                with open("./Day 24/notes_app.txt", "w") as file:
                    file.writelines(notes)
                
                print("\nNote deleted successfully.")
                
            else:
                print("\nInvalid Note Id. Enter a valid Note Id to delete that note.")
                
    except FileNotFoundError:
        print("No file found.")
    except ValueError:
        print("\nInvalid Note Id. Enter a valid Note Id in numeric format to delete that note.")
        
    return None

def display_menu() -> None:
    print("\nNote-Taking Application")
    print("0 -> Display Menu.")
    print("1 -> Add a Note.")
    print("2 -> View Notes.")
    print("3 -> Delete a Note.")
    print("4 -> Exit Application.")
    return None

def main() -> None:
    display_menu()
    while True:
        try:
            user_choice : int = int(input("\nEnter your choice: "))
            match user_choice:
                case 0:
                    display_menu()
                case 1:
                    add_note()
                case 2:
                    view_notes()
                case 3:
                    delete_note()
                case 4:
                    print("\nThank you for using our application.\n")
                    break
                case _:
                    raise ValueError 
        except ValueError:
            print("\nOnly enter numerical value for choice (in the given range).")


if __name__ == "__main__":
    main()