

# When you have multiple sequences and want to iterate
# such that in each iteration you have a single item
# from each sequence ==> you need zip

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']

# zip class constructor: def __init__(self, *iterables)
# it takes a group of iterables
# it then returns iterator that we can use to iterate

zipped = zip(numbers, letters)

print(list(zipped))
# [(1, 'a'), (2, 'b'), (3, 'c')]

words = ["mostafa", 'saad', 'ibrahim']
print(list(zip(numbers, letters, words)))
# [(1, 'a', 'mostafa'), (2, 'b', 'saad'), (3, 'c', 'ibrahim')]

# note: zip() in Python 3 is different than Python 2

