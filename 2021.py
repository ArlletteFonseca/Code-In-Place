from karel.stanfordkarel import *

"""
File: 2021.py
--------------------
When you finish writing this file, Karel should be able to place 20 beepers,
then 21 beepers, and end facing East to the right of the 21 beepers.
"""

def main():
    """
    Karel moves foward and places  20 beepers using a for loop, Karel then moves foward one more
    space and uses a for loop to place another 21 beepers and finally Karel moves foward to an empty space.
    """
    #place 20 beepers
    for i in range(20):
        put_beeper()
    move()
    #place 21 beepers
    for x in range(21):
        put_beeper()
    move()

if __name__ == '__main__':
    run_karel_program('3x3.w')
