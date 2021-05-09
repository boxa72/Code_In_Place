"""
Number Guesser Program

This is an example of how to use variables to 
keep track of information in a program that 
also makes use of loops
"""

from random import randint

LOWER_NUM = 0
HIGHER_NUM = 100

def main():
    num_guesses = 0
    lower_bound = LOWER_NUM
    upper_bound = HIGHER_NUM
    
    guess = randint(lower_bound, upper_bound)

    while True:
        
        
        user_input = input("Is your number " + str(guess) + "? ")
        num_guesses += 1


        if user_input == "lower":
            upper_bound = guess - 1
        elif user_input == "higher":
            lower_bound = guess + 1
        else:
            print("I win! It took me " + str(num_guesses) + " guesses")
            break

        guess = (lower_bound + upper_bound) // 2
if __name__ == "__main__":
    main()