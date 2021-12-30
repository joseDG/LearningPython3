
def f(x):
    if x < 0:
        raise ValueError(f'{x} is negative value')
    print(x / 2)


if __name__ == '__main__':
    f(-10)

"""
  File "02.py", line 9, in <module>
    f(-10)
  File "02.py", line 4, in f
    raise ValueError(f'{x} is negative value')
ValueError: -10 is negative value
"""

