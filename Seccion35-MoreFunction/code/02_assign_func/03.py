

lst = ['I', 'am', 'Mostafa', 'and', 'You']
print(sorted(lst))                      # ['I', 'Mostafa', 'You', 'am', 'and']

# key: will be used to compare elements
print(sorted(lst, key = str.lower))     # ['am', 'and', 'I', 'Mostafa', 'You']

print(sorted(lst, key = len))           # ['I', 'am', 'and', 'You', 'Mostafa']

def fun(string):
    if not string:
        return ''
    return string[-1].lower()

print(sorted(lst, key = fun))           # ['Mostafa', 'and', 'I', 'am', 'You']

n = len(max(lst, key=len))  # 7 = length of longest string in list!

def get_key(id):
    if id == 1:
        return str.lower
    return len

