
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
words = ["mostafa", 'saad', 'ibrahim']

for tuple_item in zip(numbers, words, letters):
    print(tuple_item)

"""
(1, 'mostafa', 'a')
(2, 'saad', 'b')
(3, 'ibrahim', 'c')
"""

for number, word, letter in zip(numbers, words, letters):
    print(number, word, letter)
"""
1 mostafa a
2 saad b
3 ibrahim c
"""