from math import log
import math
import random

def guess(x):
    random_number = random.randint(1,x)

    usersGuess = 0

    max_guesses = math.floor(log(x, 2)) + 2

    numUserGuesses = 0
    while usersGuess!=random_number and numUserGuesses < max_guesses:
        print(f"You have {max_guesses-numUserGuesses} guesses remaining")
        usersGuess = int(input("Guess the number between 1 and %s: " % x))
        if usersGuess < random_number:
            print("Too low!")
        elif usersGuess > random_number:
            print("Too high!")
        numUserGuesses += 1
    
    print("Spot on!")
    print(f"You did it in {numUserGuesses} tries")
    
guess(10)