from learn.logo import logo_guess_the_number

import random
import os
clear = lambda: os.system('clear')

# Currently throws an error : TERM environment variable not set. INVESTIGATE
# clear()

def play_game(): 
    print(logo_guess_the_number)
    TOTAL_CHANCES = 6
    current_guesses = 0

    chosen_number = random.randint(1, 100)

    while (current_guesses < TOTAL_CHANCES):    
        number_guessed = int(input("Guess the number from 1 to 100\n"))
        current_guesses += 1

        if number_guessed == chosen_number:
            print(f"You correctly guessed the number {chosen_number} in {current_guesses} attempt")
            break
        elif number_guessed < chosen_number:
            print(f"The number you guessed is lower than the chosen number. Current guesses={current_guesses}")
            
        else:
            print(f"The number you guessed is greater than the chosen number. Current guesses={current_guesses}")

    if not number_guessed == chosen_number:
        print(f"Sorry, you didn't guess the correct number: {chosen_number}")
    

play_game()
continue_game = True
while continue_game:
    if input("Enter y to play the game again\n") == "y":
        play_game()
    else:
        continue_game = False

