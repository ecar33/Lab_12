class Account:
    """
    A class representing a person's bank account object
    """

    def __init__(self, name: str):
        """

        :param self.account_name: Person's name
        :param self.account_balance: Person's account balance

        """
        self.account_name = name
        self.account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Method to deposit funds from account
        :param amount: Amount to deposit

        """
        try:
            # Check if amount is a float
            amount = float(amount)
            if amount >= 0:
                # Check if amount is positive
                self.account_balance += amount
                return True
            else:
                return False
        except ValueError:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        Method to withdraw funds from account
        :param amount: Amount to withdraw

        """
        try:
            # Check if amount is a float
            amount = float(amount)
            if (amount >= 0) and (amount <= self.account_balance):
                # Check if amount is positive and less than or equal to current balance
                self.account_balance -= float(amount)
                return True
            else:
                return False
        except ValueError:
            return False

    def get_balance(self) -> float:
        """

        :return: Account balance

        """
        return self.account_balance

    def get_name(self) -> str:
        """

        :return: Account name

        """
        return self.account_name
