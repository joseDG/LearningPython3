


def list_increment(lst, position = 0):
    if len(lst) == position:
        return

    lst[position] += len(lst) - position
    list_increment(lst, position + 1)




if __name__ == '__main__':
    lst = [1, 8, 2, 10, 3]
    list_increment(lst)

    print(lst)  # [6, 12, 5, 12, 4]