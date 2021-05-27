SAMPLE_ROSTER = ['miranda', 'karel', 'shrek', 'donkey']


def find_karel(roster):
    """
    Prints whether or not Karel is in the roster.
    >>> find_karel(['chris', 'mehran'])
    Karel isn't here.
    >>> find_karel(['karel', 'is', 'here'])
    Karel is here!
    """

    LENGTH = len(SAMPLE_ROSTER)
    COUNT = 0
    for i in range(0, LENGTH):

        if roster[i] == 'karel':
            COUNT = 1
    if COUNT > 0:
        print("Karel is here!")
    else:
        print("Karel isn't here")


def main():
    # delete the pass statement below and write your code here!
    find_karel(SAMPLE_ROSTER)


if __name__ == "__main__":
    main()
