class DublicateStudentError(Exception):
    """Raised when a group_title already have this student"""
    def __init__(self, student, group_title):
        self.student = student
        self.group_title = group_title

    def __str__(self):
        return f'The {self.student} registered in group {self.group_title}.'
