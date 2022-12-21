
class OrderIter:

    def __init__(self, order):
        self.order = order
        self.index = 0

    def __next__(self):
        if self.index < len(self.order):
            self.index += 1
            return self.order[self.index - 1]
        raise StopIteration

    def __iter__(self):
        return self
