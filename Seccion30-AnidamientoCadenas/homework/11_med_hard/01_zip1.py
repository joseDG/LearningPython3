class OurZip:
    # receive varying numbers of of iterables: assume only list, tuple, string
    def __init__(self, *iterables):
        self.iterables = iterables
        self.cur_col_idx = 0

    def has_next(self):
        for seq in self.iterables:
            if self.cur_col_idx >= len(seq):
                return False
        return True

    def get_next(self):
        # append is slow. we know the target size
        ret = [0] * len(self.iterables)
        for idx, seq in enumerate(self.iterables):
            ret[idx] =  self.iterables[idx][self.cur_col_idx]
        self.cur_col_idx += 1

        return tuple(ret)

if __name__ == '__main__':
    z = OurZip(list(range(10, 15)), list(range(100)), 'Mostafa')
    while z.has_next():
        print(z.get_next())
"""
(10, 0, 'M')
(11, 1, 'o')
(12, 2, 's')
(13, 3, 't')
(14, 4, 'a')
"""