from karel.stanfordkarel import *



def main():
    """
    Karel checks to see if there is a beeper, if there isn't he places a beeper, if there is
    a beeper he leaves it alone
    """
    check_beepers()

def check_beepers():
    if beepers_present():
        pick_beeper()

if __name__ == '__main__':
    run_karel_program('SafePickup2.w')
