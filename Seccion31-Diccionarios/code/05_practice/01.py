


if __name__ == '__main__':


    line = input()
    dict = {}
    for char in line:
        char = char.lower()
        dict.setdefault(char, 0)    # if not exist, put value 0
        dict[char] += 1

    for key in sorted(dict):
        print(f'Letter {key} repeated {dict[key]} times')