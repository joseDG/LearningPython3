

# How to create an 3x4 grid of some value (e.g. 0)?

rows, cols = 3, 4
lst = [[0] * rows] * cols
print(lst)
# [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

lst[0][0] = 2
print(lst)
# [[2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0]]  hmmm
print(id(lst[0]), id(lst[1]))   # 0x111 0x111
# * cols just append the same object

lst = [ [0] * rows for i in range(cols) ]
lst[0][0] = 2
print(lst)
# [[2, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

lst = [[x for x in range(rows)] for y in range(cols)]
print(lst)
# [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]

# Useful: https://blog.finxter.com/python-list-of-lists
# https://nedbatchelder.com/blog/201308/names_and_values_making_a_game_board.html

