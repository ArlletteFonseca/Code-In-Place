SAMPLE_LIST = [1, 2, 3, 4, 5, 6]


def count_even(lst):
    """
    Returns number of even numbers in list.
    >>> count_even([1,2,3,4])
    2
    >>> count_even([1,3,5,7])
    0
    """
    COUNT = 0
    LENGTH = len(SAMPLE_LIST)
    for i in range(0, LENGTH):
        if SAMPLE_LIST[i] % 2 == 0:
            COUNT = COUNT + 1
    print(COUNT)


def main():
    count_even(SAMPLE_LIST)


if __name__ == "__main__":
    main()

