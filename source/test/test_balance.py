
import unittest
import sys
sys.path.append('../bank')
from balance import Balance


class TestBalanceMethods(unittest.TestCase):
    """ Test the methods of balance class """

    @classmethod
    def setUp(self):
        """ setting up data fixture """
        self.balance = Balance()

    def test_add(self):
        """ test add method in Balance """
        self.balance.add(10)
        self.assertEqual(self.balance.get_balance(), 10)

    def test_positive_integer(self):
        """ test positive integer values """
        self.balance.add(100)
        self.assertEqual(self.balance.get_balance(), 100)

    def test_float_values(self):
        """ test floating point values """
        self.balance.add(110.50)
        self.assertEqual(self.balance.get_balance(), 110)

    def test_string_integer(self):
        """ test string integer values """
        self.balance.add('100')
        self.assertEqual(self.balance.get_balance(), 100)

    def test_string(self):
        """ test string values """
        self.assertRaises(ValueError, self.balance.add, 'a')

    def test_substract(self):
        """ test subtract method """
        self.balance.subtract(1)
        self.assertEqual(self.balance.get_balance(), -1)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBalanceMethods)
unittest.TextTestRunner(verbosity=2).run(suite)
