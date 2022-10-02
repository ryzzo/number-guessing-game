"""A number guessing game.  The program generates a number between 1 and 1000,
and the user asked is to guess the number"""

import random

def numberGenerator():
    """Generates a random number"""
    guessed_number = random.randint(0, 1000)
    return guessed_number

def userInput():
    """Gets input from the user"""
    try:
        user_guess =int(input("Guess the number (1 - 1000): "))
        if user_guess <= 0 or user_guess > 1000:
            raise 

    except:
        return "Invalid input"

    finally:
        return user_guess
    

def compareInput(program_guess, user_guess):
    """compare the program guess and the user input"""
    if program_guess == user_guess:
        return "correct"
    elif program_guess < user_guess:
        return "larger"
    else:
        return "smaller"
