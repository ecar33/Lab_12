class Account:
    """
    A class representing a person's bank account object
    """

    def __init__(self, name: str):
        """
        Constructor to create the initial state of an Account object.
        :param name: The name of the account holder as a string.
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Method to deposit funds from account
        :param amount: Amount to deposit
        :return: Success/failure to deposit

        """
        try:
            # Check if amount is a float
            amount = float(amount)
            if amount > 0:
                # Check if amount is positive
                self.__account_balance += amount
                return True
            else:
                return False
        except ValueError:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        Method to withdraw funds from account
        :param amount: Amount to withdraw
        :return: Success/failure to withdraw

        """
        try:
            # Check if amount is a float
            amount = float(amount)
            if (amount >= 0) and (amount <= self.get_balance()):
                # Check if amount is positive and less than or equal to current balance
                self.__account_balance -= float(amount)
                return True
            else:
                return False
        except ValueError:
            return False

    def get_balance(self) -> float:
        """
        Method to obtain the account's balance
        :return: Account balance

        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Method to obtain the account's name
        :return: Account name

        """
        return self.__account_name
