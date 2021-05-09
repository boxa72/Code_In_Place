""" Program that simulates the game of Nimm """

import random

def main():
    stones = 20
    player = 1

    while stones > 0:
        print("There are " + str(stones) + " stones left")
        num_stones = int(input("Player " + str(player) + " would you like to remove 1 or 2 stones? "))
        while num_stones < 1 or num_stones > 2:
            num_stones = int(input("Please enter 1 or 2: "))

        if player == 1:
            player = 2
        else:
            player = 1
   
       
        stones -= num_stones
        print()

    if stones == 0:
        if player == 2:
            print("Player 2 wins!")
        else:
            print("Player 1 wins!")

if __name__ == '__main__':
    main()