
# If u know smarter ways to do this code, GIVEN what is taught in the course so far, share with me
# In practice, we may implement it in more safer way (e.g current TypeError/ValueError) below are a bit risky

# instead of using None as default, which make it hard for others, we define our temp class
class _DefaultMarker:
    pass

__special_default_object = _DefaultMarker() # internal dummy special object

def _my_max(*iterable, key = None):
    first, *iterable = iterable

    if not iterable:
        return first    # if no more elements, let's return it

    remain = _my_max(*iterable)

    if key is None:
        return first if first > remain else remain

    first_key, remain_key = key(first), key(remain)

    return first if first_key > remain_key else remain


def my_max(*iterable, default = __special_default_object, key = None):
    # This function will try to handle the different errors
    # If no errors, it will call the actual maximization
    try:
        # Make sure at least 1 element
        first, *sub_iterable = iterable
    except:
        raise TypeError('max expected 1 argument, got 0') from None
        # without from None: you see 2 exceptions: original one (ValueError) and our TypeError

    if not sub_iterable:    # just single item: either iterable or not. If iterable, it might be empty, e.g. []
        try:
            # Let's try to unpack it
            return _my_max(*first)
        except TypeError:
            raise TypeError(f"'{type(first).__name__}' object is not iterable") from None
            # The step (*first) will fail as * expects first to be iterable. Input e.g. 15
        except ValueError:
            if default is not __special_default_object:
                return default
            raise ValueError('my_max() arg is an empty sequence') from None # Empty such as []
            # It will happen from the unpacking in _my_max: first, *iterable = iterable

    # # At least 2 items: let's call our max now
    return _my_max(*iterable, key = key)


if __name__ == '__main__':


    #my_max = max   # uncomment to test python max

    print(my_max(2, 5))                       # 5
    print(my_max([10, 3, 60, 20]))            # 60
    print(my_max(10, 3, 6, 20))               # 20
    print(my_max({5, 7, 1}))                  # 7
    print(my_max([5, 1], [4, 9]))             # [5, 1]
    print(my_max('1234'))                     # 4
    print(my_max('1234', '98'))               # 98
    print(my_max('1234', '98', key = len))    # 1234
    print(my_max([5, 1], [4, 9], key = sum))  # [4, 9]

    # Don't show any other internal exceptions
    #print(my_max())                # TypeError: max expected 1 argument, got 0
    #print(my_max(default = -1))    # TypeError: max expected 1 argument, got 0
    #print(my_max([]))              # ValueError: max() arg is an empty sequence
    print(my_max([], default = None)) # None
    #print(my_max(-15))    # TypeError: 'int' object is not iterable
    #print(my_max(3, [4])) # TypeError: '>' not supported between instances of 'list' and 'int'