"""
Nimm is an ancient game of strategy that is named after the old German word for "take." It is also called Tiouk Tiouk in West Africa and Tsynshidzi in China. Players alternate taking stones until there are zero left.

The game of Nimm goes as follows:

The game starts with a pile of 20 stones between the players.

The two players alternate turns.

On a given turn, a player may take either 1 or 2 stone from the center pile.

The two players continue until the center pile has run out of stones.

The last player to take a stone loses. Here's a sample execution:
"""

import random


def main():
    stones = 20
    turn = 1
    player1 = " "
    player2 = " "
#is number input 1 or 2

    def invalid(num):
        if(num == 2 or num == 1):
            return "true"
        else:
            return "false"
# checks to see if stones is over 0
    while stones > 0:
        amount = 0
        print("There are " + str(stones)+" stones "+"left")
        if(turn % 2) == 0:
            # checks to see if turn is an odd or even number starts as odd 1 so player 1 goes
            amount = int(
                input("Player 2 would you like to remove 1 or 2 stones? "))
            while invalid(amount) == "false":
                amount = int(input("Please enter 1 or 2: "))
            print("")
            stones -= amount
            turn += 1
            player2 = "last"
            player1 = "first"
        else:
            amount = int(
                input("Player 1 would you like to remove 1 or 2 stones? "))
            while invalid(amount) == "false":
                amount = int(input("Please enter 1 or 2: "))
            print("")
            stones -= amount
            turn += 1
            #below keeps track of whose gone first and last so I can declare winner
            player1 = "last"
            player2 = "first"

    if (player1 == "last"):
        print("Player 2 wins!")
    else:
        print("Player 1 wins!")


if __name__ == '__main__':
    main()

