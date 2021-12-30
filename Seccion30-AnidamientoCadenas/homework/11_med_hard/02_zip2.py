class OurZip:
    # receive varying numbers of of iterables: assume only list, tuple, string
    def __init__(self, *iterables):
        self.iterables = iterables
        self.cur_col_idx = 0

    def has_next(self):
        # if there is at least one: use it
        for seq in self.iterables:
            if self.cur_col_idx < len(seq):
                return True
        return False

    def get_next(self):
        ret = [0] * len(self.iterables)

        for idx, seq in enumerate(self.iterables):
            if self.cur_col_idx < len(self.iterables[idx]):
                ret[idx] = self.iterables[idx][self.cur_col_idx]
            else:
                ret[idx] = None
        self.cur_col_idx += 1

        return tuple(ret)



if __name__ == '__main__':

    z = OurZip(list(range(10, 15)),
               list(range(10)), 'Mostafa')
    while z.has_next():
        print(z.get_next())
"""
(10, 0, 'M')
(11, 1, 'o')
(12, 2, 's')
(13, 3, 't')
(14, 4, 'a')
(None, 5, 'f')
(None, 6, 'a')
(None, 7, None)
(None, 8, None)
(None, 9, None)
"""