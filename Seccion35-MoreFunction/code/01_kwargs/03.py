
def hello(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

hello(a="Mostafa", b=10, c=(1, 2, 5))

"""
a Mostafa
b 10
c (1, 2, 5)
"""
