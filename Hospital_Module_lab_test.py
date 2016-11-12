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

    def test_doctor_str(self):
        doc1 = Doctor('Boswell', 'Gathu', 55, 29736670, 'BGathu234')
        self.assertEqual('Boswell Gathu', doc1.__str__(), msg='The str should return `Boswell Gathu`')
