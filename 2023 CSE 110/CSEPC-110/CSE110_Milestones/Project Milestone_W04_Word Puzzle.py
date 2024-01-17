""""
Author: Ezra Zacarias
Class : CSEPC 110_W04_Prove
Purpose: Create Project Milestone Word Puzzle game
"""
# 1. Have a secret word stored in the program.
# 2. Prompt the user for a guess.
# 3. Continue looping as long as that guess is not correct.
# 4. Calculate the number of guesses and display it at the end.
# 5. You do not need to have any hints at this point.

# What is your guess?
 # Your guess was not correct.
 # Congratulations! You guessed it!
 # It took you [3] guesses.

import random

# Provide the secret word in variable, with guess counter initial hint with underscores
secret_word = "work"
hint = "_" * len(secret_word)
guess_count = 0

# Print the welcome message
print("Welcome to the Word Guessing Game!")
print()

# Start a loop that continues until the guess is correct
while True:
    # Prompt the user for a guess
    guess = input("Guess the secret word: ").lower()

    # Check if the guess length is correct
    if len(guess) != len(secret_word):
        print("Your guess was not correct. The secret word has", len(secret_word), "letters.")
        continue

    guess_count += 1

    # Check if the guess is correct
    if guess == secret_word:
        print("Congratulations! You guessed the secret word:", secret_word)
        print("Number of guesses:", guess_count)
        break

    # Provide new hint based on the secret word
    new_hint = ""
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            new_hint += guess[i].upper()
        elif guess[i] in secret_word:
            new_hint += guess[i].lower()
        else:
            new_hint += "_"

    # Print additional hint 
    print("Hint:", new_hint)