#!/usr/bin/env python
"""test.py, by Chris
This program is my first python test program
"""
import random
import gpiozero

def main():
    print "Guess a number between 1 and 100."
    randomNumber = random.randint(1,100)
    found = False   # flag variable to see if they guessed it
    while not found:
        userGuess = input("Your guess: ")
        if userGuess == randomNumber:
            print "Yay"
            acceptable = False
            while not acceptable:
                userInput = raw_input("Play again? (Yes/No):")
                if userInput == "Yes":
                    found = False
                    print "Guess a number between 1 and 100."
                    randomNumber = random.randint(1,100)
                    acceptable = True
                elif userInput == "No":
                    found = True
                    acceptable = True
                else:
                    print "Unacceptable input!  Yes or No"
        elif userGuess > randomNumber:
            print "Guess lower"
        else:
            print "Guess higher"


if __name__ == "__main__":
    main()
