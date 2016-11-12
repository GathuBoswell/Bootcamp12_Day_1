import unittest

from Hospital_Module_lab import Person, Doctor, Nurse, Lab_Tech, Patient

class HospitaLModuleTest(unittest.TestCase):
    """
        Class to test the Hospital_Module_lab
    """
    def test_doctor_instance(self):
        doc1 = Doctor('Boswell', 'Gathu', 55, 29736670)
        self.assertIsInstance(doc1, Person, msg='The object should be an instance of the `Person` class')
