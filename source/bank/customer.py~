
from account import Account

class Customer(object):
    """ the customer of the bank """

    def __init__(self, name):
        """ instantiate the customer """
        self.name = name
        self.accounts = dict()

    def register_account(self, account_type):
        """ add a new account by account_type
        Args:
            account_type str(): type of the account
        """
        account_type = str(account_type)
        if not self.accounts.get(account_type, None):
            self.accounts[account_type] = Account(account_type)

    def close_account(self, name):
        """ close the account based on type of account
        Args:
            name (str) : type of account e.g saving
        """
        name = str(name)
        self.accounts.pop(name, None)

    def deposit_account(self, account_type, money):
        """
        Deposit money into your account based on your account_type
        Args:
            account_type (str): type of your account
            money (int): money in dollars
        """
        account_type = str(account_type)
        money = int(money)
        account = self.accounts.get(account_type, None)
        if account:
            account.deposit(money)

    def withdrawal_account(self, account_type, money):
        """ withdrawal from account based on account type
        Args:
            account_type (str): type of account
            money (int): money in dollars
        """
        account_type = str(account_type)
        money = int(money)
        account = self.accounts.get(account_type, None)
        if account:
            account.withdrawal(money)

    def get_account_totals(self):
        """ get the totals for all accounts
        """

        return sum([account.get_balance for account in self.accounts.values()])
