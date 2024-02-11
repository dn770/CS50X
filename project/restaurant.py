
class Restaurant:

    def __init__(self, name, address, phone_number, description):
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number
        self.__description = description


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        self.__phone_number = phone_number

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description
