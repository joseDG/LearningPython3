class MyRange:
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step

    # we will assume user will be nice won't do illegal get_next

    def has_next(self):
        return self.start < self.end

    def get_next(self):
        ret = self.start
        self.start += self.step
        return ret


rng = MyRange(5, 10, 1)

while rng.has_next():
    print(rng.get_next(), end=" ")  # 5 6 7 8 9
print()

rng = MyRange(5, 10, 2)
while rng.has_next():
    print(rng.get_next(), end=" ")  # 5 7 9
