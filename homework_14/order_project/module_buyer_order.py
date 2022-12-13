class Buyer():
    def __init__(self, surname: str, name: str, phone: str, email: str):
        """
        Function for typical created new buyer
        :param surname: buyers surname
        :param name: buyers name
        :param phone: contact number phone
        :param email: contact email address
        """
        self.surname = surname
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f'{self.surname} {self.name[0]}. {self.phone} {self.email}'
