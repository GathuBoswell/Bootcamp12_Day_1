class Person(object):
    def __init__(self, fname, lname, age, id_no):
        self.__fname = fname
        self.__lname = lname
        self.__id_no = id_no
        self._age = age
    def __str__(self):
        return self.__fname + ' ' + self.__lname

class Doctor(Person):
    def __init__(self, fname, lname, age, id_no, doctor_hospital_id):
        super().__init__(fname, lname, age, id_no)
        self.__doctor_hospital_id = doctor_hospital_id

    def can_treat_patient(self):
        return True


class Nurse(Person):
    def __init__(self, fname, lname, age, id_no, nurse_hospital_id):
        self.__nurse_hospital_id = nurse_hospital_id
        super().__init__(fname, lname, age, id_no)

    def can_treat_patient(self):
        return True


class LabTech(Person):
    def __init__(self, fname, lname, age, id_no, lab_tech_hospital_id):
        self.__lab_tech_id = lab_tech_hospital_id
        super().__init__(fname, lname, age, id_no)

    def can_treat_patient(self):
        return False


class Patient(Person):
    def __init__(self, fname, lname, age, id_no, patient_hospital_id):
        super().__init__(fname, lname, age, id_no)
        self.__patient_id = patient_hospital_id


    def treatment_history(self, **patient_Med_History):
        pass

def main():
    doc1 = Doctor('Boswell', 'Gathu', 55, 29736670, 'BG' )
    print(isinstance(doc1, Doctor))
    print(doc1.__str__())

if __name__ == '__main__':main()