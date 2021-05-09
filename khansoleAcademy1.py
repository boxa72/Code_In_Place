"""
Prints out a randomly generated addition problem
and checks if the user answers correctly.
"""

import random 

MIN_RANDOM = 10     # smallest random number
MAX_RANDOM = 99     # largest random number

def main():
    num1 = random.randint(MIN_RANDOM, MAX_RANDOM)
    num2 = random.randint(MIN_RANDOM, MAX_RANDOM)
    
    print("What is " + str(num1) + ' + ' + str(num2) + '? ')
    user_input = int(input())
    print("Your answer: " + str(user_input))
    correct_answer = num1 + num2

    if user_input == correct_answer:
        print("Correct!")
    else:
        print("Incorrect. The expected answer is " + str(correct_answer))

    

if __name__ == '__main__':
    main()