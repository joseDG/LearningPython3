
def sq1(x):
    return x * x

print(sq1(3))    # 9

sq2 = lambda x: x * x

print(sq2(3))    # 9

def name1(first, second):
    return f'{first} - {second}'

print(name1('mostafa', 'saad'))  # mostafa - saad

name2 =  lambda first, second: f'{first} - {second}'

print(name2('mostafa', 'saad'))  # mostafa - saad

print((lambda x, y: x * y)(2, 4))   # 8
