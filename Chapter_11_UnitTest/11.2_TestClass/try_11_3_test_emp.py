import unittest
from try_11_3_employee import Employee

class TestEmpCase(unittest.TestCase):
    def setUp(self):

        self.add = Employee('Victor', 'Delacroix', 6000)

    def test_give_default_raise(self):
        self.assertEqual(self.add.give_raise(), 11000)

    def test_give_custom_raise(self):
        self.assertEqual(self.add.give_raise(10000), 16000)

unittest.main()