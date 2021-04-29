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
    """
    karel goes accross the board horizontally and vertically until achieving to put columns
    on the needed avenues.
    """

    while front_is_clear():
        face_up()
        check_beepers()
        move_vertically()
        face_down()
        move_vertically()
        face_up()
        move_horizontally()
    if right_is_blocked():
        face_up()
        check_beepers()
        move_vertically()
        face_down()
        move_vertically()
        face_up()


def move_vertically():
    while front_is_clear():
        move()
        check_beepers()


def face_down():
    turn_left()
    turn_left()


def move_horizontally():
    for i in range(4):
        move()


def face_up():
    turn_left()


def check_beepers():
    if no_beepers_present():
        put_beeper()


if __name__ == '__main__':
    run_karel_program('SampleQuad1.w')
