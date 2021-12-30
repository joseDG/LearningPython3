
def read_int(msg):
    age = input(msg)  # 'Hey'
    age = int(age)
    return age


age = read_int('Enter age: ')
print(age)    # not reachable if RTE before it

"""
Traceback (most recent call last):
  File "01.py", line 4, in <module>
    age = int(age)
ValueError: invalid literal for int() with base 10: 'Hey'
"""


