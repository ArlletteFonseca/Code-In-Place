from karel.stanfordkarel import *

"""
File: CleanupKarel.py
--------------------
When you finish writing this file, CleanupKarel should be able to
pick up all beepers from the first row of any sized world and
end in the bottom right corner facing East.
"""


def main():
    """
    Karel moves foward to check for beepers and picks them up only if his front is clear.
    """
    while front_is_clear():
        move()
        check_beepers()


def check_beepers():
    if beepers_present():
       pick_beeper()


if __name__ == '__main__':
    run_karel_program('Cleanup2.w')
