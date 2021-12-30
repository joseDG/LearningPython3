

memory = None

def fib(n):
    if n <= 1:
        return 1

    global memory
    if memory is None:  # first call
        memory = [-1] * (n+1)   # create n+1 list entries, intialize to -1

    if memory[n] != -1:
        return memory[n]        # computed already. Just return it

    memory[n] = fib(n-1) + fib(n-2)
    return memory[n]    # we can merge these 2 lines



if __name__ == '__main__':
    memory = None
    print(fib(6))

    memory = None
    print(fib(35))  # 14930352

    memory = None
    print(fib(50))  # 20365011074

    memory = None
    print(fib(800))  # 225591516161936330872512695036072072046011324913758190588638866418474627738686883405015987052796968498626
