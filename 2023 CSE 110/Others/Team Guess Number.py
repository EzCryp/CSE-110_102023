import random

magic_number = random.randint(1, 50)

# I need to start the variable "guess" at something, but I don't want to start it as
# valid number that the computer may have chosen, so I'll start with -1
guess = -1

# Keep going as long as the guess doesn't match the magic number

while guess != magic_number:
    guess = int(input("What is your guess? "))

    if guess < magic_number:
        print("Higher")
    elif guess > magic_number:
        print("Lower")
    else:
        print("You guessed it!")

# do the stretch challenge

# trial = input("Would you like to try again? ")
#     if trial == "yes":
#         guess = int(input("What is your guess? "))
#     elif trial == "no":
#         print("Thank you for playing!")