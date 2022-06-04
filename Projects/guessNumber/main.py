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
    
# guess(10)

def computerGuessRandom():
    random_number = int(input("Please choose a number that is more than 1 and less than 100 for the computer to guess: "))

    guess = 0
    max_int = 100
    count = 0
    while guess!=random_number:
        guess = random.randint(1,100)
        print(f"The computer guessed {guess}")
        count += 1
    print(f"The computer succeded in {count} guesses")

def computerGuessFaster():
    random_number = int(input("Please choose a number that is more than 1 and less than 100 for the computer to guess: "))

    guess = 0
    max_int = 100
    min_int = 1
    count = 0
    while guess!=random_number:
        guess = random.randint(min_int,max_int)
        print(f"The computer guessed {guess}")
        if(guess < random_number):
            min_int = guess
        elif(guess > random_number):
            max_int = guess
        count += 1
    print(f"The computer succeded in {count} guesses")

def computerGuessBinary():
    random_number = int(input("Please choose a number that is more than 1 and less than 100 for the computer to guess: "))
    guess = 0
    max_int = 100
    min_int = 1
    count = 0

    while guess!=random_number:
        guess = math.floor((max_int+min_int)/2)
        print(f"The computer guessed {guess}")
        if(random_number > guess):
            min_int = guess
        elif(random_number < guess):
            max_int = guess
        count += 1
    print(f"The computer succeded in {count} guesses")

computerGuessBinary()