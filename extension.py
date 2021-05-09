"""
    I remember writing this program not long ago in C++ but I've never
    written it in Python before. This is the Hailstone sequence.
"""

from math import trunc

def main():
    count = 0
    number = int(input("Enter a number: "))
    while number > 1:
        if number % 2 == 0:
            print(str(number) + " is even, so I take half: " + str(int(number / 2)))
            number = number // 2
        else:
            print(str(number) + " is odd, so I make 3n + 1: " + str(int(3 * number + 1)))
            number = 3 * number + 1
        count += 1
    print("The process took " + str(count) + " steps to reach 1")
if __name__ == "__main__":
    main()