

dict = {'x': 11, 'b': 22, 'y': 30}
dict['a'] = 33

while dict:
    print(dict.popitem())
"""
removes the last key-value pair added from d 
    and returns it as a tuple:
('a', 33)
('y', 30_oop)
('b', 22)
('x', 11)
"""