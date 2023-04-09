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

        :param amount: Amount to deposit

        """
        try:
            self.account_balance += float(amount)
            return True
        except ValueError:
            return False

    def withdraw(self, amount: float) -> bool:
        """

        :param amount: Amount to withdraw

        """
        try:
            self.account_balance -= float(amount)
            return True
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
