
from balance import Balance
from exceptions import ValueError

class Account(object):
    """ account related information and operations are contained here """

    def __init__(self, name):
        self.name = str(name)
        self.balance = Balance()

    def withdrawal(self, money):
        """ withdrawal from account if self.balance._total >= money
        Args:
            money (int) : money is dollars
        """
	money = int(money)
        if not self.balance.get_balance() > money:
            raise ValueError("I am sorry! Your balance is less than {}".format(money))

        if self.balance.get_balance() >= money:
            self.balance.subtract(money)

    def deposit(self, money):
        """ deposit to your account
        Args:
            money (int) : money in dollars
        """
	money = int(money)
        self.balance.add(money)

    def get_balance(self):
        """ get balance amount
        Returns:
            self.balance._total (int) : balance left
        """
        return self.balance.get_balance()

    def transfer(self, recipient_name, account_type, money):
        """ transfer money to recipient_name
        Args:
            recipient_name (Customer): it should be the object of type Customer
            account_type (str): the type of account
            money (int): money in dollars to be transferred
        """

	account_type = str(account_type) 
	money = int(money)
        if not self.balance.get_balance() > money:
            raise ValueError("I am sorry! Amount cannot be transferred. Your balance is less than {}".format(money))

        if self.balance.get_balance() >= money:
            self.balance.subtract(money)

        recipient_account = recipient_name.accounts[account_type]
        recipient_balance = recipient_account.balance
        recipient_balance.add(money)

