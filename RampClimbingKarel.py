from karel.stanfordkarel import *

"""
File: RampClimbingKarel.py
--------------------
When you finish writing this file, RampClimbingKarel should be
able to draw a line with slope 1/2 in any odd sized world
"""


def main():
    """
    Karel is going to go up 1/2 slope as long as there is space in front. leaving a beeper at every
    1/2 step up. There is a move_foward function too allow the same movement foward. There is
    also a turn_right function allowing karel to move east after everytime he moves up.
    """
    put_beeper()
    while front_is_clear():
        move_foward()
        turn_right()


def move_foward():
    move()
    move()
    turn_left()
    move()
    put_beeper()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


if __name__ == '__main__':
    run_karel_program('RampKarel3.w')
