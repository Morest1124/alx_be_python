# bank_account.py

class BankAccount:
    """
    A class to represent a simple bank account that encapsulates
    basic banking operations like deposit, withdrawal, and balance display.
    """

    def __init__(self, initial_balance=0.0):
        """
        Initializes the BankAccount with an optional initial balance.

        Args:
            initial_balance (float, optional): The starting balance of the account. 
                                               Defaults to 0.0.
        """
        self.account_balance = float(initial_balance)

    def deposit(self, amount):
        """
        Adds the specified amount to the account balance.
        It is assumed the amount is a positive number.

        Args:
            amount (float): The amount to deposit.
        """
        if amount > 0:
            self.account_balance += amount
        else:
            print("Warning: Deposit amount should be positive.")

    def withdraw(self, amount):
        """
        Deducts the specified amount from the account balance if funds are sufficient.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            bool: True if the withdrawal was successful, False if funds were insufficient.
        """
        if amount > 0 and self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        The balance is formatted to two decimal places.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")