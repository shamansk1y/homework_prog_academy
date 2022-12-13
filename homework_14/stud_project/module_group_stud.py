import logging
import module_ex_dublicate
import module_ex_group_limit
from module_student_stud import Student

logger = logging.getLogger('homework_13')
logger.setLevel(logging.INFO)

ch = logging.FileHandler("homework_13.log")
ch.setLevel(level=logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.info('A new student has been added to the list')

class Group():
    def __init__(self, title, max_students=10):
        """
        Create a new group
        :param title: Name of new group
        :param max_students: Maximum student in group
        """
        if not isinstance(max_students, int):
            raise TypeError()
        if max_students <= 0:
            raise ValueError()
        self.title = title
        self.__students = []
        self.max_students = max_students

    # add new student
    def stud_add(self, student: Student):
        """
        Function add a new student to the group
        :param student: use person from class Student
        :return: no return, only append
        """
        if student in self.__students:
            raise module_ex_dublicate.DublicateStudentError(student, self.title)
        if len(self.__students) >= self.max_students:
            raise module_ex_group_limit.InvalidGroupListError(self.max_students)
        self.__students.append(student)
        logger.info('A new student has been added to the list')

    # search student
    def search_stud(self, surname: str):
        """
        The function searches for all student by last name in the group, when it finds it adds to the list
        :param surname: searched surname
        :return: list in link form
        """
        self.res_search = []
        for student in self.__students:
            if student.surname == surname:
                self.res_search.append(student)
        return self.res_search

    # del student
    def stud_del(self, surname: str):
        """
        The function removes the student from the group by surname
        :param surname: surname of the student to be deleted
        :return: no return, only remove
        """
        for student in self.__students:
            if student.surname == surname:
                self.__students.remove(student)

    def __str__(self):
        return f"Students {self.title} list:\n{'_' * 45}\n" + '\n'.join(map(str, self.__students)) + '\n'
