class Person(object):
    def __init__(self, fname, lname, age, id_no):
        self._fname = fname
        self._lname = lname
        self._id_no = id_no
        self._age = age
    def return_personal_info(self):
        personal_details = {'Name': (self._fname + '' + self._lname),
                            'Id_No': self._id_no, 'Age': self._age}
        return personal_details

class Doctor(Person):
    def __init__(self, fname, lname, age, id_no, doctor_hospital_id):
        self.__doctor_hospital_id = doctor_hospital_id
        super().__init__(fname, lname, age, id_no)

    def return_personal_info(self):
        personal_details = {'Name': (self._fname + '' + self._lname),
                            'Id_No': self._id_no, 'Age': self._age,
                            'Hospital_id': self.__doctor_hospital_id}
        return personal_details

    def can_treat_patient(self):
        return True

    def order_lab_test(self, patient_hospital_id, test_type, instructions):
        test_details = {patient_hospital_id:(test_type, [instructions])}
        return test_details


class Nurse(Person):
    def __init__(self, fname, lname, age, id_no, nurse_hospital_id):
        self.__nurse_hospital_id = nurse_hospital_id
        super().__init__(fname, lname, age, id_no)
        
    def return_personal_info(self):
        personal_details = {'Name': self._fname + '' + self._lname,
                            'Id_No': self._id_no, 'Age': self._age,
                            'Hospital_id': self.__nurse_hospital_id}
        return personal_details

    def can_treat_patient(self):
        return True


class LabTech(Person):
    def __init__(self, fname, lname, age, id_no, lab_tech_hospital_id):
        self.__lab_tech_id = lab_tech_hospital_id
        super().__init__(fname, lname, age, id_no)

    def return_personal_info(self):
        personal_details = {'Name': self._fname + '' + self._lname,
                            'Id_No': self._id_no, 'Age': self._age,
                            'Hospital_id': self.__lab_tech_id}
        return personal_details

    def can_treat_patient(self):
        return False

    def view_lab_test_request(self, **lab_test_request):
        for k, v in lab_test_request.items():
            lab_test_id = k + '001A' # require a generator to issue unique id for each request
            return lab_test_id

    def return_lab_test_results(self, lab_test_id):
        lab_test_results = {lab_test_id:('results')}
        return lab_test_results


class Patient(Person):
    def __init__(self, fname, lname, age, id_no, patient_hospital_id):
        super().__init__(fname, lname, age, id_no)
        self.__patient_id = patient_hospital_id

    def return_personal_info(self):
        personal_details = {'Name': self._fname + '' + self._lname,
                            'Id_No': self._id_no, 'Age': self._age,
                            'Hospital_id': self.__patient_id}
        return personal_details

    def treatment_history(self, **patient_Med_History):
        return patient_Med_History

def main():
    doctor = Doctor('Boswell', 'Gathu', 55, 29736670, 'BG_1945_DC')
    nurse = Nurse('Jeremy', 'Simpson', 34, 3426837, 'JS_1234_NU')
    labtech = LabTech('Nyachanga', 'Gita', 47, 6390364, 'NG_4560_LT')
    patient = Patient('Joshua', 'Mutuika', 89, 4379273, 'patient_D_105')


    # print(isinstance(doc1, Doctor))
    print('Doctor Details  :', doctor.return_personal_info())
    print('Nurse Details   :', nurse.return_personal_info())
    print('LabTech Details :', labtech.return_personal_info())
    print('Patient Details :', patient.return_personal_info())

if __name__ == '__main__':main()