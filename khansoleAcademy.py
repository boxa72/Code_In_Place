"""
Prints out a randomly generated addition problem
and checks if the user answers correctly.
"""

import random 

MIN_RANDOM = 10     # smallest random number to be generated
MAX_RANDOM = 99     # largest random number to be generated
THREE_CORRECT = 3   # constant for the loop

def main():
    math_test()

def math_test():
    """ function that holds the whole game """
    num_correct = 0


    while num_correct != THREE_CORRECT:
        num1 = random.randint(MIN_RANDOM, MAX_RANDOM)
        num2 = random.randint(MIN_RANDOM, MAX_RANDOM)
    

        print("What is " + str(num1) + ' + ' + str(num2) + '? ')
        user_input = int(input())
        print("Your answer: " + str(user_input))
        correct_answer = num1 + num2

        if user_input == correct_answer:
            num_correct += 1
            if num_correct == 1:
                print("Correct! You've gotten " + str(num_correct) + " correct in a row.")
            elif num_correct == 2:
                print("Correct! You've gotten " + str(num_correct) + " correct in a row.")
            elif num_correct == 3:
                print("Correct! You've gotten " + str(num_correct) + " correct in a row.")
                print("Congratulations! You mastered addition.")   
        else:
            print("Incorrect. The expected answer is " + str(correct_answer))
            num_correct = 0

    
if __name__ == '__main__':
    main()