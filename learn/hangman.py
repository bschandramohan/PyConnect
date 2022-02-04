import random

print("Hangman game")
total_lives = 9

word_list = ["amazing", "harry", "movie", "showdown"]

word_chosen = random.choice(word_list)


def print_character_list(list):
    str = ""
    for index in range(len(list)):
        str += list[index] + " "
    print(str + "\n")


# print word with underlines
word_underline = []
for i in range(0, len(word_chosen)):
    word_underline += "_"

correct_guesses_count = 0
correct_characters = []
guessed_characters = []

# using while loop instead of for since we can't change index (for continue cases below) in for
guesses_index = 0
while guesses_index < total_lives:
    print_character_list(word_underline)
    character = input(f"{guesses_index}: Guess the character: ").lower()
    if len(character) > 1:
        print("Invalid entry")
        continue

    if not character.isalnum():
        print("Not alpha numeric character")
        continue

    if guessed_characters.count(character) > 0:
        print("You already guessed the character. Try something else")
        continue

    guessed_characters += character

    present_count = word_chosen.count(character)
    if present_count > 0:
        print("Good guess")
        correct_guesses_count += present_count
        correct_characters += character
        for position in range(len(word_chosen)):
            if word_chosen[position].lower() == character.lower():
                word_underline[position] = character

        if correct_guesses_count == len(word_chosen):
            print("Correctly guessed the word")
            break
    else:
        guesses_index += 1
        print("Sorry! Not present")

print(f"\nWord chosen was {word_chosen}\n"
      f"You guessed correctly {correct_guesses_count} character(s) in the word.\n"
      f"Characters guessed correctly were {correct_characters}\n")
