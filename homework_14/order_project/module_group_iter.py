class GroupIter:

    def __init__(self, students):
        self.students = students
        self.index = 0
    def __next__(self):
        if self.index < len(self.students):
            self.index += 1
            return self.students[self.index - 1]
        raise StopIteration
