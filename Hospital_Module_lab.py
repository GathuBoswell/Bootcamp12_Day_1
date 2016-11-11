class Person(object):
    def __init__(self, fname, lname, age, id_no):
        self.__fname = fname
        self.__lname = lname
        self.__id_no = id_no
        self._age = age


class Doctor(Person):
    pass


class Nurse(Person):
    pass


class Lab_Tech(Person):
    pass


class Patient(Person):
    pass