import re
from typing import Iterable

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

def is_common_domain(email : str) -> bool:
    return any((domain in email) for domain in ["@gmail.com", "@outlook.com", "@hotmail.com", "@yahoo.com"])

def list_emails(path : str, list_separately : bool = False) -> None:
    # Opening the file and saving the text.
    with open(path, "r", encoding="utf-8") as file:
        file_text : str = file.read()
    
    # Using the extract_emails function to extract emails from the text.
    emails : list[str] = extract_emails(file_text)
    
    if emails:
        # Logic for printing common emails and custom emails separately.
        if list_separately:
            # Separtion of emails
            common_emails : Iterable[str] = filter(is_common_domain, emails)
            custom_emails : Iterable[str] = filter(lambda x : not is_common_domain(x), emails)
            
            # Setting these up for printing purposes
            domain_types : tuple[str, str] = ("\nCommon Domain Emails:", "\nCustom Domain Emails:")
            domain_type_index : int = 0
            
            for list_of_emails in (common_emails, custom_emails):
                # Printing the domain type name.
                print(domain_types[domain_type_index])
                # Printing the list of emails under that domain type.
                for index, email in enumerate(list_of_emails, start=1):
                    print(f"{index}. {email}")
                
                domain_type_index += 1
        else:
            for index, email in enumerate(emails, start=1):
                print(f"{index}. {email}")
    else:
        print("No email was found in file.")

def main() -> None:
    list_emails("Day 18/text.txt", list_separately=True)

if __name__ == "__main__":
    main()