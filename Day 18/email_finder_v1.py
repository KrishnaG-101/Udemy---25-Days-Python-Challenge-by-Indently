import re

def extract_emails(text : str, unique : bool = True, case_sensitive : bool = True) -> list[str]:
    # Regex to match email patterns.
    email_pattern : str = (
        r'\b[A-Za-z0-9.!#$%&\'*+/=?^_`{|}~-]+@[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?'
        r'(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?)*\.[A-Za-z]{2,}\b'
    )
    
    # To retreive and store all the emails.
    emails : list[str] = re.findall(email_pattern, text)
    
    if unique:
        emails = list(dict.fromkeys(emails))
    
    if not case_sensitive:
        emails = [email.lower() for email in emails]
        
    return emails

def list_emails(path : str) -> None:
    # Opening the file and saving the text.
    with open(path, "r") as file:
        file_text : str = file.read()
    
    # Using the extract_emails function to extract emails from the text.
    emails : list[str] = extract_emails(file_text)
    
    # Printing.
    if emails:
        for index, email in enumerate(emails):
            print(f"{index}. {email}")
    else:
        print("No email was found in file.")

def main() -> None:
    list_emails("Day 18/text.txt")

if __name__ == "__main__":
    main()