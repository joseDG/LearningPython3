def foo(s1, s2):
    return s1 + s2

def area(a=4, b=3):
    return a * b

print(area(5, 7))

#Funciones con argumetnos
def media(*args):
    return sum(args) / len(args)

print(media(1, x=3.4))

#fucion
def foo(*args):
    return sum(args) / len(args)

#funciones 
def foo(*args):
    args = [x.upper() for x in args]
    return sorted(args)

#fujcniones varios arguemntos
# def mean(***kwargs):
#     return kwargs 

print(mean(a=1, b=2, c=3))

#ejercios
def find_sum(**kwargs):
    return sum(kwargs.values())
    
print(find_sum(x=1, y=2, z=6))

