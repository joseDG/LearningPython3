
if __name__ == '__main__':
    n = int(input())
    dct = {}
    # Generate all prefixes and put in a dict
    while n:
        line = input()
        for idx in range(len(line)):
            substr = line[:idx +1]
            dct.setdefault(substr, [])
            dct[substr].append(line)
        n -= 1

    q = int(input())
    while q:
        line = input()
        if line not in dct:
            print('Not found')
        else:
            print(f'{line} matches {dct[line]}')
        q -= 1