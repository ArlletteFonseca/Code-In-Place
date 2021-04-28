from karel.stanfordkarel import *

"""
File: PuzzleKarel.py
--------------------
Karel should finish the puzzle by picking up the last beeper (puzzle piece) and placing it in the right spot.
Karel should end in the same position Karel starts in -- the bottom left corner of the world.
"""

def main():
    """
    Karel is going to move east 2 spaces, pick up a beeper and then move one more space to the east.
    then karel will  turn left  90 degrees and move north 2 spaces and place the beeper
    """
    pick_up_beeper()
    turn_north()
    place_beeper()
    face_south()
    face_west()
    move_home()

# Karel moves two spaces and picks up beeper
def pick_up_beeper():
    move()
    move()
    pick_beeper()
# Karel faces north
def turn_north():
    move()
    turn_left()
#Karel moves two spaces and places beeper
def place_beeper():
    move()
    move()
    put_beeper()
#Karel Faces south
def face_south():
    turn_left()
    turn_left()
#Karel Faces west
def face_west():
    move()
    turn_right()
# Karel goes back to where he started
def move_home():
    move()
    move()
    move()
    turn_left()
    move()
    turn_left()
#turns karel 90 degrees to the right
def turn_right():
    turn_left()
    turn_left()
    turn_left()




if __name__ == '__main__':
    run_karel_program('Puzzle.w')
