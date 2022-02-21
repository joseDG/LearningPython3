def foo(lst, obj):
    if obj not in lst:
        lst.append(obj)
    return lst

foo('hola', foo)