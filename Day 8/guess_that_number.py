# This file contains code for the project: Guess That Number, which is a simple number guessing game for the user.

from typing import Final
from random import randint


def bot_message(message : str) -> None:
    """Simply prints the computer message for the game.

    Args:
        message (str): message to be printed.
    """
    
    print(f"Computer: {message}")
    
    return None

def guess_the_number_game(lower_limit : int, upper_limit : int) -> int:
    """The main function running the number guessing game logic, checks player input and runs the game.

    Args:
        lower_limit (int): lower limit number for the range
        upper_limit (int): upper limit number for the range

    Raises:
        ValueError: if player input is out of range (lower_lower - upper_limit)

    Returns:
        int: number of attempts made by the player
    """    
    attempts : int = 0
    random_number : int = randint(lower_limit, upper_limit)
    
    print("\nWelcome to Guess That Number Game!")
    bot_message(f"Choose a number between {lower_limit} and {upper_limit}")
    
    while True:
        try:
            player_guess : int = int(input("\nEnter your guess: "))
            
            if player_guess < lower_limit or player_guess > upper_limit:
                raise ValueError("Input out of range.")
            else:
                attempts += 1
            
            if player_guess > random_number:
                bot_message("The number is lower than your guess.")
            elif player_guess < random_number:
                bot_message("The number is higher than your guess.")
            else:
                bot_message(f"Congratulations! You guessed the correct number: {random_number} in {attempts} Attempt(s).\n")
                return attempts
        
        except ValueError as error:
            bot_message(f"{error}")
            print(f"\nPlease only enter integer numbers between {lower_limit} and {upper_limit}.")


if __name__ == "__main__":
    LOWER_LIMIT : Final[int] = 1
    UPPER_LIMIT : Final[int] = 100
    guess_the_number_game(lower_limit=LOWER_LIMIT, upper_limit=UPPER_LIMIT)

# Good work!