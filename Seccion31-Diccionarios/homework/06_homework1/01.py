

if __name__ == '__main__':
    # Create a dict with requested mapping
    from_str = 'abcdefghijklmnopqrstuvwxyz0123456789'
    to_str = 'YZIMNESTODUAPWXHQFBRJKCGVL!@#$%^&*()'
    # create the dict with comprehension
    dict = {from_str[idx]:to_str[idx] for idx in range(len(from_str))}

    string = input()
    res = ''
    for char in string:
        if char in dict:
            char = dict[char]
        res += char
    print(res)
