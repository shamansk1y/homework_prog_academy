class UserSequence:
    def __init__(self, order):
        self.order = order

    def __getitem__(self, item):
        if isinstance(item, int):
            if item < len(self.order):
                return self.order[item]
            else:
                raise IndexError
        if isinstance(item, slice):
            res = []
            start = item.start or 0
            stop = item.stop or len(self.order)
            step = item.step or 1
            for i in range(start, stop, step):
                res.append(self.order[i])
            return res
        raise TypeError
