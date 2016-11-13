import unittest

from Hospital_Module_lab import Person, Doctor, Nurse, LabTech, Patient

class HospitaLModuleTest(unittest.TestCase):
    """
        Class to test the Hospital_Module_lab
    """
    def test_doctor_instance(self):
        doc1 = Doctor('Boswell', 'Gathu', 55, 29736670, 'BGathu234')
        self.assertIsInstance(doc1, Person, msg='The object should be an instance of the `Person` class')

    def test_nurse_instance(self):
        doc1 = Nurse('Wysla', 'James', 34, 217456, 'WJames1B')
        self.assertIsInstance(doc1, Person, msg='The object should be an instance of the `Nurse` class')

    def test_labtech_instance(self):
        doc1 = LabTech('Stella', 'Jones', 23, 29823440, 'SJones14C')
        self.assertIsInstance(doc1, Person, msg='The object should be an instance of the `LabTech` class')

    def test_patient_instance(self):
        doc1 = Patient('Ngecha', 'Maistor', 69, 1345672, 'P123M4')
        self.assertIsInstance(doc1, Person, msg='The object should be an instance of the `Patient` class')

    def test_doctor_personal_info(self):
        doc1 = Doctor('Boswell', 'Gathu', 55, 29736670, 'BG_1945_DC')
        self.assertEqual({'Hospital_id': 'BG_1945_DC', 'Id_No': 29736670, 'Age': 55, 'Name': 'BoswellGathu'},
                         doc1.return_personal_info())

    def test_nurse_personal_info(self):
        nurse = Nurse('Jeremy', 'Simpson', 34, 3426837, 'JS_1234_NU')
        self.assertEqual({'Hospital_id': 'JS_1234_NU', 'Id_No': 3426837, 'Age': 34, 'Name': 'JeremySimpson'},
                         nurse.return_personal_info())

    def test_labtech_personal_info(self):
        labtech = LabTech('Nyachanga', 'Gita', 47, 6390364, 'NG_4560_LT')
        self.assertEqual({'Hospital_id': 'NG_4560_LT', 'Id_No': 6390364, 'Age': 47, 'Name': 'NyachangaGita'},
                         labtech.return_personal_info())

    def test_patient_personal_info(self):
        patient = Patient('Joshua', 'Mutuika', 89, 4379273, 'patient_D_105')
        self.assertEqual({'Hospital_id': 'patient_D_105', 'Id_No': 4379273, 'Age': 89, 'Name': 'JoshuaMutuika'},
                         patient.return_personal_info())
