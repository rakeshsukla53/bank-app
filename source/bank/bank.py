
from customer import Customer
from exceptions import KeyError

class Bank(object):
    """ All the bank operations are contained in this class e.g customer Registration """

    def __init__(self, name):
        self.name = str(name)
        self.customers = dict()
        self.registration_customer(name)

    def registration_customer(self, name):
        """ Registration of a new user to the bank
        Args:
            name (str): name of the customer
        """
        name = str(name)
        if not self.customers.get(name, None):
            self.customers[name] = Customer(name)

    def close_customer_account(self, name, account_type):
        """ close an account of a customer by name and account_type
        Args:
            name (str) : name of the account holder
            account_type (str) : type of account
        """
        name = str(name)
        account_type = str(account_type)
        customer = self.customers.get(name, None)
        if customer:
            customer.close_account(account_type)

    def get_customer_info(self, name):
        """ get customer info
        Args:
            name (str) : name of the customer
        """

        if not self.customers[name]:
            raise KeyError('I am sorry! Customer does not exist')

        return self.customers[name]
