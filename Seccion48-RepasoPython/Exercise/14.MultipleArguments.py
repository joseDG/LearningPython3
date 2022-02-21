
def foo(*args):
    double_list = [x*2 for x in args]
    return double_list

print(foo(1,3,5))

#example 2
def foo(*args):
    return list(args)

#Example 3
def foo(**kwargs):
    return kwargs

print(foo(a=1,c=5,d=109))

#example 5
def foo(*args):
    lst = []
    for eachlist in args:
        lst = lst + eachlist
    return lst

#example 6
def foo(*args):
    return all(args)

#example 7
def foo():
    return "Hello"

def hofoo():
    return foo

#example7
# Function gets a list, converts it to tuple, returns the tuple
def list_to_tuple(lst):
    return tuple(lst)

# Function gets any Python objects, converts it into a string, returns the string
def object_to_string(object):
    return str(object)

#example8
def foo(number):
    return dict(sign = "positive" if number > 0 else
        ("negative" if number < 0 else "zero"),
        parity = "odd" if number % 2 == 1 else 
        ("even" if number % 2 == 0 else "non integer"))

#example9
def foo(mylist):
    if len(mylist) > 0:
        return mylist[-1]
    else:
        return "Empty List"

#example 10
def foo(mylist):
    return mylist[1:-1]

#example 11
def foo(lst, item):
    if len(lst) == 3:
        lst.pop(0)
        lst.append(item)
        return lst

#example 12

def foo(mylist):
    return mylist[::7]

foo(['mom','tue','wed','thu','fri','sat','sun','mom','tue','wed','thu','fri','sat','sun','mom','tue','wed','thu','fri','sat','sun'])

#example 14
import itertools

def foo(mylist):
    list_of_lists = [mylist[i:i+5] for i in range(0, len(mylist),7)]
    return list(itertools.chain.from_iterable(list_of_lists))

foo(['mom','tue','wed','thu','fri','sat','sun','mom','tue','wed','thu','fri','sat','sun','mom','tue','wed','thu','fri','sat','sun'])

#example 15
import itertools

def foo(mylist, x, y):
    list_of_lists = [mylist[i:i+x] for i in range(0, len(mylist),y)]
    return list(itertools.chain.from_iterable(list_of_lists))

#example 16
def foo(mystring):
    if "xxx" in mystring:
        return True
    else:
        return False

#example 17
def foo(mylist):
    return [string for string in mylist if isinstance(string, str) and "xxx" in string ]