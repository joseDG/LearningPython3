


def is_palindrom(lst):
    if len(lst) <= 1:
        return True

    if lst[0] != lst[-1]:
        return False

    return is_palindrom(lst[1:-1])




if __name__ == '__main__':
    lst = [1, 3, 5, 7, 4, 2]

    print(is_palindrom([]))                     # True
    print(is_palindrom([5]))                    # True
    print(is_palindrom([5, 7]))                 # False
    print(is_palindrom([5, 5]))                 # True
    print(is_palindrom([1, 2, 3, 2, 1]))        # True
    print(is_palindrom([1, 2, 3, 3, 2, 1]))     # True
    print(is_palindrom([1, 2, 3, 4, 2, 1]))     # False

    