# This file contains the project password checker, helps user create strong and good passwords.

import string

class PasswordChecker:
    def __init__(self) -> None:
        self.common_passwords : set[str] = self.load_common_passwords()
    
    @staticmethod
    def load_common_passwords() -> set[str]:
        with open("common_passwords_long.txt", "r", encoding="utf-8") as file:
            return {line.strip() for line in file if line}

    @staticmethod
    def score_to_rating(score : int) -> str:
        if score <= 2:
            return "Poor"
        elif score <= 4:
            return "Medium"
        else:
            return "Strong"
    
    def is_common(self, password : str) -> bool:
        return password in self.common_passwords
    
    def rate(self, password : str) -> tuple[str, str]:
        if len(password) <= 8:
            return ("Very Poor", "\nWarning: Password must be 8 or more characters.")
        
        if self.is_common(password=password):
            return ("Very Poor", "\nWarning: Your password is common.")
        
        score : int = 0
        recommendations : str = ""
        
        contains_upper : bool = False
        contains_lower : bool = False
        contains_digit : bool = False
        contains_special : bool = False
        contains_unique : bool = False
        
        for char in set(password):
            if char in string.ascii_lowercase:
                contains_lower = True
            elif char in string.ascii_uppercase:
                contains_upper = True
            elif char in string.digits:
                contains_digit = True
            elif char in string.punctuation:
                contains_special = True
        
        if not contains_lower:
            recommendations += "\nAdd lowercase letters to your password."
        else:
            score += 1
        
        if not contains_upper:
            recommendations += "\nAdd uppercase letters to your password."
        else:
            score += 1
        
        if not contains_digit:
            recommendations += "\nAdd digits to your password."
        else:
            score += 1
        
        if not contains_special:
            recommendations += "\nAdd special characters to your password."
        else:
            score += 1
        
        if len(password)/len(set(password)) < 2:
            contains_unique = True
            score += 1
        else:
            recommendations += "\nAdd unique characters to your password."
        
        rating : str = self.score_to_rating(score=score)
        
        return (rating, recommendations)
            
    
def main() -> None:
    validator : PasswordChecker = PasswordChecker()
    
    print("Welcome to Password Checker!")
    print("Enter your password to check its rating and security level.")
    
    while True:
        password_input : str = input("\nEnter your password: ").strip()
        rating_tuple : tuple[str, str] = validator.rate(password=password_input)
        
        rating : str = rating_tuple[0]
        recommendations : str = rating_tuple[1]
        
        print(f"\nrating: {rating}\n{recommendations}\n")
    

if __name__ == "__main__":
    main()
    
# Version 1 has many problems, redundant code, no annotation and/or docstrings.