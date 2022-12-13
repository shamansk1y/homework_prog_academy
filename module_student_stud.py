import module_human_stud

class Student(module_human_stud.Human):
    def __init__(self, surname, name, person_id, programming_language: str):
        """
        Create sub class from mother class Human
        :param surname: Take mather class parametr
        :param name : Take mather class parametr
        :param person_id: Take mather class parametr
        :param programming_language: Name of programming languege
        """
        if not isinstance(person_id, int):
            raise TypeError()
        super().__init__(surname, name, person_id)
        self.programming_language = programming_language

    def __str__(self):
        return super().__str__() + f' {self.programming_language}'
