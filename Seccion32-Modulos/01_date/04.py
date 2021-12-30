
def hello(lst = []):
    lst.append(1)
    print(lst)

hello() # [1]
hello() # [1, 1]
hello() # [1, 1, 1]
