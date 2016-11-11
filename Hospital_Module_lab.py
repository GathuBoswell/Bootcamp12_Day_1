class Person(object):
    def __init__(self, fname, lname, age, id_no):
        self.__fname = fname
        self.__lname = lname
        self.__id_no = id_no
        self._age = age
    def __str__(self):
        return self.__fname + ' ' + self.__lname

class Doctor(Person):
    def _init__(self,fname, lname, age, id_no, doctor_hospital_id):
        self.__doctor_hospital_id = doctor_hospital_id
        super().__init__(self)

    def can_treat_patient(self):
        return True


class Nurse(Person):
    def _init__(self,fname, lname, age, id_no, nurse_hospital_id):
        self.__nurse_hospital_id = nurse_hospital_id
        super().__init__(self)

    def can_treat_patient(self):
        return True


class Lab_Tech(Person):
    def _init__(self,fname, lname, age, id_no, lab_tech_hospital_id):
        self.__lab_tech_id = lab_tech_hospital_id
        super().__init__(self)

    def can_treat_patient(self):
        return False


class Patient(Person):
    pass