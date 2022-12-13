class InvalidGroupListError(Exception):
    """Raised when a self.__students list is full"""
    def __init__(self, max_limit):
        self.max_limit = max_limit

    def __str__(self):
        return f'Group full, limit {self.max_limit} students.'

