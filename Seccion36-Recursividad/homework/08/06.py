


def startswith(main, pattern):
    if not pattern:
        return True

    if not main:
        return False

    if main[0] != pattern[0]:
        return False

    return startswith(main[1:], pattern[1:])


if __name__ == '__main__':
    print(startswith("abcdefg", ""))        # True
    print(startswith("abcdefg", "abcd"))    # True
    print(startswith("abcdefg", "ax"))      # False
    print(startswith("abcd", "abcdefg"))    # False
    print(startswith("abcd", "abcd"))       # True
    print(startswith("", ""))               # True