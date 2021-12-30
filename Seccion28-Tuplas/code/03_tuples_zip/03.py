
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
words = ["mostafa", 'saad', 'ibrahim']

for idx, tuple_item in enumerate(zip(numbers, words, letters)):
    print(idx, tuple_item)

"""
0 (1, 'mostafa', 'a')
1 (2, 'saad', 'b')
2 (3, 'ibrahim', 'c')
"""

for idx, (number, word, letter) in enumerate(zip(numbers, words, letters)):
    print(idx, number, word, letter)
"""
0 1 mostafa a
1 2 saad b
2 3 ibrahim c
"""