class Human():
    def __init__(self, surname: str, name: str, person_id: int):
        """
        Base class
        :param surname: Surname of human
        :param name: Name of human
        :param person_id: Persons number of human
        """
        self.surname = surname
        self.name = name
        self.person_id = person_id

    def __str__(self):
        return f'{self.surname} {self.name} {self.person_id}'
