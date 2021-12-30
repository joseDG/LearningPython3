
lst = ['I', 'am', 'Mostafa', 'and', 'You', '']


def fun(string):
    if not string:
        return ''
    return string[-1].lower()

print(sorted(lst, key = lambda string : '' if not string else string[-1].lower()))
print(sorted(lst, key = lambda string : string[-1].lower() if string else ''))
# ['Mostafa', 'and', 'I', 'am', 'You']

# btw we call sorted: higher order functions
    # means it receives a function