from karel.stanfordkarel import *

"""
File: Midpoint.py
------------------------
Place a beeper in the middle of the first row.
"""


def main():
    """
    Karel fills bottom row with beepers and then he goes back and forth picking up beepers
    from the ends of the row. Once there are no beepers places one beeper in the middle.
    """

    fill_with_beepers()
    check_beepers()
    put_beeper()


def turn_around():
    turn_left()
    turn_left()


def fill_with_beepers():
       while front_is_clear():
            move()
            put_beeper()
        turn_around()


def check_beepers():
       while beepers_present():
            if front_is_clear():
                pick_beeper()
                move()
                while beepers_present():
                    move()
            turn_around()
            if front_is_clear():
                move()


if __name__ == '__main__':
    run_karel_program('Midpoint8.w')
