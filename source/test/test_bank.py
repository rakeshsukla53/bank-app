

import unittest
import sys
sys.path.append('../bank')
from bank import Bank


class TestBankMethods(unittest.TestCase):
    """ test bank methods """

    @classmethod
    def setUp(self):
        self.bank = Bank('Bikash')

    def test_registration(self):
        """ test customer registration """
        customer = self.bank.get_customer_info('Bikash')
        self.assertEqual('Bikash', customer.name)

    def test_customer_info(self):
        """ test customer info """
        customer1 = self.bank.get_customer_info('Bikash')
        customer2 = self.bank.get_customer_info
        self.assertEqual('Bikash', customer1.name)
        self.assertRaises(KeyError, customer2, 'Rakesh')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBankMethods)
unittest.TextTestRunner(verbosity=2).run(suite)
