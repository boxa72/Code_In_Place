"""
Prints out 10 random numbers between 0 and 100.
"""

NUM_RANDOM = 10
MIN_RANDOM = 0
MAX_RANDOM = 100

import random

def main():
    for x in range(NUM_RANDOM):
        print(random.randint(MIN_RANDOM, MAX_RANDOM))

if __name__ == '__main__':
    main()