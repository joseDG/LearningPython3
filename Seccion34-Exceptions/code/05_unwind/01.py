

def f4(path, idx):
    file = open(path, 'r')
    idx = int(idx)
    lst = file.read().splitlines()
    res = lst[idx]
    file.close()
    return res

def f3(path, idx):
    try:
        return f4(path, idx)
    except FileNotFoundError:
        print('F3 caught FileNotFoundError')
        return -3

def f2(path, idx):
    try:
        return f3(path, idx)
    except ValueError:
        print('F2 caught ValueError')
        return -2

def f1(path, idx):
    try:
        return f2(path, idx)
    except IndexError as e:
        print('F1 caught IndexError')
        print('Log and raise again')
        raise e


if __name__ == '__main__':
    path, idx = input().split()
    print(f1(path, idx))
    print('Bye')