# Moustapha Bah 9/15/2025
# Lab 4 Hangman Game
import random


random_number = random.randint(1, 15)
wrong_guesses = 0
hangwman_list = [

""" 
|---  
   |
   |
   |
    
""",
""" 
|---  
O  |
   |
   |
""",
"""
|---
O  |
|  |
   |
""",
"""
|---
O  |
|  |
|  |
""",

""" 
  |---
  O  |
 \|  |
  |  |      
""",

""" 
  |---
  O  |
 \|/ |
  |  |
""",

""" 
  |---
  O  |
 \|/ |
  |  |
 /
""",

""" 
  |---
  O  |
 \|/ |
  |  |
 / \\
"""

]





print(hangwman_list[wrong_guesses])   
print("Hello! Today we're going to play Hangman!") 
print('You have 7 tries to try and guess a randomly generated number between 1 and 15. Start the game!!')

while True:
    
    user_guess = int(input("Guess a number between 1 and 15: "))
    # Have user guess a number between 1 and 15
    if user_guess < 1 or user_guess > 15:
        print("Please guess a number within the range.")
        continue
    # Check if the guess is within the range
    if user_guess == random_number:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Incorrect guess. Try again.")
        wrong_guesses += + 1
        print(hangwman_list[wrong_guesses])  # Display hangman state
        # 7 guesses allowed
        print(f"You have {7 - wrong_guesses} guesses left.")
        if wrong_guesses >= 7:
            print(f"Sorry, you've exceeded the maximum number of guesses. The correct number was {random_number}.")
            break

