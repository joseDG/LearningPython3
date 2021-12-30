

def find_smallest(lst, target_type):
    new_lst = [item for item in lst if type(item) is target_type]

    if len(new_lst) == 0:
        return None

    return min(new_lst)


if __name__ == '__main__':
    lst = [10, -2.5, 20, 5, 'mostafa', 5.2, 'Ziad']

    print(find_smallest(lst, type(0)))      # 5
    print(find_smallest(lst, type(0.0)))    # -2.5
    print(find_smallest(lst, type('')))     # Ziad




