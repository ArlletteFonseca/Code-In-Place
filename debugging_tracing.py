"""
Part A:
It will print n =42
"""

"""
Part B:
Edit this code so that it works correctly
"""


def divide_and_round(n):
    """
    Divides an integer n by 2 and rounds
    up to the nearest whole number
    """
    if n % 2 == 0:
        n = n / 2
        # this part of the statement is not returning n back to main so I added return statement
        return n
    else:
        n = (n + 1) / 2
        # this part of the statement is not returning n back to main so I added return statement
        return n


def main():
    n = 42
    divide_and_round(n)
    # the print statement below is now printing the result of divide_and_round(n), before it was just n, now it will be 21.0
    print(divide_and_round(n))


if __name__ == "__main__":
    main()
