SAMPLE_LIST = ['a', 'b', 'c', 'd', 'e']
MAX_LENGTH = 3
LENGTH = len(SAMPLE_LIST)


def shorten(lst, max_len):
    if LENGTH > MAX_LENGTH:
        for i in range(MAX_LENGTH, LENGTH):
            print(SAMPLE_LIST.pop())
    else:
        print(SAMPLE_LIST)


def main():
    shorten(SAMPLE_LIST, MAX_LENGTH)


if __name__ == "__main__":
    main()
