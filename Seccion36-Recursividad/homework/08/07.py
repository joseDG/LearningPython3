
def do_something1(n):
    if n:
        print(n%10, end='')
        do_something1(n//10)


def do_something2(n):
    if n:
        do_something2(n//10)
        print(n % 10, end='')


if __name__ == '__main__':
    do_something1(12345)
    print()
    do_something2(12345)
    do_something2(0)

"""
do_something1 prints the number backward, but do_something2 prints it in normal order

Both functions don't handle the zero
"""