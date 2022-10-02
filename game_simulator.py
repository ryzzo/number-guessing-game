"""A program to solve the number guessing game using binary search algorithm"""
import number_guessing_game as ngg

# generated number
guessed_number = ngg.numberGenerator()
print("Number guessed: ", guessed_number)

low = 0
high = 1000


while True:
    user_guess = (high + low)//2
    result = ngg.compareInput(guessed_number, user_guess)
    
    if result == "larger":
        high = user_guess
        print(user_guess)

    elif result == "smaller":
        low = user_guess
        print(user_guess)
        
    else:
        print(user_guess)

        break
    
