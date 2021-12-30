class MyRange:
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step
        self.idx = 0

    def has_next(self):
        if self.step > 0:
            return self.start < self.end
        return self.start > self.end

    def get_next(self):
        ret = self.idx, self.start
        self.start += self.step
        self.idx += 1

        return ret


rng = MyRange(10, 5, -1)

while rng.has_next():
    print(rng.get_next())
