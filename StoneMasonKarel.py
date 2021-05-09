from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should be
able to solve the "repair the quad" problem from Assignment 1.
You should make sure that your program works for all of the
sample worlds supplied in the starter folder.
"""

def main():
    while front_is_clear():
        build_pylon()
        next_pylon()


def build_pylon():
    turn_left()
    while front_is_clear():
        check_beeper()
        move()
    turn_around()
    while front_is_clear():
        move()
    turn_left()


def next_pylon():
    for x in range(4):
        move()


def turn_around():
    check_beeper()
    for x in range(2):
        turn_left()


def check_beeper():
    if no_beepers_present():
        put_beeper()


if __name__ == '__main__':
    run_karel_program('21x21.w')
