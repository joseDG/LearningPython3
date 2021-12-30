


sq = lambda x : x * x

def ff1(st, en, step):
    def inner(f):
        return [f(val) for val in range(st, en, step)]

    return inner



processor = ff1(2, 6, 1)
print(processor(sq))

ff2 = lambda st, en, step: lambda f: [f(val) for val in range(st, en, step)]
processor = ff2(5, 1, -1)
print(processor(sq))

