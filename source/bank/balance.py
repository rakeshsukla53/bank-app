
class Balance(object):
    """ all balance related operations are contained here  """

    def __init__(self):
        """ instantiate the balance class, default value 0 """
        self._total = 0

    def add(self, value):
        """ add value to balance amount
        Args:
            value (int): numeric value to be added
        """
        value = int(value)
        self._total += value

    def subtract(self, value):
        """ subtract value from the balance amount
        Args:
            value (int): numeric value
        """
        value = int(value)
        self._total -= value

    def get_balance(self):
        """ return the value amount of the account
        Returns:
            self._total (int): return balance amount
        """
        return self._total

